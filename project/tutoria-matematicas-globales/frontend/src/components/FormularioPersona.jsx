import React, { useState } from 'react';
import axios from 'axios';

function FormularioPersona({ onPersonaAgregada }) {
  const [nombre, setNombre] = useState('');
  const [apellido, setApellido] = useState('');

  const handleAddPersona = () => {
    if (!nombre || !apellido) {
      alert("Por favor ingresa nombre y apellido");
      return;
    }

    axios.post('http://localhost:8001/api/lists/', { nombre, apellido })
      .then(res => {
        onPersonaAgregada(res.data);
        setNombre('');
        setApellido('');
      })
      .catch(err => {
        console.error('Error al agregar persona:', err);
      });
  };

  return (
    <div>
      <input
        className="mb-2 form-control"
        value={nombre}
        onChange={(e) => setNombre(e.target.value)}
        placeholder="Nombre"
      />
      <input
        className="mb-2 form-control"
        value={apellido}
        onChange={(e) => setApellido(e.target.value)}
        placeholder="Apellido"
      />
      <button
        className="btn btn-outline-primary mb-3"
        style={{ borderRadius: '50px', fontWeight: 'bold' }}
        onClick={handleAddPersona}
      >
        Agregar
      </button>
    </div>
  );
}

export default FormularioPersona;
