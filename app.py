from flask import Flask, request
from dotenv import load_dotenv
import os
from utils.db import test_connection
from routes.onboarding import onboarding_bp

# Load environment variables from the .env file
load_dotenv()

# Initialize the Flask app
app = Flask(__name__)

# Register blueprints
app.register_blueprint(onboarding_bp, url_prefix='/api')

# A simple route to test if the server is running
@app.route('/')
def home():
    return "Employee Onboarding Automation Backend is running!"

if __name__ == '__main__':
    # Test the database connection
    test_connection()
    # Use environment variables for the port and debug mode
    app.run(debug=os.getenv("FLASK_DEBUG", True))