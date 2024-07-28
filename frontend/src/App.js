import React from 'react';
import NotificationForm from './components/NotificationForm';
import './App.css';

const App = () => {
    return (
        <div className="app-container">
            <header className="app-header">
                <h1>Flight Status Notifier</h1>
            </header>
            <NotificationForm />
        </div>
    );
};

export default App;
