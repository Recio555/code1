
// api/sessions.js
import axios from 'axios';

const API_URL = process.env.REACT_APP_API_URL || 'http://localhost:5000/api';

export const getUserSessions = async (status = 'all') => {
  try {
    const response = await axios.get(`${API_URL}/sessions`, { params: { status } });
    return response.data;
  } catch (error) {
    throw new Error(error.response?.data?.message || 'Error al obtener sesiones');
  }
};

export const getSessionById = async (id) => {
  try {
    const response = await axios.get(`${API_URL}/sessions/${id}`);
    return response.data;
  } catch (error) {
    throw new Error(error.response?.data?.message || 'Error al obtener sesión');
  }
};

export const cancelSession = async (id, reason) => {
  try {
    const response = await axios.post(`${API_URL}/sessions/${id}/cancel`, { reason });
    return response.data;
  } catch (error) {
    throw new Error(error.response?.data?.message || 'Error al cancelar sesión');
  }
};

export const updateSession = async (id, sessionData) => {
  try {
    const response = await axios.put(`${API_URL}/sessions/${id}`, sessionData);
    return response.data;
  } catch (error) {
    throw new Error(error.response?.data?.message || 'Error al actualizar sesión');
  }
};

// Para la transmisión de video/chat en tiempo real, se recomienda usar Socket.IO
// Aquí solo incluiremos métodos para guardar mensajes o notas de las sesiones

export const saveSessionNotes = async (id, notes) => {
  try {
    const response = await axios.post(`${API_URL}/sessions/${id}/notes`, { notes });
    return response.data;
  } catch (error) {
    throw new Error(error.response?.data?.message || 'Error al guardar notas');
  }
};

export const sendSessionMessage = async (id, message) => {
  try {
    const response = await axios.post(`${API_URL}/sessions/${id}/messages`, { message });
    return response.data;
  } catch (error) {
    throw new Error(error.response?.data?.message || 'Error al enviar mensaje');
  }
};
