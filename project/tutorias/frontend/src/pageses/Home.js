import React from 'react';

const Home = () => {
  const enterFullscreen = () => {
    const element = document.documentElement; // Puedes usar también un div específico si prefieres

    if (element.requestFullscreen) {
      element.requestFullscreen();
    } else if (element.webkitRequestFullscreen) { // Para Safari
      element.webkitRequestFullscreen();
    } else if (element.msRequestFullscreen) { // Para IE11
      element.msRequestFullscreen();
    }
  };

  return (
    <div className="p-4">
      <h1 className="text-2xl font-bold">Modo pantalla completa</h1>
      <button
        onClick={enterFullscreen}
        className="mt-4 px-4 py-2 bg-blue-600 text-white rounded hover:bg-blue-700"
      >
        Entrar en pantalla completa
      </button>
    </div>
  );
};

export default Home;
