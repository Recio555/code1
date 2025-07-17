// src/pages/LoginPage.js
import React, { useState } from "react";
import { useAuth } from "../contexts/AuthContext";
import { useNavigate, useLocation } from "react-router-dom";

function LoginPage() {
  const { login, isAuthenticated, logout } = useAuth();
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [errorMsg, setErrorMsg] = useState("");
  const navigate = useNavigate();
  const location = useLocation();

  const from = location.state?.from?.pathname || "/dashboard";

  const handleLogin = async (e) => {
    e.preventDefault();
    setErrorMsg("");
    const { error } = await login(email, password);
    if (error) {
      setErrorMsg(error);
    } else {
      navigate(from, { replace: true }); // redirige tras login exitoso
    }
  };

  if (isAuthenticated) {
    return (
      <div>
        <h2>Ya estás logueado</h2>
        <button onClick={logout}>Cerrar sesión</button>
      </div>
    );
  }

  return (
    <form onSubmit={handleLogin}>
      <h2>Iniciar sesión</h2>
      {errorMsg && <p style={{ color: "red" }}>{errorMsg}</p>}
      <input
        type="email"
        placeholder="Correo electrónico"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
        required
      />
      <br />
      <input
        type="password"
        placeholder="Contraseña"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
        required
      />
      <br />
      <button type="submit">Entrar</button>
    </form>
  );
}

export default LoginPage;

