import os
from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from firebase_admin import credentials, initialize_app, messaging
from dotenv import load_dotenv
from flask_cors import CORS
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from twilio.rest import Client

load_dotenv()

app = Flask(__name__)
CORS(app)
app.config["MONGO_URI"] = os.getenv("MONGO_URI")
mongo = PyMongo(app)

# Initialize Firebase Admin SDK
cred = credentials.Certificate('serviceAccountKey.json')
initialize_app(cred)

@app.route('/notifications', methods=['POST'])
def send_notification():
    data = request.get_json()
    flight_id = data['flight_id']
    name = data['name']
    date_of_travel = data['date_of_travel']
    method = data['method']
    recipient = data['recipient']

    # Fetch flight details from the database
    flight = mongo.db.flights.find_one({"flight_id": flight_id})

    if not flight:
        return jsonify({"error": "Flight not found"}), 404

    # Determine the flight status and create the notification message
    if flight['status'] == "On Time":
        message = f"Dear {name}, your flight {flight_id} is on time. Departure gate: {flight['departure_gate']}."
    elif flight['status'] == "Delayed":
        message = f"Dear {name}, your flight {flight_id} is delayed. New departure time: {flight['actual_departure']}. Departure gate: {flight['departure_gate']}."
    elif flight['status'] == "Cancelled":
        message = f"Dear {name}, your flight {flight_id} has been cancelled."
    else:
        message = f"Dear {name}, status update for your flight {flight_id}: {flight['status']}."

    notification_data = {
        "flight_id": flight_id,
        "name": name,
        "date_of_travel": date_of_travel,
        "message": message,
        "timestamp": flight['scheduled_departure'],
        "method": method,
        "recipient": recipient
    }

    mongo.db.notifications.insert_one(notification_data)

    # Send notification based on the selected method
    if method == "App":
        # Send notification using Firebase Admin SDK
        notification_message = messaging.Message(
            notification=messaging.Notification(
                title='Flight Status Update',
                body=message
            ),
            token=recipient
        )
        try:
            response = messaging.send(notification_message)
            print('Successfully sent message:', response)
        except messaging.ApiCallError as e:
            print('Error sending message:', e)
    elif method == "SMS":
        # Send SMS using Twilio
        account_sid = os.getenv('TWILIO_ACCOUNT_SID')
        auth_token = os.getenv('TWILIO_AUTH_TOKEN')
        client = Client(account_sid, auth_token)
        try:
            message = client.messages.create(
                body=message,
                from_=os.getenv('TWILIO_PHONE_NUMBER'),
                to=recipient
            )
            print('Successfully sent SMS:', message.sid)
        except Exception as e:
            print('Error sending SMS:', e)
    elif method == "Email":
        # Send Email using SMTP
        email_address = os.getenv('EMAIL_ADDRESS')
        email_password = os.getenv('EMAIL_PASSWORD')
        msg = MIMEMultipart()
        msg['From'] = email_address
        msg['To'] = recipient
        msg['Subject'] = 'Flight Status Update'
        msg.attach(MIMEText(message, 'plain'))
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(email_address, email_password)
            text = msg.as_string()
            server.sendmail(email_address, recipient, text)
            server.quit()
            print('Successfully sent email')
        except Exception as e:
            print('Error sending email:', e)

    return jsonify({"message": "Notification sent!"}), 200

if __name__ == "__main__":
    app.run(debug=True)
