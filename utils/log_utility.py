import logging
from flask import jsonify

def log_api_request(request):
    """Logs details of an incoming API request."""
    logging.info(f"API Request - Method: {request.method}, Path: {request.path}, IP: {request.remote_addr}")
    if request.is_json:
        logging.info(f"Request Body: {request.json}")

def log_api_response(response, status_code):
    """Logs details of an outgoing API response."""
    logging.info(f"API Response - Status: {status_code}, Response Body: {response}")