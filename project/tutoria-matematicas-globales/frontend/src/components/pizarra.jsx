import { useState, useRef, useEffect } from 'react';

export default function Whiteboard() {
  const [isDrawing, setIsDrawing] = useState(false);
  const [color, setColor] = useState('#000000');
  const [brushSize, setBrushSize] = useState(5);
  const [drawingHistory, setDrawingHistory] = useState([]);
  const [historyIndex, setHistoryIndex] = useState(-1);
  const canvasRef = useRef(null);
  const ctxRef = useRef(null);

  useEffect(() => {
    const canvas = canvasRef.current;
    canvas.width = window.innerWidth * 0.8;
    canvas.height = window.innerHeight * 0.6;
    
    const ctx = canvas.getContext('2d');
    ctx.lineCap = 'round';
    ctx.lineJoin = 'round';
    ctx.strokeStyle = color;
    ctx.lineWidth = brushSize;
    ctxRef.current = ctx;
    
    // Initialize with blank canvas
    saveToHistory(ctx.getImageData(0, 0, canvas.width, canvas.height));
  }, []);

  useEffect(() => {
    if (ctxRef.current) {
      ctxRef.current.strokeStyle = color;
      ctxRef.current.lineWidth = brushSize;
    }
  }, [color, brushSize]);

  const startDrawing = (e) => {
    const { offsetX, offsetY } = getCoordinates(e);
    ctxRef.current.beginPath();
    ctxRef.current.moveTo(offsetX, offsetY);
    setIsDrawing(true);
  };

  const draw = (e) => {
    if (!isDrawing) return;
    const { offsetX, offsetY } = getCoordinates(e);
    ctxRef.current.lineTo(offsetX, offsetY);
    ctxRef.current.stroke();
  };

  const stopDrawing = () => {
    if (isDrawing) {
      ctxRef.current.closePath();
      setIsDrawing(false);
      
      // Save to history
      const canvas = canvasRef.current;
      saveToHistory(ctxRef.current.getImageData(0, 0, canvas.width, canvas.height));
    }
  };

  const getCoordinates = (e) => {
    const canvas = canvasRef.current;
    const rect = canvas.getBoundingClientRect();
    
    // Handle both mouse and touch events
    if (e.touches && e.touches[0]) {
      return {
        offsetX: e.touches[0].clientX - rect.left,
        offsetY: e.touches[0].clientY - rect.top
      };
    }
    
    return {
      offsetX: e.clientX - rect.left,
      offsetY: e.clientY - rect.top
    };
  };

  const clearCanvas = () => {
    const canvas = canvasRef.current;
    ctxRef.current.clearRect(0, 0, canvas.width, canvas.height);
    
    // Save cleared state to history
    saveToHistory(ctxRef.current.getImageData(0, 0, canvas.width, canvas.height));
  };

  const saveToHistory = (imageData) => {
    // If we're not at the end of the history, remove everything after current point
    if (historyIndex < drawingHistory.length - 1) {
      setDrawingHistory(drawingHistory.slice(0, historyIndex + 1));
    }
    
    setDrawingHistory([...drawingHistory.slice(0, historyIndex + 1), imageData]);
    setHistoryIndex(historyIndex + 1);
  };

  const undo = () => {
    if (historyIndex > 0) {
      setHistoryIndex(historyIndex - 1);
      ctxRef.current.putImageData(drawingHistory[historyIndex - 1], 0, 0);
    }
  };

  const redo = () => {
    if (historyIndex < drawingHistory.length - 1) {
      setHistoryIndex(historyIndex + 1);
      ctxRef.current.putImageData(drawingHistory[historyIndex], 0, 0);
    }
  };

  return (
    <div className="flex flex-col items-center justify-center w-full p-4 bg-gray-100">
      <h1 className="text-2xl font-bold mb-4">Pizarra Digital</h1>
      
      <div className="flex gap-4 mb-4">
        <div className="flex items-center">
          <label htmlFor="color-picker" className="mr-2 text-sm">Color:</label>
          <input
            id="color-picker"
            type="color"
            value={color}
            onChange={(e) => setColor(e.target.value)}
            className="w-8 h-8 border border-gray-300 rounded"
          />
        </div>
        
        <div className="flex items-center">
          <label htmlFor="brush-size" className="mr-2 text-sm">Tamaño:</label>
          <input
            id="brush-size"
            type="range"
            min="1"
            max="20"
            value={brushSize}
            onChange={(e) => setBrushSize(parseInt(e.target.value))}
            className="w-32"
          />
          <span className="ml-2 text-sm">{brushSize}px</span>
        </div>
      </div>
      
      <div className="flex gap-2 mb-4">
        <button
          onClick={clearCanvas}
          className="px-3 py-1 bg-red-500 text-white rounded hover:bg-red-600"
        >
          Borrar Todo
        </button>
        <button
          onClick={undo}
          disabled={historyIndex <= 0}
          className={`px-3 py-1 bg-blue-500 text-white rounded hover:bg-blue-600 ${
            historyIndex <= 0 ? 'opacity-50 cursor-not-allowed' : ''
          }`}
        >
          Deshacer
        </button>
        <button
          onClick={redo}
          disabled={historyIndex >= drawingHistory.length - 1}
          className={`px-3 py-1 bg-blue-500 text-white rounded hover:bg-blue-600 ${
            historyIndex >= drawingHistory.length - 1 ? 'opacity-50 cursor-not-allowed' : ''
          }`}
        >
          Rehacer
        </button>
      </div>
      
      <canvas
        ref={canvasRef}
        onMouseDown={startDrawing}
        onMouseMove={draw}
        onMouseUp={stopDrawing}
        onMouseLeave={stopDrawing}
        onTouchStart={startDrawing}
        onTouchMove={draw}
        onTouchEnd={stopDrawing}
        className="bg-white border border-gray-300 rounded shadow-md touch-none"
      />
      
      <p className="mt-4 text-sm text-gray-600">
        Dibuja en el lienzo utilizando el mouse o pantalla táctil.
      </p>
    </div>
  );
}