import { useEffect, useState, useRef } from 'react';
import { io } from 'socket.io-client';

export function useSocket(serverUrl) {
  const [connected, setConnected] = useState(false);
  const socketRef = useRef(null);

  useEffect(() => {
    // Crear la conexión al servidor socket.io
    socketRef.current = io(serverUrl);

    socketRef.current.on('connect', () => {
      setConnected(true);
      console.log('Socket connected:', socketRef.current.id);
    });

    socketRef.current.on('disconnect', () => {
      setConnected(false);
      console.log('Socket disconnected');
    });

    // Limpiar la conexión al desmontar
    return () => {
      socketRef.current.disconnect();
    };
  }, [serverUrl]);

  // Función para enviar eventos
  const emit = (event, data) => {
    if (socketRef.current) {
      socketRef.current.emit(event, data);
    }
  };

  // Devuelve el socket, estado y la función emit
  return { socket: socketRef.current, connected, emit };
}
