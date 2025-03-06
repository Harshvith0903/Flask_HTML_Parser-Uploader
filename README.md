# Flask HTML Parser & Uploader

This is a Flask-based web application that serves HTML templates and handles file uploads.

## Features
- Flask backend for serving web pages
- Supports file uploads (stored in the `uploads/` directory)
- Template-based HTML rendering

## Installation
### Prerequisites
Ensure you have the following installed:
- Python (>= 3.8)
- pip (Python package manager)

### Steps to Install and Run
1. **Clone the repository:**
   ```sh
   git clone https://github.com/yourusername/html-flask-project.git
   cd html-flask-project
   ```

2. **Create a virtual environment and activate it:**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

4. **Run the Flask application:**
   ```sh
   python app.py
   ```

5. **Open the application in a web browser:**
   ```
   http://127.0.0.1:5000/
   ```

## Folder Structure
```
HTML/
│── uploads/      # Directory for uploaded files
│── templates/    # HTML template files
│── app.py        # Main Flask application script
│── test.py       # Testing script
```

## Usage
- Start the Flask application.
- Access the web interface.
- Upload files (if supported by the app).

## Contributing
Feel free to submit issues or pull requests.

## License
This project is licensed under the MIT License.
