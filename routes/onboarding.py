from flask import Blueprint, request, jsonify
from controllers.onboarding_controller import handle_onboarding_webhook

onboarding_bp = Blueprint('onboarding_bp', __name__)

@onboarding_bp.route('/webhook', methods=['POST'])
def webhook_receiver():
    data = request.json
    return handle_onboarding_webhook(request, data) # Pass the full request object