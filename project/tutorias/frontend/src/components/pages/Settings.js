import { useNavigate } from 'react-router-dom';
import axios from 'axios';
import { useState } from 'react';

const Settings = () => {
  const navigate = useNavigate();
  const [sessionId, setSessionId] = useState('');
  const [loading, setLoading] = useState(false);

  const handleCreateSession = async () => {
    setLoading(true);
    try {
      const response = await axios.post('http://localhost:8001/api/v1/virtual-class/create-session');
      const newSessionId = response.data.session_id;
      setSessionId(newSessionId);
      //Navegar al aula
      console.log(`/aula/${newSessionId}`);
      navigate(`/aula/${newSessionId}`);
    } catch (error) {
      console.error("Error al crear sesión:", error);
      alert("No se pudo crear la sesión.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ padding: '20px' }}>
      <h2>Bienvenido al Aula Virtual</h2>
      {sessionId && <p>Sesión creada: {sessionId}</p>}
      <button onClick={handleCreateSession} disabled={loading}>
        {loading ? 'Creando sesión...' : 'Crear nueva sesión'}
      </button>
    </div>
  );
};

export default Settings;


