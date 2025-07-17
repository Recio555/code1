import React, { useEffect, useState } from 'react';
import { useSocket } from '../../contexts/SocketContext';

const Profile = () => {
  const socket = useSocket();
  const [connected, setConnected] = useState(false);
  const [messages, setMessages] = useState([]);

  useEffect(() => {
    if (!socket) {
      console.warn('❗ Socket no disponible en el contexto');
      return;
    }

    const handleConnect = () => {
      console.log('✅ Socket conectado:', socket.id);
      setConnected(true);
    };

    const handleMessage = (data) => {
      console.log('📩 Mensaje del servidor:', data);
      setMessages((prev) => [...prev, data]);
    };

    const handleError = (err) => {
      console.error('❌ Error de conexión:', err);
    };

    socket.on('connect', handleConnect);
    socket.on('server-message', handleMessage);
    socket.on('connect_error', handleError);

    return () => {
      socket.off('connect', handleConnect);
      socket.off('server-message', handleMessage);
      socket.off('connect_error', handleError);
    };
  }, [socket]);

  const sendMessage = () => {
    if (!socket) {
      console.warn('⚠️ No se puede enviar mensaje: el socket no está disponible.');
      return;
    }

    const message = `Mensaje de prueba desde el cliente (${new Date().toLocaleTimeString()})`;
    socket.emit('client-message', message);
    console.log('📤 Enviado al servidor:', message);
  };

  return (
    <div style={{ padding: '1rem', border: '1px solid gray' }}>
      <h2>Test de Socket.IO</h2>
      <p>Estado: {connected ? '🟢 Conectado' : '🔴 No conectado'}</p>
      <button onClick={sendMessage} disabled={!connected}>
        Enviar mensaje de prueba
      </button>
      <div style={{ marginTop: '1rem' }}>
        <h4>Mensajes recibidos del servidor:</h4>
        <ul>
          {messages.map((msg, i) => (
            <li key={i}>{msg}</li>
          ))}
        </ul>
      </div>
    </div>
  );
};

export default Profile;

