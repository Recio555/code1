import React from 'react';
import { FaChalkboard, FaFileUpload, FaVideo, FaVideoSlash, FaMicrophone, FaMicrophoneSlash, FaDesktop, FaPhoneSlash } from 'react-icons/fa';
import { IoMdChatboxes } from 'react-icons/io';
//import './ClassroomControls.css';

const ClassroomControls = ({
  activeTab,
  onTabChange,
  onAudioToggle,
  onVideoToggle,
  onScreenShareToggle,
  onEndCall,
  isAudioMuted,
  isVideoMuted,
  isScreenSharing
}) => {
  return (
    <div className="classroom-controls">
      <div className="tabs-controls">
        <button
          className={`tab-btn ${activeTab === 'whiteboard' ? 'active' : ''}`}
          onClick={() => onTabChange('whiteboard')}
          title="Pizarra"
        >
          <FaChalkboard />
        </button>
        
        <button
          className={`tab-btn ${activeTab === 'documents' ? 'active' : ''}`}
          onClick={() => onTabChange('documents')}
          title="Documentos"
        >
          <FaFileUpload />
        </button>
        
        <button
          className={`tab-btn ${activeTab === 'chat' ? 'active' : ''}`}
          onClick={() => onTabChange('chat')}
          title="Chat"
        >
          <IoMdChatboxes />
        </button>
      </div>

      <div className="media-controls">
        <button
          className={`control-btn ${isAudioMuted ? 'muted' : ''}`}
          onClick={onAudioToggle}
          title={isAudioMuted ? 'Activar micrófono' : 'Silenciar micrófono'}
        >
          {isAudioMuted ? <FaMicrophoneSlash /> : <FaMicrophone />}
        </button>
        
        <button
          className={`control-btn ${isVideoMuted ? 'muted' : ''}`}
          onClick={onVideoToggle}
          title={isVideoMuted ? 'Activar cámara' : 'Desactivar cámara'}
        >
          {isVideoMuted ? <FaVideoSlash /> : <FaVideo />}
        </button>
        
        <button
          className={`control-btn ${isScreenSharing ? 'active' : ''}`}
          onClick={onScreenShareToggle}
          title={isScreenSharing ? 'Dejar de compartir pantalla' : 'Compartir pantalla'}
        >
          <FaDesktop />
        </button>
      </div>

      <div className="call-controls">
        <button
          className="end-call-btn"
          onClick={onEndCall}
          title="Finalizar llamada"
        >
          <FaPhoneSlash />
        </button>
      </div>
    </div>
  );
};

export default ClassroomControls;