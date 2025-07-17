import React, { useState } from 'react';
import FormularioPersona from './FormularioPersona';
import ListaPersonas from './ListaPersonas';
import 'bootstrap/dist/css/bootstrap.min.css';

function DatosPersona() {
  const [personas, setPersonas] = useState([]);

  const agregarPersona = (nuevaPersona) => {
    setPersonas((prev) => [...prev, nuevaPersona]);
  };

  return (
    <div className="App list-group-item justify-content-center align-items-center mx-auto"
         style={{ width: "400px", backgroundColor: "white", marginTop: "15px" }}>
      <h1 className="card text-white bg-primary mb-1">Task Manager</h1>
      <h6 className="card text-white bg-primary mb-3">FASTAPI - React - MongoDB-Docker</h6>

      <div className="card-body">
        <h5 className="card text-white bg-dark mb-3">Agregar Persona</h5>
        <FormularioPersona onPersonaAgregada={agregarPersona} />

        <h5 className="card text-white bg-dark mb-3">Personas Agregadas</h5>
        <ListaPersonas />
      </div>

      <h6 className="card text-dark bg-warning py-1 mb-0">
        Copyright 2021, All rights reserved &copy;
      </h6>
    </div>
  );
}

export default DatosPersona;
