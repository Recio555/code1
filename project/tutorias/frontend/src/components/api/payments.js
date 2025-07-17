// api/payments.js
import axios from 'axios';

const API_URL = process.env.REACT_APP_API_URL || 'http://localhost:5000/api';

export const getUserPaymentMethods = async () => {
  try {
    const response = await axios.get(`${API_URL}/payments/methods`);
    return response.data;
  } catch (error) {
    throw new Error(error.response?.data?.message || 'Error al obtener métodos de pago');
  }
};

export const addPaymentMethod = async (paymentData) => {
  try {
    const response = await axios.post(`${API_URL}/payments/methods`, paymentData);
    return response.data;
  } catch (error) {
    throw new Error(error.response?.data?.message || 'Error al añadir método de pago');
  }
};

export const removePaymentMethod = async (paymentMethodId) => {
  try {
    const response = await axios.delete(`${API_URL}/payments/methods/${paymentMethodId}`);
    return response.data;
  } catch (error) {
    throw new Error(error.response?.data?.message || 'Error al eliminar método de pago');
  }
};

export const getPaymentHistory = async (filters = {}) => {
  try {
    const response = await axios.get(`${API_URL}/payments/history`, { params: filters });
    return response.data;
  } catch (error) {
    throw new Error(error.response?.data?.message || 'Error al obtener historial de pagos');
  }
};

export const makePayment = async (paymentData) => {
  try {
    const response = await axios.post(`${API_URL}/payments/process`, paymentData);
    return response.data;
  } catch (error) {
    throw new Error(error.response?.data?.message || 'Error al procesar pago');
  }
};

export const getSubscriptionPlans = async () => {
  try {
    const response = await axios.get(`${API_URL}/payments/plans`);
    return response.data;
  } catch (error) {
    throw new Error(error.response?.data?.message || 'Error al obtener planes de suscripción');
  }
};

export const subscribeToplan = async (planId, paymentMethodId) => {
  try {
    const response = await axios.post(`${API_URL}/payments/subscribe`, {
      planId,
      paymentMethodId
    });
    return response.data;
  } catch (error) {
    throw new Error(error.response?.data?.message || 'Error al suscribirse al plan');
  }
};