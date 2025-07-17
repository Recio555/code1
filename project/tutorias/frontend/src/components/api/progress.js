// api/progress.js
import axios from 'axios';

const API_URL = process.env.REACT_APP_API_URL || 'http://localhost:5000/api';

export const getUserProgress = async () => {
  try {
    const response = await axios.get(`${API_URL}/progress`);
    return response.data;
  } catch (error) {
    throw new Error(error.response?.data?.message || 'Error al obtener progreso');
  }
};

export const getUserStreak = async () => {
  try {
    const response = await axios.get(`${API_URL}/progress/streak`);
    return response.data;
  } catch (error) {
    throw new Error(error.response?.data?.message || 'Error al obtener racha de estudio');
  }
};

export const getLanguageProficiency = async (language) => {
  try {
    const response = await axios.get(`${API_URL}/progress/proficiency`, {
      params: { language }
    });
    return response.data;
  } catch (error) {
    throw new Error(error.response?.data?.message || 'Error al obtener nivel de competencia');
  }
};

export const getStudyStats = async (period = 'month') => {
  try {
    const response = await axios.get(`${API_URL}/progress/stats`, {
      params: { period }
    });
    return response.data;
  } catch (error) {
    throw new Error(error.response?.data?.message || 'Error al obtener estadísticas');
  }
};

export const setStudyGoal = async (goalData) => {
  try {
    const response = await axios.post(`${API_URL}/progress/goals`, goalData);
    return response.data;
  } catch (error) {
    throw new Error(error.response?.data?.message || 'Error al establecer objetivo');
  }
};

export const getUserGoals = async () => {
  try {
    const response = await axios.get(`${API_URL}/progress/goals`);
    return response.data;
  } catch (error) {
    throw new Error(error.response?.data?.message || 'Error al obtener objetivos');
  }
};