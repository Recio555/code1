import React, { createContext, useContext, useEffect, useState } from 'react';
import io from 'socket.io-client';

// Crear el contexto
const SocketContext = createContext(null);

// Proveedor del contexto
export const SocketProvider = ({ children, sessionId }) => {
  const [socket, setSocket] = useState(null);

  useEffect(() => {
    if (!sessionId) {
      console.warn('SocketProvider: sessionId no definido. No se establecerá conexión.');
      return;
    }

 

  const newSocket = io("http://localhost:8001", {
    path: `/api/v1/virtual-class/sessions/${sessionId}`,
    transports: ['websocket'],
  });

    //const newSocket = io(process.env.REACT_APP_SOCKET_SERVER, {
     // transports: ['websocket'], // Fuerza WebSocket si se desea
    //  query: { sessionId }
   // });


    setSocket(newSocket);

    console.log('Socket conectado con sessionId:', sessionId);

    return () => {
      newSocket.disconnect();
      console.log('Socket desconectado');
    };
  }, [sessionId]);

  return (
    <SocketContext.Provider value={socket}>
      {children}
    </SocketContext.Provider>
  );
};

// Hook personalizado para usar el socket
export const useSocket = () => {
  const socket = useContext(SocketContext);

  if (!socket) {
    console.warn('useSocket: socket no disponible en el contexto');
  }

  return socket;
};
