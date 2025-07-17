import axios from 'axios';

const API_URL = process.env.REACT_APP_API_URL || 'http://localhost:5000/api';

export const getAllTutors = async (filters = {}) => {
  try {
    const response = await axios.get(`${API_URL}/tutors`, { params: filters });
    return response.data;
  } catch (error) {
    throw new Error(error.response?.data?.message || 'Error al obtener tutores');
  }
};

export const getTutorById = async (id) => {
  try {
    const response = await axios.get(`${API_URL}/tutors/${id}`);
    return response.data;
  } catch (error) {
    throw new Error(error.response?.data?.message || 'Error al obtener tutor');
  }
};

export const getTutorAvailability = async (id) => {
  try {
    const response = await axios.get(`${API_URL}/tutors/${id}/availability`);
    return response.data;
  } catch (error) {
    throw new Error(error.response?.data?.message || 'Error al obtener disponibilidad');
  }
};

export const bookSession = async (tutorId, sessionData) => {
  try {
    const response = await axios.post(`${API_URL}/tutors/${tutorId}/book`, sessionData);
    return response.data;
  } catch (error) {
    throw new Error(error.response?.data?.message || 'Error al reservar sesión');
  }
};

export const rateSession = async (sessionId, rating, review) => {
  try {
    const response = await axios.post(`${API_URL}/sessions/${sessionId}/review`, {
      rating,
      review,
    });
    return response.data;
  } catch (error) {
    throw new Error(error.response?.data?.message || 'Error al calificar sesión');
  }
};

export const getTutorReviews = async (tutorId) => {
  try {
    const response = await axios.get(`${API_URL}/tutors/${tutorId}/reviews`);
    return response.data;
  } catch (error) {
    throw new Error(error.response?.data?.message || 'Error al obtener reseñas');
  }
};