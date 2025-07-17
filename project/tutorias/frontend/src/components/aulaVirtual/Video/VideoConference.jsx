import React, { useEffect, useRef } from 'react';
// import './VideoConference.css'; // Asegúrate de tener los estilos o créalos

const VideoConference = ({ localStream, remoteStream, isAudioMuted, isVideoMuted }) => {
  const localVideoRef = useRef(null);
  const remoteVideoRef = useRef(null);

  useEffect(() => {
    if (localVideoRef.current && localStream) {
      localVideoRef.current.srcObject = localStream;
    }
  }, [localStream]);

  useEffect(() => {
    if (remoteVideoRef.current && remoteStream) {
      remoteVideoRef.current.srcObject = remoteStream;
    }
  }, [remoteStream]);

  return (
    <div className="video-conference">
      {/* Remote video */}
      <div className="remote-video-container">
        <video
          key="remote-video"
          ref={remoteVideoRef}
          autoPlay
          playsInline
          className="remote-video"
        />
        <div className="video-status">
          {isAudioMuted && <span className="muted-indicator">🔇</span>}
          {isVideoMuted && <span className="muted-indicator">📷❌</span>}
        </div>
      </div>

      {/* Local video */}
      <div className="local-video-container">
        <video
          key="local-video"
          ref={localVideoRef}
          autoPlay
          playsInline
          muted // El video local debe estar silenciado para evitar eco
          className="local-video"
          style={{
            opacity: isVideoMuted ? 0.5 : 1,
            border: isAudioMuted ? '2px solid red' : 'none'
          }}
        />
      </div>
    </div>
  );
};

export default VideoConference;
