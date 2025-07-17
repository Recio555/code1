import React, { useEffect, useRef, useState } from "react";
import io from "socket.io-client";

const socket = io("http://localhost:8080");

const App = () => {
  const localVideoRef = useRef(null);
  const remoteVideoRef = useRef(null);
  const pcRef = useRef(null); // Usamos un ref para mantener la misma instancia

  useEffect(() => {
    const pc = new RTCPeerConnection({
      iceServers: [{ urls: "stun:stun.l.google.com:19302" }],
    });

    pcRef.current = pc;

    navigator.mediaDevices.getUserMedia({ video: true, audio: true })
      .then(stream => {
        if (localVideoRef.current) {
          localVideoRef.current.srcObject = stream;
        }

        stream.getTracks().forEach(track => {
          if (pc.signalingState !== "closed") {
            pc.addTrack(track, stream);
          }
        });
      })
      .catch(console.error);

    pc.ontrack = event => {
      if (remoteVideoRef.current) {
        remoteVideoRef.current.srcObject = event.streams[0];
      }
    };

    socket.on("offer", async offer => {
      if (pc.signalingState === "closed") return;
      await pc.setRemoteDescription(new RTCSessionDescription(offer));
      const answer = await pc.createAnswer();
      await pc.setLocalDescription(answer);
      socket.emit("answer", answer);
    });

    socket.on("answer", async answer => {
      if (pc.signalingState === "closed") return;
      await pc.setRemoteDescription(new RTCSessionDescription(answer));
    });

    socket.on("ice-candidate", async candidate => {
      if (pc.signalingState === "closed") return;
      await pc.addIceCandidate(new RTCIceCandidate(candidate));
    });

    pc.onicecandidate = event => {
      if (event.candidate) {
        socket.emit("ice-candidate", event.candidate);
      }
    };

    return () => {
      pc.getSenders().forEach(sender => pc.removeTrack(sender));
      pc.close();
    };
  }, []);

  const handleStartCall = async () => {
    const pc = pcRef.current;
    if (!pc || pc.signalingState === "closed") return;
    const offer = await pc.createOffer();
    await pc.setLocalDescription(offer);
    socket.emit("offer", offer);
  };

  return (
    <div>
      <h1>Videollamada WebRTC</h1>
      <video ref={localVideoRef} autoPlay playsInline muted style={{ width: 300 }} />
      <video ref={remoteVideoRef} autoPlay playsInline style={{ width: 300 }} />
      <button onClick={handleStartCall}>Iniciar llamada</button>
    </div>
  );
};

export default App;