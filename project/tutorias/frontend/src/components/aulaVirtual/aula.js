import React from 'react';
import { useParams } from 'react-router-dom';
import { SocketProvider } from '../../contexts/SocketContext';
import useClassroomState from './useClassroomState';
import FullscreenPrompt from './FullscreenPrompt';
import MainLayout from '../../layouts/MainLayout';

import './VirtualClassroom.css';

const VirtualClassroom = () => {
  const { sessionId } = useParams();

  const {
    activeTab,
    setActiveTab,
    documents,
    chatMessages,
    whiteboardRef,
    showFullscreenPrompt,
    handleSendMessage,
    handleDocumentUpload,
    webRTC
  } = useClassroomState(sessionId);

  // Si sessionId no está presente, mostrar mensaje de carga
  if (!sessionId) return <div>Cargando sesión...</div>;

  return (
    <SocketProvider sessionId={sessionId}>
      <div className="virtual-classroom">
        {showFullscreenPrompt && <FullscreenPrompt />}

        <MainLayout
          activeTab={activeTab}
          setActiveTab={setActiveTab}
          documents={documents}
          handleDocumentUpload={handleDocumentUpload}
          whiteboardRef={whiteboardRef}
          sessionId={sessionId}
          chatMessages={chatMessages}
          handleSendMessage={handleSendMessage}
          webRTC={webRTC}
        />
      </div>
    </SocketProvider>
  );
};

export default VirtualClassroom;






