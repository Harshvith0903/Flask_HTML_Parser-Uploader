# HTML Processing and Data Extraction System

## Overview
This project is a Flask-based web application that processes multiple HTML files, extracts relevant data, and generates an output Excel file. The application provides a web interface for uploading HTML files and selecting files for processing.

## Features
- Upload multiple HTML files.
- Extract structured data from HTML content.
- Generate an Excel file (`output.xlsx`) with extracted data.
- Web-based interface using Flask templates.

## Project Structure
```
HTML-Processing-App/
│── app.py                  # Main Flask application
│── requirements.txt        # Project dependencies
│── uploads/                # Stores uploaded HTML files
│   ├── sample1.html
│   ├── sample2.html
│   ├── output.xlsx         # Generated Excel file
│── templates/              # HTML templates for the web interface
│   ├── upload.html
│   ├── select_files.html
│── .git/                   # Version control files
```

## Installation

### Prerequisites
- Python 3.x
- Flask and required dependencies (see `requirements.txt`)

### Setup
1. **Clone the repository:**
   ```sh
   git clone <repo-url>
   cd HTML-Processing-App
   ```
2. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
3. **Run the Flask application:**
   ```sh
   python app.py
   ```

## Usage
1. **Open the web interface** in your browser (`http://127.0.0.1:5000`).
2. **Upload HTML files** via the web interface.
3. **Select files for processing** and extract relevant data.
4. **Download the generated Excel file (`output.xlsx`)** with extracted content.

## Future Enhancements
- Automate email notifications for processed files.
- Implement better data validation and extraction.
- Improve UI for enhanced user experience.

