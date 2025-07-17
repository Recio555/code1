import axios from 'axios';

const API_URL = process.env.REACT_APP_API_URL || 'http://localhost:3001/auth/login';

// Configura axios para incluir automáticamente el token en cada solicitud
axios.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('token');
    if (token) {
      config.headers['Authorization'] = `Bearer ${token}`;
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

// Manejo global de errores
axios.interceptors.response.use(
  (response) => response,
  (error) => {
    // Si hay un error 401 (No autorizado), eliminar token y redirigir al login
    if (error.response && error.response.status === 401) {
      localStorage.removeItem('token');
      window.location.href = '/login';
    }
    return Promise.reject(error);
  }
);

export const Login = async (email, password) => {
  try {
    const response = await axios.post(`${API_URL}/auth/login`, {
      email,
      password,
    });
    return response.data;
  } catch (error) {
    throw new Error(error.response?.data?.message || 'Error al iniciar sesión');
  }
};

export const loginUser = async () => {
  const formData = new URLSearchParams();
  formData.append("username", email); // FastAPI espera el campo "username"
  formData.append("password", password);

  try {
    const response = await fetch("http://localhost:3001/api/login", {
      method: "POST",
      headers: {
        "Content-Type": "application/x-www-form-urlencoded",
      },
      body: formData.toString(),
    });

    const data = await response.json();
    console.log("Token:", data.access_token);
  } catch (error) {
    console.error("Login error:", error);
  }
};



export const registerUser = async (userData) => {
  try {
    const response = await axios.post(`${API_URL}/auth/register`, userData);
    return response.data;
  } catch (error) {
    throw new Error(error.response?.data?.message || 'Error al registrarse');
  }
};

export const getCurrentUser = async () => {
  try {
    const response = await axios.get(`${API_URL}/auth/me`);
    return response.data;
  } catch (error) {
    throw new Error(error.response?.data?.message || 'Error al obtener usuario');
  }
};

export const logoutUser = async () => {
  try {
    await axios.post(`${API_URL}/auth/logout`);
    return true;
  } catch (error) {
    throw new Error(error.response?.data?.message || 'Error al cerrar sesión');
  }
};

export const resetPassword = async (email) => {
  try {
    const response = await axios.post(`${API_URL}/auth/reset-password`, { email });
    return response.data;
  } catch (error) {
    throw new Error(error.response?.data?.message || 'Error al solicitar cambio de contraseña');
  }
};

export const updatePassword = async (token, newPassword) => {
  try {
    const response = await axios.post(`${API_URL}/auth/update-password`, {
      token,
      password: newPassword,
    });
    return response.data;
  } catch (error) {
    throw new Error(error.response?.data?.message || 'Error al actualizar contraseña');
  }
};