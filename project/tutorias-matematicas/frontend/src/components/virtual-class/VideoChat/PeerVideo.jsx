import React, { useEffect, useRef, useState } from 'react';
import { useWebRTC } from '../../../hooks/useWebRTC';
import VideoControls from './VideoControls';
import RecordingControls from '../SessionRecording/RecordingControls';

const PeerVideo = ({ roomId, userId, localStream, remoteStream }) => {
  const localVideoRef = useRef(null);
  const remoteVideoRef = useRef(null);
  const [recorder, setRecorder] = useState(null);
  const [isRecording, setIsRecording] = useState(false);
  const { 
    muteAudio, 
    muteVideo, 
    shareScreen,
    isAudioMuted,
    isVideoMuted,
    isScreenSharing
  } = useWebRTC(roomId, userId);

  useEffect(() => {
    if (localVideoRef.current && localStream) {
      localVideoRef.current.srcObject = localStream;
    }
    
    if (remoteVideoRef.current && remoteStream) {
      remoteVideoRef.current.srcObject = remoteStream;
    }
  }, [localStream, remoteStream]);

  const startRecording = async () => {
    try {
      const stream = localVideoRef.current.captureStream();
      const mediaRecorder = new MediaRecorder(stream, {
        mimeType: 'video/webm;codecs=vp9'
      });
      
      const chunks = [];
      mediaRecorder.ondataavailable = (e) => chunks.push(e.data);
      
      mediaRecorder.onstop = async () => {
        const blob = new Blob(chunks, { type: 'video/webm' });
        const arrayBuffer = await blob.arrayBuffer();
        // Enviar al backend para guardar
      };
      
      mediaRecorder.start(1000); // Capturar datos cada segundo
      setRecorder(mediaRecorder);
      setIsRecording(true);
    } catch (error) {
      console.error('Error starting recording:', error);
    }
  };

  const stopRecording = () => {
    if (recorder) {
      recorder.stop();
      setIsRecording(false);
      setRecorder(null);
    }
  };

  return (
    <div className="video-chat-container">
      <div className="remote-video-wrapper">
        <video 
          ref={remoteVideoRef} 
          autoPlay 
          playsInline 
          className="remote-video"
        />
        <RecordingControls
          isRecording={isRecording}
          onStart={startRecording}
          onStop={stopRecording}
        />
      </div>
      
      <div className="local-video-wrapper">
        <video
          ref={localVideoRef}
          autoPlay
          playsInline
          muted
          className="local-video"
        />
        <VideoControls
          isAudioMuted={isAudioMuted}
          isVideoMuted={isVideoMuted}
          isScreenSharing={isScreenSharing}
          onToggleAudio={muteAudio}
          onToggleVideo={muteVideo}
          onToggleScreen={shareScreen}
        />
      </div>
    </div>
  );
};

export default PeerVideo;