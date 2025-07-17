import React from 'react';
import VideoConference from '../components/aulaVirtual/Video/VideoConference';
import ContentArea from '../components/aulaVirtual/ContentArea';
import ClassroomControls from '../components/aulaVirtual/ClassroomControls';
import ChatPanel from '../components/Chat/ChatPanel';

const MainLayout = ({
  activeTab,
  setActiveTab,
  documents,
  handleDocumentUpload,
  whiteboardRef,
  sessionId,
  chatMessages,
  handleSendMessage,
  webRTC
}) => {
  // Verificar si webRTC está definido antes de acceder a sus propiedades
  const localStream = webRTC?.localStream;
  const remoteStream = webRTC?.remoteStream;
  const isAudioMuted = webRTC?.isAudioMuted;
  const isVideoMuted = webRTC?.isVideoMuted;

  return (
    <>
      <div className="main-content">
        <VideoConference
          localStream={localStream} // Ahora seguro de que no es undefined
          remoteStream={remoteStream}
          isAudioMuted={isAudioMuted}
          isVideoMuted={isVideoMuted}
        />
        <ContentArea
          activeTab={activeTab}
          documents={documents}
          onUpload={handleDocumentUpload}
          whiteboardRef={whiteboardRef}
          sessionId={sessionId}
        />
      </div>

      <div className="sidebar">
        <ClassroomControls
          activeTab={activeTab}
          onTabChange={setActiveTab}
          onAudioToggle={webRTC?.toggleAudio}
          onVideoToggle={webRTC?.toggleVideo}
          onScreenShareToggle={webRTC?.toggleScreenShare}
          onEndCall={webRTC?.endCall}
          isAudioMuted={isAudioMuted}
          isVideoMuted={isVideoMuted}
          isScreenSharing={webRTC?.isScreenSharing}
        />
        <ChatPanel
          messages={chatMessages}
          onSendMessage={handleSendMessage}
        />
      </div>
    </>
  );
};

export default MainLayout;

