import React, { useState } from "react";
import RegisterStudent from './api/RegisterStudent.js';
import RegisterTutor from './api/RegisterTutor';
import '../css/registerForm.css';



const RegisterForm = () => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [expertise, setExpertise] = useState("");
  const [availability, setAvailability] = useState([]);
  const [userType, setUserType] = useState("student");
  const [materia, setmateria] = useState("")

   const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      if (userType === "student") {
         RegisterStudent({ username, password, name, email });
      } else {
         RegisterTutor({ username, password, name, expertise, availability, materia });
      }
      alert("Registro exitoso!");
    } catch (err) {
      console.error(err);
      alert("Hubo un error en el registro.");
    }
  };

  return (
    <div>
      <h1>Formulario de Registro</h1>
      <form onSubmit={handleSubmit}>
        <label>Nombre:</label>
        <input type="text" value={name} onChange={(e) => setName(e.target.value)} required />
        <label>Correo electrónico:</label>
        <input type="email" value={email} onChange={(e) => setEmail(e.target.value)} required />
        <label>Nombre de usuario:</label>
        <input type="text" value={username} onChange={(e) => setUsername(e.target.value)} required />
        <label>Contraseña:</label>
        <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} required />
        {userType === "tutor" && (
          <>
            <label>Área de Expertise:</label>
            <input type="text" value={expertise} onChange={(e) => setExpertise(e.target.value)} />
            <label>Disponibilidad (ej. "Mon 10:00"):</label>
            <input type="text" value={availability} onChange={(e) => setAvailability(e.target.value.split(','))} />
             <label>materia:</label>
             <input type="text" value={availability} onChange={(e) => setmateria(e.target.value.split(','))} />
          </>
        )}
        <label>Tipo de usuario:</label>
        <select onChange={(e) => setUserType(e.target.value)} value={userType}>
          <option value="student">Alumno</option>
          <option value="tutor">Tutor</option>
        </select>
        <button type="submit">Registrar</button>
      </form>
    </div>
  );
};

export default RegisterForm;
