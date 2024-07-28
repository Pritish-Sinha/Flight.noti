# Flight.noti
#### An Indigo Flight Notification Service

## Project Overview
This project is a Flight Notification Service that notifies users about the status of their flights via mobile app notifications, SMS, and email. 

## Tech Stack

### Frontend
- **React**: For building the user interface
- **Firebase**: For handling push notifications

### Backend
- **Flask**: For creating the server and API endpoints
- **MongoDB**: For storing flight and notification data
- **Firebase Admin SDK**: For sending push notifications
- **Twilio**: For sending SMS notifications
- **SMTP**: For sending email notifications

### Additional Tools and Libraries
- **dotenv**: For managing environment variables
- **flask-cors**: For handling Cross-Origin Resource Sharing (CORS)
- **twilio**: Twilio's Python library for SMS
- **smtplib**: Python's built-in library for sending emails

## Setup Instructions

### Prerequisites
- Node.js
- Python
- MongoDB
- Firebase account
- Twilio account
- Email account (Gmail recommended)

### Backend Setup

1. **Clone the repository**:
    ```bash
    git clone git@github.com:Pritish-Sinha/Flight.noti.git
    cd ../backend
    ```

2. **Create a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Setup MongoDB**:
    - Install MongoDB and MongoDB Compass from the [official website](https://www.mongodb.com/try/download/community).
    - Create a new database named `flight_noti` and a collection named `flights`.

5. **Setup Firebase**:
    - Go to the [Firebase Console](https://console.firebase.google.com/) and create a new project.
    - Navigate to Project Settings > Service accounts.
    - Generate a new private key and download the `serviceAccountKey.json` file.
    - Place the `serviceAccountKey.json` file in the `backend` directory.

6. **Setup Twilio**:
    - Sign up or log in to [Twilio](https://www.twilio.com/).
    - Get your Account SID, Auth Token, and a Twilio phone number.
    - Add these details to the `.env` file.

7. **Setup Email**:
    - Use a Gmail account and generate an App Password.
    - Add your email address and app password to the `.env` file.

8. **Start the backend server**:
    ```bash
    python app.py
    ```

### Frontend Setup

1. **Navigate to the frontend directory**:
    ```bash
    cd ../frontend
    ```

2. **Install dependencies**:
    ```bash
    npm install
    ```

3. **Setup Firebase**:
    - Go to the [Firebase Console](https://console.firebase.google.com/) and navigate to Project Settings > General.
    - In the "Your apps" section, select the web icon to register a new web app.
    - Follow the instructions to get your Firebase configuration and update `firebase.js`.

4. **Start the frontend server**:
    ```bash
    npm start
    ```

### Environment Variables
Create a `.env` file in the `backend` directory with the following content:

```plaintext
MONGO_URI=your_mongo_uri
TWILIO_ACCOUNT_SID=your_twilio_account_sid
TWILIO_AUTH_TOKEN=your_twilio_auth_token
TWILIO_PHONE_NUMBER=your_twilio_phone_number
EMAIL_ADDRESS=your_email_address
EMAIL_PASSWORD=your_email_password
```

### Usage

   - Start the backend server and the frontend server.
   - Use the frontend application to send flight status notifications via mobile app, SMS, or email.

### Demo
- Due to limited access to the above-mentioned API services, the backend is not yet running actively. You need to run it locally with the newly created keys. 
- The demo for the frontend is available through Vercel deployment [Flight.Noti](https://flight-noti.vercel.app/)
