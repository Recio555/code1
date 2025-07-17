import React, { useState } from 'react';

const RegisterTutor = () => {
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    password: '',
    subjects: '',
    experience: '',
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

    // Preparamos los datos para enviarlos a la API
    const preparedData = {
      ...formData,
      subjects: formData.subjects.split(',').map(s => s.trim()), // convertir string en array
      experience: parseInt(formData.experience, 10)
    };

    console.log('Tutor registrado:', preparedData);
    // Aquí puedes hacer la petición a la API con fetch o axios

    setSubmitted(true);
    setFormData({
      name: '',
      email: '',
      password: '',
      subjects: '',
      experience: '',
    });
  };

  return (
    <div>
      <h2>Registro de Tutor</h2>
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
          Materias:
          <input type="text" name="subjects" placeholder="Materias (separadas por comas)" value={formData.subjects} onChange={handleChange} required />
        </label>
        <br />
        <label>
          Años de experiencia:
          <input type="number" name="experience" placeholder="Años de experiencia" value={formData.experience} onChange={handleChange} required />
        </label>
        <br />
        <button type="submit">Registrarse</button>
      </form>
    </div>
  );
};

export default RegisterTutor;

