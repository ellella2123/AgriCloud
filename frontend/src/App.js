import React, { useState } from 'react';

function App() {
  const [city, setCity] = useState('');
  const [report, setReport] = useState(null);
  const [loading, setLoading] = useState(false);

  const getAgriData = async () => {
    setLoading(true);
    try {
      const response = await fetch(`/api/message?city=${city}`);
      if (!response.ok) throw new Error('API not responding');
      const data = await response.json();
      setReport(data);
    } catch (err) {
      alert("Error: " + err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ padding: '50px', textAlign: 'center' }}>
      <h1>🌱 AgriCloud Portal</h1>
      <input onChange={(e) => setCity(e.target.value)} placeholder="City name..." />
      <button onClick={getAgriData} disabled={loading}>
        {loading ? "Searching..." : "Get Advice"}
      </button>

      {report && (
        <div style={{ marginTop: '20px', border: '1px solid green', padding: '10px' }}>
          <h2>{report.city}</h2>
          <p>Advice: {report.advice}</p>
        </div>
      )}
    </div>
  );
}

export default App;