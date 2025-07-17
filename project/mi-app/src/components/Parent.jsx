import React from 'react';
import Hijo from './Child';
import Button from '@mui/material/Button';
import { useState } from 'react';



const msj = "Esta es la data del componente Padre.";


export default function Padre() {
  const [datos, estableceDatos] = useState('');
  const [s, setS] = useState(0);
 

  const padreAHijo = (mensaje) => {
   
    estableceDatos(mensaje);
    setS(s + 1);
  }


  return (
    <div className="App">
      {datos}
      <hr />
      {s}
      <hr />
      <div>
      <Button variant="contained" onClick={() => padreAHijo(msj)}>Clic Padre</Button>
      </div>
      <hr />

      <Hijo padreAHijo={padreAHijo}/>
    </div>
  );
}