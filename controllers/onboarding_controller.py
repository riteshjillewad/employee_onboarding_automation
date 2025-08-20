from models.employee import Employee
from datetime import timedelta
from utils.db import get_db
from services.mail_service import send_welcome_mail, send_contract_mail # This is new

def handle_onboarding_webhook(data):
    try:
        # 1. Validate the incoming data with the Employee schema
        employee_data = Employee(**data)

        # 2. Auto-calculate the end date from start_date + duration
        end_date = employee_data.start_date + timedelta(days=30 * employee_data.duration)
        employee_data.end_date = end_date

        # 3. Save validated data to MongoDB
        db = get_db()
        employees_collection = db['employees']
        employee_dict = employee_data.model_dump()

        employee_dict['start_date'] = employee_dict['start_date'].isoformat()
        if employee_dict['end_date']:
            employee_dict['end_date'] = employee_dict['end_date'].isoformat()

        result = employees_collection.insert_one(employee_dict)

        if result.acknowledged:
            print(f"Successfully saved employee with ID: {result.inserted_id}")

            # Trigger the email flows
            send_welcome_mail(employee_email=employee_data.email, name=employee_data.name)
            send_contract_mail(employee_email=employee_data.email, name=employee_data.name, end_date=employee_data.end_date)

        return {"status": "success", "message": "Data validated and processed", "employee": employee_data.model_dump()}, 200
    except Exception as e:
        return {"status": "error", "message": str(e)}, 400