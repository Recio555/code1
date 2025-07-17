import React, { createContext, useContext, useEffect, useRef, useState } from 'react';
import { io } from 'socket.io-client';

const SocketContext = createContext(null);

export const SocketProvider = ({ children }) => {
  const socketRef = useRef(null);
  const [isReady, setIsReady] = useState(false);

  useEffect(() => {
    const socketUrl = import.meta.env.VITE_SOCKET_URL || 'http://localhost:8001/api/v1/virtual-class/sessions/abc123';
    socketRef.current = io(socketUrl, {
      transports: ['websocket'],
      reconnectionAttempts: 5,
    });

    socketRef.current.on('connect', () => {
      console.log('✅ Socket conectado:', socketRef.current.id);
      setIsReady(true);
    });

    socketRef.current.on('connect_error', (err) => {
      console.error('❌ Error de conexión del socket: EN useSocket', err.message);
    });

    return () => {
      socketRef.current?.disconnect();
      console.log('🔌 Socket desconectado');
    };
  }, []);

  return (
    <SocketContext.Provider value={isReady ? socketRef.current : null}>
      {children}
    </SocketContext.Provider>
  );
};

export const useSocket = () => useContext(SocketContext);







