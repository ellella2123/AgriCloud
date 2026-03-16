import React, { useState } from 'react';

function App() {
  const [city, setCity] = useState('');
  const [report, setReport] = useState(null);
  const [loading, setLoading] = useState(false);

  const getAgriData = async () => {
    if (!city) {
      alert("Please enter a city name first!");
      return;
    }
    setLoading(true);
    try {
      // This calls the Python function at /api/message
      const response = await fetch(`/api/message?city=${city}`);
      
      if (response.status === 404) {
        throw new Error("Backend not found. Azure is still deploying your API. Wait 2 minutes and try again.");
      }
      if (!response.ok) {
        throw new Error(`Server Error: ${response.status}`);
      }

      const data = await response.json();
      setReport(data);
    } catch (err) {
      alert(err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ padding: '50px', textAlign: 'center', backgroundColor: '#f0fdf4', minHeight: '100vh', fontFamily: 'sans-serif' }}>
      <h1 style={{ color: '#166534' }}>🌱 AgriCloud Smart Dashboard</h1>
      <p>Enter your city to get real-time agricultural advice</p>
      
      <div style={{ margin: '20px 0' }}>
        <input 
          style={{ padding: '10px', width: '250px', borderRadius: '5px', border: '1px solid #ccc' }}
          onChange={(e) => setCity(e.target.value)} 
          placeholder="e.g. London, Lagos, Nairobi..." 
        />
        <button 
          style={{ padding: '10px 20px', marginLeft: '10px', backgroundColor: '#22c55e', color: 'white', border: 'none', borderRadius: '5px', cursor: 'pointer' }}
          onClick={getAgriData} 
          disabled={loading}
        >
          {loading ? "Analyzing..." : "Get Farming Advice"}
        </button>
      </div>

      {report && (
        <div style={{ marginTop: '30px', border: '2px solid #22c55e', padding: '20px', borderRadius: '10px', backgroundColor: 'white', display: 'inline-block', minWidth: '300px' }}>
          <h2 style={{ color: '#166534', marginTop: 0 }}>{report.city}</h2>
          <p style={{ fontSize: '1.2rem' }}><strong>Advice:</strong> {report.advice}</p>
          <p style={{ color: '#666' }}>Temperature: {Math.round(report.temp - 273.15)}°C</p>
        </div>
      )}
    </div>
  );
}

export default App;