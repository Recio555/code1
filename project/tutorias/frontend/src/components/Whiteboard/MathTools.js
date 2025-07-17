import React from 'react';

const MathTools = ({ activeTool, onToolChange, onAddSymbol, onClear }) => {
  return (
    <div>
      <button onClick={() => onToolChange('pen')}>Pen</button>
      <button onClick={() => onToolChange('select')}>Select</button>
      <button onClick={() => onAddSymbol('+')}>+</button>
      <button onClick={() => onAddSymbol('-')}>-</button>
      <button onClick={() => onAddSymbol('×')}>×</button>
      <button onClick={() => onAddSymbol('÷')}>÷</button>
      <button onClick={() => onClear()}>Clear</button>
    </div>
  );
};

export default MathTools;


