import React, { useState } from 'react';

const RegisterStudent = () => {
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    password: '',
    grade: '',
  });

  const [submitted, setSubmitted] = useState(false);

  const handleChange = (e) => {
    setFormData({ 
      ...formData, 
      [e.target.name]: e.target.value 
    });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log('Estudiante registrado:', formData);

    // Aquí puedes hacer la petición a la API (fetch/axios)

    // Simular éxito
    setSubmitted(true);
    setFormData({
      name: '',
      email: '',
      password: '',
      grade: '',
    });
  };

  return (
    <div>
      <h2>Registro de Estudiante</h2>
      {submitted && <p style={{ color: 'green' }}>¡Registro exitoso!</p>}
      <form onSubmit={handleSubmit}>
        <label>
          Nombre:
          <input type="text" name="name" placeholder="Nombre" value={formData.name} onChange={handleChange} required />
        </label>
        <br />
        <label>
          Correo:
          <input type="email" name="email" placeholder="Correo" value={formData.email} onChange={handleChange} required />
        </label>
        <br />
        <label>
          Contraseña:
          <input type="password" name="password" placeholder="Contraseña" value={formData.password} onChange={handleChange} required />
        </label>
        <br />
        <label>
          Grado:
          <input type="text" name="grade" placeholder="Grado" value={formData.grade} onChange={handleChange} required />
        </label>
        <br />
        <button type="submit">Registrarse</button>
      </form>
    </div>
  );
};

export default RegisterStudent;

