import { useEffect, useRef, useState } from 'react';
import { io } from 'socket.io-client';

const useSocket = (sessionId) => {
  const socketRef = useRef(null);
  const [isReady, setIsReady] = useState(false);

  useEffect(() => {
    if (!sessionId) return;

    // Crear la conexión socket con la URL y opciones
    socketRef.current = io(`http://localhost:8001/api/v1/virtual-class/sessions`, {
      transports: ['websocket'],
      // Puedes agregar reconexión automática si quieres
      reconnectionAttempts: 5,
    });

    // Evento conexión exitosa
    socketRef.current.on('connect', () => {
      console.log('✅ Socket conectado:', socketRef.current.id);
      setIsReady(true);
    });

    // Evento error en la conexión
    socketRef.current.on('connect_error', (err) => {
      console.error('❌ Error al conectar socket:', err.message);
    });

    // Cleanup: desconectar cuando se desmonta o cambia sessionId
    return () => {
      if (socketRef.current) {
        socketRef.current.disconnect();
        socketRef.current = null;
      }
      setIsReady(false);
    };
  }, [sessionId]);

  return isReady ? socketRef.current : null;
};

export default useSocket;





