import React, { useState, useEffect, useRef } from 'react';
import { useParams } from 'react-router-dom';
import { useAuth } from '../contexts/AuthContext';
import Whiteboard from '../components/VirtualClass/Whiteboard';
import VideoChat from '../components/VirtualClass/VideoChat';
import ChatPanel from '../components/VirtualClass/ChatPanel';
import ClassControls from '../components/VirtualClass/ClassControls';

const VirtualClassPage = () => {
  const { roomId } = useParams();
  const { user } = useAuth();
  const [messages, setMessages] = useState([]);
  const [whiteboardData, setWhiteboardData] = useState(null);
  const [isConnected, setIsConnected] = useState(false);
  const ws = useRef(null);

  useEffect(() => {
    ws.current = new WebSocket(`ws://localhost:8000/ws/class/${roomId}/${user.id}`);
    
    ws.current.onopen = () => {
      setIsConnected(true);
      sendMessage({ type: 'notification', content: 'joined the class' });
    };

    ws.current.onmessage = (e) => {
      const message = JSON.parse(e.data);
      
      switch(message.type) {
        case 'chat':
          setMessages(prev => [...prev, message]);
          break;
        case 'whiteboard':
          setWhiteboardData(message.data);
          break;
        default:
          break;
      }
    };

    return () => {
      ws.current.close();
    };
  }, [roomId, user.id]);

  const sendMessage = (content) => {
    if (isConnected) {
      ws.current.send(JSON.stringify({
        type: 'chat',
        content,
        sender: user.full_name,
        userId: user.id
      }));
    }
  };

  const sendWhiteboardUpdate = (data) => {
    if (isConnected) {
      ws.current.send(JSON.stringify({
        type: 'whiteboard',
        data,
        userId: user.id
      }));
    }
  };

  return (
    <div className="virtual-class-container">
      <div className="main-content">
        <VideoChat roomId={roomId} userId={user.id} />
        <Whiteboard 
          initialData={whiteboardData} 
          onUpdate={sendWhiteboardUpdate} 
        />
      </div>
      
      <div className="sidebar">
        <ChatPanel 
          messages={messages} 
          onSendMessage={sendMessage} 
          currentUser={user}
        />
        <ClassControls roomId={roomId} />
      </div>
    </div>
  );
};

export default VirtualClassPage;