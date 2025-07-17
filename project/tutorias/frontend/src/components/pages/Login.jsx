import React, { useState } from "react";
import { loginUser } from "./api/api";
import { useNavigate, Link } from "react-router-dom";

import "../css/LoginForm.css";


const LoginForm = () => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState(null);
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();

    // Validar que los campos no estén vacíos
    if (!username || !password) {
      setError("Por favor, ingresa usuario y contraseña.");
      return;
    }

    try {
      // Corregir la llamada para enviar datos correctamente
      const data = await loginUser(username, password);
      if (!data || !data.access_token) {
        throw new Error("Error en la autenticación. Verifica tus credenciales.");
      }
      //Rutas protegidas por el login
      localStorage.setItem("token", data.access_token);
    } catch (err) {
      setError(err.message);
    }
  };

  return (
    <div className="login-container">
         Login
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="Usuario"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
          required
        />
        <input
          type="password"
          placeholder="Contraseña"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          required
        />
        <button type="submit">LOGING</button>
      </form>
      {error && <p className="error-message">{error}</p>}
      <p className="signup-text">
        ¿No tienes una cuenta?{" "}
        <Link to="/register" className="signup-link">Regístrate aquí</Link>
      </p>
    </div>
  );
};

export default LoginForm;