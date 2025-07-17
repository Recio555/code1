import React, { useState, useEffect, useRef } from 'react';
import { useSocket } from '../../contexts/SocketContext';

const ChatPanel = ({ messages: propMessages = [], onSendMessage }) => {
  const [message, setMessage] = useState('');
  const [messages, setMessages] = useState(propMessages);
  const messagesEndRef = useRef(null);
  const socket = useSocket();

  console.log(socket);

  useEffect(() => {
    if (!socket || typeof socket.on !== 'function') {
      console.error('en ChatPanel, Socket no está correctamente inicializado.');
      return;
    }

    const handleNewMessage = (msg) => {
      setMessages((prev) => [...prev, msg]);
    };

    socket.on('new-message', handleNewMessage);

    return () => {
      socket.off('new-message', handleNewMessage);
    };
  }, [socket]);

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!socket || typeof socket.emit !== 'function') {
      console.error('⚠️ Socket no está disponible para emitir mensajes.');
      return;
    }

    if (message.trim()) {
      const newMessage = {
        id: Date.now(),
        sender: 'Yo',
        content: message,
        timestamp: new Date().toLocaleTimeString(),
      };
      onSendMessage(message);
      socket.emit('send-message', newMessage);
      setMessages((prev) => [...prev, newMessage]);
      setMessage('');
    }
  };

  return (
    <div className="chat-panel">
      <div className="chat-messages">
        {messages.map((msg) => (
          <div key={msg.id} className={`message ${msg.sender === 'Yo' ? 'sent' : 'received'}`}>
            <div className="message-sender">{msg.sender}</div>
            <div className="message-content">{msg.content}</div>
            <div className="message-time">{msg.timestamp}</div>
          </div>
        ))}
        <div ref={messagesEndRef} />
      </div>

      <form onSubmit={handleSubmit} className="chat-input">
        <input
          type="text"
          value={message}
          onChange={(e) => setMessage(e.target.value)}
          placeholder="Escribe un mensaje..."
        />
        <button type="submit">Enviar</button>
      </form>
    </div>
  );
};

export default ChatPanel;




