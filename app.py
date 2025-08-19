from flask import Flask, request
from dotenv import load_dotenv
import os
from utils.db import test_connection

# Load environment variables from the .env file
load_dotenv()

# Initialize the Flask app
app = Flask(__name__)

# A simple route to test if the server is running
@app.route('/')
def home():
    return "Employee Onboarding Automation Backend is running!"

# This is the endpoint that will receive data from the Google Form webhook
@app.route('/webhook', methods=['POST'])
def handle_webhook():
    # You will add the logic to process the data here
    if request.method == 'POST':
        data = request.json
        print("Received data from webhook:", data)
        # TODO: Add logic to save data to MongoDB and trigger email flows
        return {"status": "success", "message": "Data received and processing started"}, 200
    else:
        return {"status": "error", "message": "Method not allowed"}, 405

if __name__ == '__main__':
    # Test the database connection
    test_connection()
    # Use environment variables for the port and debug mode
    app.run(debug=os.getenv("FLASK_DEBUG", True))