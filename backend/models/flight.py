from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client.flightDB

flights = [
    {
        "flight_id": "6E 2341",
        "airline": "Indigo",
        "status": "On Time",
        "departure_gate": "A12",
        "arrival_gate": "B7",
        "scheduled_departure": "2024-07-26T14:00:00Z",
        "scheduled_arrival": "2024-07-26T18:00:00Z",
        "actual_departure": "2024-07-26T14:00:00Z",
        "actual_arrival": "2024-07-26T18:00:00Z"
    },
    {
        "flight_id": "6E 2342",
        "airline": "Indigo",
        "status": "Delayed",
        "departure_gate": "C3",
        "arrival_gate": "D4",
        "scheduled_departure": "2024-07-26T16:00:00Z",
        "scheduled_arrival": "2024-07-26T20:00:00Z",
        "actual_departure": "2024-07-26T18:30:00Z",
        "actual_arrival": "2024-07-26T21:30:00Z"
    },
    {
        "flight_id": "6E 2343",
        "airline": "Indigo",
        "status": "Cancelled",
        "departure_gate": "E2",
        "arrival_gate": "F1",
        "scheduled_departure": "2024-07-26T12:00:00Z",
        "scheduled_arrival": "2024-07-26T16:00:00Z",
        "actual_departure": None,
        "actual_arrival": None
    }
]

db.flights.insert_many(flights)
