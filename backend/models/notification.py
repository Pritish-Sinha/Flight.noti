from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client.flightDB

notifications = [
    {
        "notification_id": "1",
        "flight_id": "6E 2341",
        "message": "Your flight 6E 2341 is on time. Departure gate: A12.",
        "timestamp": "2024-07-26T13:00:00Z",
        "method": "SMS",
        "recipient": "+1234567890"
    },
    {
        "notification_id": "2",
        "flight_id": "6E 2342",
        "message": "Your flight 6E 2342 is delayed. New departure time: 2024-07-26T17:00:00Z. Departure gate: C3.",
        "timestamp": "2024-07-26T15:30:00Z",
        "method": "Email",
        "recipient": "user@example.com"
    },
    {
        "notification_id": "3",
        "flight_id": "6E 2343",
        "message": "Your flight 6E 2343 has been cancelled.",
        "timestamp": "2024-07-26T11:00:00Z",
        "method": "App",
        "recipient": "user_app_id_12345"
    }
]

db.notifications.insert_many(notifications)
