import axios from 'axios';

const API_URL = process.env.REACT_APP_API_URL || 'http://localhost:5000/api';

export const getAllExercises = async (filters = {}) => {
  try {
    const response = await axios.get(`${API_URL}/exercises`, { params: filters });
    return response.data;
  } catch (error) {
    throw new Error(error.response?.data?.message || 'Error al obtener ejercicios');
  }
};

export const getExerciseById = async (id) => {
  try {
    const response = await axios.get(`${API_URL}/exercises/${id}`);
    return response.data;
  } catch (error) {
    throw new Error(error.response?.data?.message || 'Error al obtener ejercicio');
  }
};

export const submitExerciseAnswer = async (id, answer) => {
  try {
    const response = await axios.post(`${API_URL}/exercises/${id}/submit`, { answer });
    return response.data;
  } catch (error) {
    throw new Error(error.response?.data?.message || 'Error al enviar respuesta');
  }
};

export const getUserExercises = async () => {
  try {
    const response = await axios.get(`${API_URL}/user/exercises`);
    return response.data;
  } catch (error) {
    throw new Error(error.response?.data?.message || 'Error al obtener ejercicios del usuario');
  }
};

export const getRecommendedExercises = async () => {
  try {
    const response = await axios.get(`${API_URL}/exercises/recommended`);
    return response.data;
  } catch (error) {
    throw new Error(error.response?.data?.message || 'Error al obtener ejercicios recomendados');
  }
};