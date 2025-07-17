import React, { useState, useEffect } from 'react';
import axios from 'axios';

function ListaPersonas() {
  const [personas, setPersonas] = useState([]);
  useEffect(() => {
    axios.get('http://localhost:8001/api/lists')
      .then(res => {
        setPersonas(res.data);
      })
      .catch(err => {
        console.error('Error fetching todos:', err);
      });
  }, []);
  

  return (
    <div>
      {personas.map((item, index) => (
        <div key={index} className="list-group-item">
          {item.name} {item.nombre} {item.apellido}
        </div>
      ))}
    </div>
  );
}

export default ListaPersonas;
