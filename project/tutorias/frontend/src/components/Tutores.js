import React, { useEffect, useState } from "react";

const Tutores = () => {
  const [tutores, setTutores] = useState([]);

  useEffect(() => {
    // Simulación de carga de datos
    const fetchTutores = async () => {
      try {
        const response = await fetch("http://localhost:3000/api/tutores"); // Ajusta la URL según tu backend
        if (!response.ok) {
          throw new Error("Error al obtener tutores");
        }
        const data = await response.json();
        setTutores(data);
      } catch (error) {
        console.error(error);
      }
    };

    fetchTutores();
  }, []);

  return (
    <div>
      <h2>Lista de Tutores</h2>
      {tutores.length > 0 ? (
        <ul>
          {tutores.map((tutor) => (
            <li key={tutor.id}>
              {tutor.name} - {tutor.subject}
            </li>
          ))}
        </ul>
      ) : (
        <p>No hay tutores disponibles.</p>
      )}
    </div>
  );
};

export default Tutores;
