import React, { useEffect, useState } from 'react';
import {fetchTutors} from '../api/fetchTutors';




const TutorList = () => {
  const [tutores, setTutores] = useState([]);
  const [error, setError] = useState(null);

  useEffect(() => {
    const token = localStorage.getItem('token');
    if (token) {
      fetchTutors(token)
        .then(data => setTutores(data))
        .catch(err => setError(err.message));
    }
  }, []);

  return (
    <div>
      <h1>Tutores</h1>
      {error && <p>{error}</p>}
      <ul>
        {tutores.map(tutor => (
          <li key={tutor.id}>{tutor.name} - {tutor.expertise}</li>
        ))}
      </ul>
    </div>
  );
};

export default TutorList;
