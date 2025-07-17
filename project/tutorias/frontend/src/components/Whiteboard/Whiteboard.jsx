import React, { useEffect, useRef, useState } from 'react';
import * as fabric from 'fabric';
import MathTools from './MathTools';
import { useSocket } from '../../hooks/useSocket';

const Whiteboard = React.forwardRef(({ sessionId }, ref) => {
  const canvasRef = useRef(null);
  const [canvas, setCanvas] = useState(null);
  const [activeTool, setActiveTool] = useState('pen');
  const socket = useSocket();  // CORRECCIÓN: no destructures, el contexto devuelve el socket directamente

  // Initialize canvas and listen socket events
  useEffect(() => {
   // if (!canvasRef.current || !socket) return; // Protege si socket no está listo

    const canvasInstance = new fabric.Canvas(canvasRef.current, {
      isDrawingMode: true,
      width: 800,
      height: 600,
      backgroundColor: '#ffffff'
    });
    setCanvas(canvasInstance);

    const handleWhiteboardUpdate = (data) => {
      if (data.sessionId === sessionId) {
        canvasInstance.loadFromJSON(data.state, () => {
          canvasInstance.renderAll();
        });
      }
    };

    socket.on('whiteboard-update', handleWhiteboardUpdate);

    return () => {
      canvasInstance.dispose();
      //socket.off('whiteboard-update', handleWhiteboardUpdate);
    };
  }, [sessionId, socket]);

  // Emit changes to the socket
  useEffect(() => {
    if (!canvas || !socket) return; // Protege si no están listos

    const handleChange = () => {
      const state = canvas.toJSON();
      socket.emit('whiteboard-update', {
        sessionId,
        state
      });
    };

    canvas.on('object:modified', handleChange);
    canvas.on('object:added', handleChange);
    canvas.on('object:removed', handleChange);

    return () => {
      canvas.off('object:modified', handleChange);
      canvas.off('object:added', handleChange);
      canvas.off('object:removed', handleChange);
    };
  }, [canvas, sessionId, socket]);

  // Tool change handler
  const changeTool = (tool) => {
    setActiveTool(tool);
    if (canvas) {
      canvas.isDrawingMode = tool === 'pen';
      canvas.selection = tool === 'select';
    }
  };

  // Add math symbol to canvas
  const addMathSymbol = (symbol) => {
    if (canvas) {
      const text = new fabric.Text(symbol, {
        left: 100,
        top: 100,
        fontSize: 30,
        fontFamily: 'Arial'
      });
      canvas.add(text);
      canvas.renderAll();
    }
  };

  // Clear the canvas
  const clearCanvas = () => {
    if (canvas) {
      canvas.clear();
      canvas.backgroundColor = '#ffffff';
      canvas.renderAll();
    }
  };

  React.useImperativeHandle(ref, () => ({
    saveAsImage: () => {
      if (canvas) {
        return canvas.toDataURL('png');
      }
      return null;
    },
    clearCanvas
  }));

  return (
    <div className="whiteboard-container">
      <div className="whiteboard-toolbar">
        <MathTools 
          activeTool={activeTool}
          onToolChange={changeTool}
          onAddSymbol={addMathSymbol}
          onClear={clearCanvas}
        />
      </div>
      <canvas ref={canvasRef} />
    </div>
  );
});

export default Whiteboard;

