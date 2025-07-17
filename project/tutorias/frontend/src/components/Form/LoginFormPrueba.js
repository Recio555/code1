import React, { useState } from "react";
import api from "../api/api";

const LoginFormPrueba = () => {
  const [message, setMessage] = useState("");

  const handleLogin = async (e) => {
    e.preventDefault();
    console.log("URL base de la API:", api.defaults.baseURL);

    try {
      const response = await api.post("/auth/tutor", {
        name: "Juan Pérez",
        subject: "Matemáticas",
        email: "juan@example.com"
      }, {
        headers: {
          "Content-Type": "application/json"
        }
      });

      if (response.status === 200) {
        setMessage(response.data.message || "Login exitoso");
      } else {
        setMessage("Error en login: respuesta inesperada del servidor.");
      }
    } catch (error) {
      console.error("Error en login:", error);

      if (error.response) {
        setMessage(`Error: ${error.response.status} - ${error.response.data.message || "Error desconocido"}`);
      } else {
        setMessage("No se pudo conectar con el servidor.");
      }
    }
  };

  return (
    <div>
      <h2>Tutor</h2>
      <form onSubmit={handleLogin}>
        <button type="submit">Iniciar sesión</button>
      </form>
      {message && <p>{message}</p>}
    </div>
  );
};

export default LoginFormPrueba;

