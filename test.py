import os
from flask import Flask, render_template, request, redirect, url_for, send_from_directory, flash
from werkzeug.utils import secure_filename
from openpyxl import Workbook
from bs4 import BeautifulSoup

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'  # Directory where uploaded files will be stored
app.config['ALLOWED_EXTENSIONS'] = {'html'}  # Allowed file extensions for upload
app.secret_key = 'supersecretkey'  # Secret key for session management

# Ensure upload directory exists
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

def parse_filename(filename):
    parts = filename.split('_')
    if len(parts) < 6:
        return None

    system_name = parts[0]
    department = parts[-5]
    employee_name = parts[-4]
    branch_name = parts[-3]
    location = parts[-2]
    port_number = parts[-1].split('.')[0]

    return {
        'System Name': system_name,
        'Department': department,
        'Employee Name': employee_name,
        'Branch Name': branch_name,
        'Location': location,
        'Port Number': port_number
    }

def extract_system_info_from_html(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')

    computer_name = soup.find('table', class_="reportHeader").find_all('tr')[1].find('td').text.strip()
    os = soup.find_all('div', class_='reportSection rsLeft')[0].find('td').get_text(separator='\n', strip=True).split('\n')[0]
    system_model = soup.find_all('div', class_="reportSection rsRight")[0].find('td').get_text(separator='\n', strip=True).split('\n')[0]
    processor = soup.find_all('div', class_="reportSection rsLeft")[1].find('td').get_text(separator='\n', strip=True).split('\n')[0]
    board = ''.join(soup.find_all('div', class_="reportSection rsRight")[1].find('td').get_text(separator='\n', strip=True).split('\n')[0].split(' ')[1:])
    hard_disk = soup.find_all('div', class_='reportSection rsLeft')[2].find('td').get_text(separator='\n', strip=True).split('\n')[0].split(' ')[0] + 'GB'
    memory = str(int(soup.find_all('div', class_="reportSection rsRight")[2].find('td').get_text(separator='\n', strip=True).split('\n')[0].split(' ')[0]) / 1000) + 'GB'
    ram_slots = soup.find_all('div', class_="reportSection rsRight")[2].find('td').get_text(separator='\n', strip=True).count('Slot')
    graphics = soup.find_all('div', class_="reportSection rsRight")[4].find('td').get_text(separator='\n', strip=True).split('[')[0]
    monitor = soup.find_all('div', class_="reportSection rsRight")[4].find('td').contents[-1].strip().split('[')[0]

    return {
        'Computer Name': computer_name,
        'OS': os,
        'System Model': system_model,
        'Processor': processor,
        'Board': board,
        'Hard Disk': hard_disk,
        'Memory': memory,
        'RAM Slots': ram_slots,
        'Graphic Card': graphics,
        'Monitor': monitor
    }

@app.route('/')
def upload():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'files[]' not in request.files:
        flash('No file part')
        return redirect(request.url)
    files = request.files.getlist('files[]')
    for file in files:
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        else:
            flash('Allowed file types are html')
            return redirect(request.url)
    flash('Files successfully uploaded')
    return redirect(url_for('generate_excel'))

@app.route('/generate_excel')
def generate_excel():
    files = os.listdir(app.config['UPLOAD_FOLDER'])
    files = [f for f in files if f.endswith('.html')]
    directory = app.config['UPLOAD_FOLDER']
    output_file = 'output.xlsx'

    wb = Workbook()
    sheet = wb.active
    sheet.title = 'System Information'

    headers = ['System Name', 'Department', 'Employee Name', 'Branch Name', 'Location', 'Port Number',
               'Computer Name', 'Operating System', 'System Model', 'Processor', 'Board', 'Hard Disk', 'Memory', 'RAM Slots', 'Graphic Card', 'Monitor']
    sheet.append(headers)

    for filename in files:
        file_path = os.path.join(directory, filename)
        file_info = parse_filename(filename)

        if file_info:
            system_info = extract_system_info_from_html(file_path)
            row = [file_info['System Name'], file_info['Department'], file_info['Employee Name'],
                   file_info['Branch Name'], file_info['Location'], file_info['Port Number'],
                   system_info['Computer Name'], system_info['OS'], system_info['System Model'],
                   system_info['Processor'], system_info['Board'], system_info['Hard Disk'],
                   system_info['Memory'], system_info['RAM Slots'], system_info['Graphic Card'], system_info['Monitor']]
            sheet.append(row)

    wb.save(os.path.join(app.config['UPLOAD_FOLDER'], output_file))
    flash(f"Excel file generated successfully: {output_file}")
    return send_from_directory(directory, output_file)

if __name__ == "__main__":
    app.run(debug=True)
