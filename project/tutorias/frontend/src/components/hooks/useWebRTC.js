import { useState, useEffect, useCallback, useRef } from "react";

const useWebRTC = (roomId) => {
  const [localStream, setLocalStream] = useState(null);
  const [remoteStream, setRemoteStream] = useState(null);
  const [isAudioMuted, setIsAudioMuted] = useState(false);
  const [isVideoMuted, setIsVideoMuted] = useState(false);
  const [isScreenSharing, setIsScreenSharing] = useState(false);

  const peerConnectionRef = useRef(null);

  // Obtiene el stream local de cámara y micrófono
  const getLocalStream = useCallback(async () => {
    try {
      const stream = await navigator.mediaDevices.getUserMedia({
        video: true,
        audio: true,
      });
      // Inicializa estados en base al stream obtenido
      setLocalStream(stream);
      setIsAudioMuted(!stream.getAudioTracks().some((t) => t.enabled));
      setIsVideoMuted(!stream.getVideoTracks().some((t) => t.enabled));
      return stream;
    } catch (error) {
      console.error("Error accessing media devices:", error);
      return null;
    }
  }, []);

  // Inicializa RTCPeerConnection y agrega tracks del stream local
  const setupWebRTC = useCallback(
    async (stream) => {
      if (!stream) return;

      const iceServers = [
        { urls: "stun:stun.l.google.com:19302" },
        process.env.REACT_APP_TURN_SERVER && {
          urls: process.env.REACT_APP_TURN_SERVER,
          username: process.env.REACT_APP_TURN_USERNAME,
          credential: process.env.REACT_APP_TURN_CREDENTIAL,
        },
      ].filter(Boolean);

      const configuration = { iceServers };

      const pc = new RTCPeerConnection(configuration);
      peerConnectionRef.current = pc;

      // Agrega cada track al peer connection
      stream.getTracks().forEach((track) => pc.addTrack(track, stream));

      pc.ontrack = (event) => {
        // Actualiza el stream remoto con la primera pista recibida
        if (event.streams && event.streams[0]) {
          setRemoteStream(event.streams[0]);
        }
      };

      pc.onicecandidate = (event) => {
        if (event.candidate) {
          // Aquí va la lógica para enviar candidates vía signaling
          // signalingSocket.emit('candidate', event.candidate);
        }
      };

      try {
        const offer = await pc.createOffer();
        await pc.setLocalDescription(offer);
        // Aquí enviar la oferta vía signaling al otro peer
        // signalingSocket.emit('offer', offer);
      } catch (err) {
        console.error("Error creating offer:", err);
      }
    },
    []
  );

  // Cambia el estado del audio local y sincroniza el flag
  const toggleAudio = useCallback(() => {
    if (!localStream) return;
    localStream.getAudioTracks().forEach((track) => {
      track.enabled = !track.enabled;
    });
    // Solo toma el estado del primer track para el flag
    setIsAudioMuted(!localStream.getAudioTracks()[0]?.enabled);
  }, [localStream]);

  // Cambia el estado del video local y sincroniza el flag
  const toggleVideo = useCallback(() => {
    if (!localStream) return;
    localStream.getVideoTracks().forEach((track) => {
      track.enabled = !track.enabled;
    });
    setIsVideoMuted(!localStream.getVideoTracks()[0]?.enabled);
  }, [localStream]);

  // Maneja la alternancia entre compartir pantalla y cámara
  const toggleScreenShare = useCallback(async () => {
    if (isScreenSharing) {
      // Si ya está compartiendo pantalla, vuelve a cámara normal
      const stream = await getLocalStream();
      // Detiene tracks previos (screen share)
      localStream?.getTracks().forEach((track) => track.stop());

      if (peerConnectionRef.current && stream) {
        const senders = peerConnectionRef.current.getSenders();
        const videoTrack = stream.getVideoTracks()[0];
        const sender = senders.find((s) => s.track?.kind === "video");
        if (sender && videoTrack) {
          await sender.replaceTrack(videoTrack);
        }
        setLocalStream(stream);
      }
      setIsScreenSharing(false);
    } else {
      try {
        const screenStream = await navigator.mediaDevices.getDisplayMedia({
          video: true,
          audio: false,
        });

        // Detiene tracks del stream local (cámara)
        localStream?.getTracks().forEach((track) => track.stop());

        setLocalStream(screenStream);

        if (peerConnectionRef.current) {
          const senders = peerConnectionRef.current.getSenders();
          const screenTrack = screenStream.getVideoTracks()[0];
          const sender = senders.find((s) => s.track?.kind === "video");
          if (sender && screenTrack) {
            await sender.replaceTrack(screenTrack);
          }
        }

        setIsScreenSharing(true);

        // Maneja evento cuando usuario deja de compartir pantalla
        screenStream.getVideoTracks()[0].onended = async () => {
          setIsScreenSharing(false);
          const stream = await getLocalStream();
          if (peerConnectionRef.current && stream) {
            const senders = peerConnectionRef.current.getSenders();
            const videoTrack = stream.getVideoTracks()[0];
            const sender = senders.find((s) => s.track?.kind === "video");
            if (sender && videoTrack) {
              await sender.replaceTrack(videoTrack);
            }
            setLocalStream(stream);
          }
        };
      } catch (error) {
        console.error("Error sharing screen:", error);
      }
    }
  }, [isScreenSharing, getLocalStream, localStream]);

  // Finaliza la llamada limpiando recursos
  const endCall = useCallback(() => {
    if (peerConnectionRef.current) {
      peerConnectionRef.current.close();
      peerConnectionRef.current = null;
    }
    localStream?.getTracks().forEach((track) => track.stop());
    setLocalStream(null);
    setRemoteStream(null);
    setIsAudioMuted(false);
    setIsVideoMuted(false);
    setIsScreenSharing(false);
  }, [localStream]);

  useEffect(() => {
    (async () => {
      const stream = await getLocalStream();
      await setupWebRTC(stream);
    })();

    return () => {
      endCall();
    };
  }, [getLocalStream, setupWebRTC, endCall]);

  return {
    localStream,
    remoteStream,
    isAudioMuted,
    isVideoMuted,
    isScreenSharing,
    toggleAudio,
    toggleVideo,
    toggleScreenShare,
    endCall,
  };
};

export default useWebRTC;



