import React, { useEffect, useRef, useState } from 'react';
import { fabric } from 'fabric';
import MathSymbolsPanel from './MathToolsPanel';
import { useWhiteboard } from '../../../hooks/useWhiteboard';
import { recognizeMathSymbol } from '../../../utils/mathRecognizer';

const WhiteboardCanvas = ({ roomId, tabId, onSave }) => {
  const canvasRef = useRef(null);
  const [canvas, setCanvas] = useState(null);
  const { boardState, sendUpdate } = useWhiteboard(roomId, tabId);
  const [recognitionActive, setRecognitionActive] = useState(false);

  useEffect(() => {
    const initCanvas = new fabric.Canvas(canvasRef.current, {
      isDrawingMode: true,
      width: 1000,
      height: 700,
      backgroundColor: '#ffffff'
    });

    // Configurar herramientas de dibujo
    initCanvas.freeDrawingBrush.width = 2;
    initCanvas.freeDrawingBrush.color = '#000000';

    // Cargar estado inicial
    if (boardState) {
      initCanvas.loadFromJSON(boardState, () => {
        initCanvas.renderAll();
      });
    }

    // Eventos para sincronización
    initCanvas.on('object:modified', handleCanvasChange);
    initCanvas.on('object:added', handleCanvasChange);
    initCanvas.on('object:removed', handleCanvasChange);
    initCanvas.on('path:created', handleCanvasChange);

    // Configurar reconocimiento de gestos
    if (recognitionActive) {
      initCanvas.on('mouse:up', handleDrawingEnd);
    }

    setCanvas(initCanvas);

    return () => {
      initCanvas.dispose();
    };
  }, [roomId, tabId, recognitionActive]);

  const handleCanvasChange = () => {
    if (canvas) {
      const state = canvas.toJSON();
      sendUpdate(state);
    }
  };

  const handleDrawingEnd = async () => {
    if (!canvas) return;
    
    const activeObject = canvas.getActiveObject();
    if (activeObject && activeObject.type === 'path') {
      try {
        const symbol = await recognizeMathSymbol(activeObject);
        if (symbol) {
          canvas.remove(activeObject);
          const text = new fabric.Text(symbol, {
            left: activeObject.left,
            top: activeObject.top,
            fontSize: 30,
            fontFamily: 'Arial'
          });
          canvas.add(text);
          canvas.renderAll();
        }
      } catch (error) {
        console.error('Recognition error:', error);
      }
    }
  };

  const addMathObject = (symbol) => {
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

  return (
    <div className="whiteboard-container">
      <div className="whiteboard-toolbar">
        <MathSymbolsPanel 
          onSelectSymbol={addMathObject} 
          recognitionActive={recognitionActive}
          toggleRecognition={() => setRecognitionActive(!recognitionActive)}
        />
      </div>
      <canvas ref={canvasRef} />
    </div>
  );
};

export default WhiteboardCanvas;