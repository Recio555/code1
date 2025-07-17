import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';

function SessionPage() {
  const { sessionId } = useParams();
  const [sessionData, setSessionData] = useState(null);
  const [error, setError] = useState("");

  useEffect(() => {
    fetch(`http://localhost:8000/sessions/${sessionId}`)
      .then(res => {
        if (!res.ok) throw new Error("Sesión no encontrada");
        return res.json();
      })
      .then(data => setSessionData(data))
      .catch(err => setError(err.message));
  }, [sessionId]);

  if (error) return <p>Error: {error}</p>;
  if (!sessionData) return <p>Cargando...</p>;

  return (
    <div>
      <h2>Sessión: {sessionId}</h2>
      <p>Título: {sessionData.title}</p>
      <p>Tutor: {sessionData.tutor}</p>
    </div>
  );
}

export default SessionPage;
