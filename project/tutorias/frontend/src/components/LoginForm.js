import React, { useState, useEffect } from "react";
import { useAuth } from "../contexts/AuthContext";
import { useNavigate, Link } from "react-router-dom";
import "../css/LoginForm.css";

const LoginForm = () => {
  const { login, isAuthenticated, isLoading } = useAuth();
  const [formData, setFormData] = useState({
    username: "",
    password: ""
  });
  const [error, setError] = useState(null);
  const navigate = useNavigate();

  // Redirigir si ya está autenticado
  useEffect(() => {
    if (isAuthenticated) {
      navigate('/dashboard');
    }
  }, [isAuthenticated, navigate]);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({
      ...prev,
      [name]: value
    }));
    
    // Limpiar errores al escribir
    if (error) setError(null);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError(null);

    // Validación de campos
    if (!formData.username.trim() || !formData.password.trim()) {
      setError("Por favor, completa todos los campos");
      return;
    }

    try {
      const result = await login(formData.username, formData.password);
      
      if (!result?.success) {
        throw new Error(result?.error || "Error en el inicio de sesión");
      }

      // La redirección se manejará en el efecto por el cambio de isAuthenticated
    } catch (error) {
      console.error('Error en login:', error);
      setError(error.message || "Credenciales incorrectas");
      // Limpiar contraseña por seguridad
      setFormData(prev => ({ ...prev, password: "" }));
    }
  };

  return (
    <div className="login-container">
      <h2>Sesión</h2>
      <form onSubmit={handleSubmit} noValidate>
        <div className="form-group">
          <input
            type="text"
            name="username"
            placeholder="Usuario"
            value={formData.username}
            onChange={handleChange}
            required
            autoComplete="username"
            disabled={isLoading}
          />
        </div>
        
        <div className="form-group">
          <input
            type="password"
            name="password"
            placeholder="Contraseña"
            value={formData.password}
            onChange={handleChange}
            required
            autoComplete="current-password"
            disabled={isLoading}
          />
        </div>

        {error && (
          <div className="error-message">
            <span role="alert">{error}</span>
          </div>
        )}

        <button 
          type="submit" 
          disabled={isLoading || !formData.username || !formData.password}
          className={isLoading ? "loading" : ""}
        >
          {isLoading ? "Procesando..." : "Ingresar"}
        </button>

        <div className="form-footer">
          <p>
            ¿No tienes una cuenta?{" "}
            <Link to="/register" className="signup-link">
              Regístrate aquí
            </Link>
          </p>
          <Link to="/forgot-password" className="forgot-password">
            ¿Olvidaste tu contraseña?
          </Link>
        </div>
      </form>
    </div>
  );
};

export default LoginForm;




