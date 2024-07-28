import React, { useState } from 'react';
import axios from 'axios';
import './NotificationForm.css';

const NotificationForm = () => {
    const [flightId, setFlightId] = useState('');
    const [name, setName] = useState('');
    const [dateOfTravel, setDateOfTravel] = useState('');
    const [method, setMethod] = useState('');
    const [recipient, setRecipient] = useState('');
    const [statusMessage, setStatusMessage] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();
        setStatusMessage('Sending...');
        try {
            const response = await axios.post('http://localhost:5000/notifications', {
                flight_id: flightId,
                name: name,
                date_of_travel: dateOfTravel,
                method: method,
                recipient: method === 'App' ? '' : recipient,
            });
            setStatusMessage('Notification sent successfully!');
        } catch (error) {
            setStatusMessage('Error sending notification. Please try again.');
        }
    };

    return (
        <div className="notification-form-container">
            <form className="notification-form" onSubmit={handleSubmit}>
                <h2>Set your notifications</h2>
                <input
                    type="text"
                    placeholder="Name"
                    value={name}
                    onChange={(e) => setName(e.target.value)}
                    required
                />
                <input
                    type="text"
                    placeholder="Flight ID"
                    value={flightId}
                    onChange={(e) => setFlightId(e.target.value)}
                    required
                />
                <input
                    type="date"
                    placeholder="Date of Travel"
                    value={dateOfTravel}
                    onChange={(e) => setDateOfTravel(e.target.value)}
                    required
                />
                <select
                    value={method}
                    onChange={(e) => setMethod(e.target.value)}
                    required
                >
                    <option value="">Select notification method</option>
                    <option value="App">App</option>
                    <option value="SMS">SMS</option>
                    <option value="Email">Email</option>
                </select>
                {method === 'SMS' && (
                    <input
                        type="text"
                        placeholder="Enter phone number"
                        value={recipient}
                        onChange={(e) => setRecipient(e.target.value)}
                        required
                    />
                )}
                {method === 'Email' && (
                    <input
                        type="email"
                        placeholder="Enter email address"
                        value={recipient}
                        onChange={(e) => setRecipient(e.target.value)}
                        required
                    />
                )}
                <button type="submit">Send</button>
                {statusMessage && <p className="status-message">{statusMessage}</p>}
            </form>
        </div>
    );
};

export default NotificationForm;
