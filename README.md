# Maize Disease Detection

This project is a web application for detecting diseases in maize leaves using deep learning models. It uses Flask for the backend and Keras/TensorFlow for model inference.

## Features
- Upload maize leaf images for disease detection
- Predicts and classifies common maize diseases
- Displays results with disease information

## Project Structure
- `maize-disease-detection/` - Main application folder
  - `app.py` - Flask application
  - `model/` - Contains trained model files (`.h5`)
  - `static/` - Static files (images, CSS, etc.)
  - `templates/` - HTML templates
- `requirements.txt` - Python dependencies
- `env/` - Python virtual environment (not tracked by git)

## Setup Instructions
1. Clone the repository:
   ```sh
   git clone https://github.com/GT-Raph/maaa.git
   cd maaa
   ```
2. Create and activate a virtual environment (optional but recommended):
   ```sh
   python -m venv env
   .\env\Scripts\activate  # On Windows
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Run the application:
   ```sh
   python maize-disease-detection/app.py
   ```
5. Open your browser and go to `http://127.0.0.1:5001`

## Notes
- Large model files (e.g., `.h5` files) are not tracked by git due to GitHub's file size limits. Download or place them manually in the `model/` directory.
- For production deployment, use a WSGI server like Waitress or Gunicorn.

## License
This project is for educational purposes.
