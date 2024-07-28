import React, { useEffect, useState } from 'react';
import axios from 'axios';

const FlightStatus = () => {
  const [flights, setFlights] = useState([]);

  useEffect(() => {
    axios.get('http://localhost:5000/flights')
      .then(response => setFlights(response.data))
      .catch(error => console.error(error));
  }, []);

  return (
    <div>
      <h2>Flight Status</h2>
      <ul>
        {flights.map(flight => (
          <li key={flight.flight_id}>
            {flight.flight_id} - {flight.status}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default FlightStatus;
