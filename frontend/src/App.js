import React, { useState } from 'react';
import './App.css';

function App() {
  const [city, setCity] = useState('');
  const [report, setReport] = useState(null);

  const getAgriData = async () => {
    // This calls the "api" folder we created
    const response = await fetch(`/api/message?city=${city}`);
    const data = await response.json();
    setReport(data);
  };

  return (
    <div style={{ padding: '50px', backgroundColor: '#f0fdf4', minHeight: '100vh' }}>
      <h1>🌱 AgriCloud Smart Dashboard</h1>
      <input 
        placeholder="Enter your City..." 
        onChange={(e) => setCity(e.target.value)} 
      />
      <button onClick={getAgriData}>Get Farming Advice</button>

      {report && (
        <div style={{ marginTop: '20px', border: '1px solid green', padding: '20px' }}>
          <h3>Report for {report.city}</h3>
          <p>Temperature: {Math.round(report.temp - 273.15)}°C</p>
          <p><strong>Action: {report.advice}</strong></p>
        </div>
      )}
    </div>
  );
}

export default App;