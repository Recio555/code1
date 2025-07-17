// components/VirtualClassroom/useClassroomState.js
import { useState, useRef, useEffect } from 'react';
import useWebRTC from '../hooks/useWebRTC';

const useClassroomState = (sessionId) => {
  const [activeTab, setActiveTab] = useState('whiteboard');
  const [documents, setDocuments] = useState([]);
  const [chatMessages, setChatMessages] = useState([]);
  const [showFullscreenPrompt, setShowFullscreenPrompt] = useState(true);
  const whiteboardRef = useRef(null);

  const webRTC = useWebRTC(sessionId);

  useEffect(() => {
    const handleFirstClick = () => {
      const element = document.documentElement;
      if (element.requestFullscreen) {
        element.requestFullscreen().catch(err => {
          console.warn('No se pudo activar pantalla completa:', err);
        });
      }
      setShowFullscreenPrompt(false);
      window.removeEventListener('click', handleFirstClick);
    };

    window.addEventListener('click', handleFirstClick);
    return () => window.removeEventListener('click', handleFirstClick);
  }, []);

  const handleSendMessage = (message) => {
    const newMessage = {
      id: Date.now(),
      sender: 'Yo',
      content: message,
      timestamp: new Date().toLocaleTimeString()
    };
    setChatMessages(prev => [...prev, newMessage]);
  };

  const handleDocumentUpload = (file) => {
    const newDocument = {
      id: Date.now(),
      name: file.name,
      type: file.type,
      size: file.size,
      uploadedBy: 'Yo',
      url: URL.createObjectURL(file)
    };
    setDocuments(prev => [...prev, newDocument]);
  };

  return {
    activeTab,
    setActiveTab,
    documents,
    setDocuments,
    chatMessages,
    setChatMessages,
    whiteboardRef,
    showFullscreenPrompt,
    webRTC,
    handleSendMessage,
    handleDocumentUpload
  };
};

export default useClassroomState;
