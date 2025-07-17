import React from 'react';
import { Link } from 'react-router-dom';

const LandingPage = () => {
  return (
    <div style={styles.container}>
      <h1>Bienvenido a la Plataforma de Tutorías</h1>
      <p>Conecta con tutores expertos y mejora tus habilidades desde cualquier lugar.</p>
      <div style={styles.buttons}>
        
        <Link to="/register" style={styles.buttonSecondary}>Registrarse</Link>
      </div>
    </div>
  );
};

const styles = {
  container: {
    maxWidth: '600px',
    margin: '100px auto',
    textAlign: 'center',
    padding: '2rem',
    backgroundColor: '#f0f8ff',
    borderRadius: '8px',
    boxShadow: '0 4px 10px rgba(0, 0, 0, 0.1)',
  },
  buttons: {
    marginTop: '2rem',
    display: 'flex',
    justifyContent: 'center',
    gap: '1rem',
  },
  button: {
    padding: '0.75rem 1.5rem',
    backgroundColor: '#007bff',
    color: '#fff',
    textDecoration: 'none',
    borderRadius: '4px',
    fontWeight: 'bold',
  },
  buttonSecondary: {
    padding: '0.75rem 1.5rem',
    backgroundColor: '#6c757d',
    color: '#fff',
    textDecoration: 'none',
    borderRadius: '4px',
    fontWeight: 'bold',
  },
};

export default LandingPage;
