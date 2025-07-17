import axios from 'axios';

const handleCreateSession = async () => {
    //setLoading(true);
    try {
      const response = await axios.post('http://localhost:8001/api/v1/virtual-class/sessions/abc123');
      const newSessionId = response.data.session_id;
      //setSessionId(newSessionId);
      //Navegar al aula
      //console.log(`/aula/${newSessionId}`);
      //navigate(`/aula/${newSessionId}`);
    } catch (error) {
    //  console.error("Error al crear sesión:", error);
    //  alert("No se pudo crear la sesión.");
   // } finally {
    //  setLoading(false);
   }
};

//const API_URL = process.env.REACT_APP_API_URL || 'http://localhost:8001';
const API_URL = "http://localhost:8001";

axios.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('token');
    if (token) {
      config.headers['Authorization'] = `Bearer ${token}`;
    }
    return config;
  },
  (error) => Promise.reject(error)
);

axios.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response?.status === 401) {
      localStorage.removeItem('token');
      window.location.href = '/login';
    }
    return Promise.reject(error);
  }
);
export async function loginUserPrueba(username, password) {
  try {
    // En una implementación real, aquí harías una petición al servidor
    // const response = await fetch('tu_endpoint/login', {
    //   method: 'POST',
    //   headers: {
    //     'Content-Type': 'application/json',
    //   },
    //   body: JSON.stringify({ username, password }),
    // });
    
    // if (!response.ok) {
    //   throw new Error('Error en las credenciales');
    // }
    
    // const data = await response.json();
    
    // Datos simulados (solo para ejemplo)
    const data = {
      access_token: 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJob...zNTR9.y9L440K4fzmVih0OsVA6S4UPR7PKPEW9cIcivl00lWQ',
      token_type: 'bearer'
    };
    
    console.log('Autenticación exitosa', data);
    
    if (!data.access_token) {
      throw new Error('Token no recibido');
    }
    
    // Almacenar el token
    localStorage.setItem('token', data.access_token);
    
    return {
      success: true,
      token: data.access_token,
      tokenType: data.token_type
    };
    
  } catch (error) {
    console.error('Error en loginUser:', error.message);
    return {
      success: false,
      error: error.message
    };
  }
}

// Función con fetch para login (versión B)
export async function loginUser(username, password) {
  try {
    if (!username || !password) {
      throw new Error("Usuario y contraseña son requeridos.");
    }
    const response = await fetch("http://localhost:8001/auth/login", {
      method: "POST",
      headers: { "Content-Type": "application/x-www-form-urlencoded" },
      body: new URLSearchParams({ username, password }),
    });
    if (!response.ok) {
      const errorData = await response.json();
      throw new Error(errorData.detail || "Error en la autenticación.");
    }
    const data = await response.json();
    console.log(data)
    
     if (!data.access_token) {
      throw new Error('Token no recibido');
    }
    
    // Almacenar el token
    localStorage.setItem('token', data.access_token);
    if (user.section_id) {
    localStorage.setItem('sectionId', user.section_id);
     }
    
    return {
      success: true,
      token: data.access_token,
      tokenType: data.token_type
    };
    
  } catch (error) {
    console.error('Error en loginUser:', error.message);
    return {
      success: false,
      error: error.message
    };
  }
}

export const logoutUser = async () => {
  try {
    await axios.post(`${API_URL}/auth/logout`);
    localStorage.removeItem('token');
    return true;
  } catch (error) {
    throw new Error(error.response?.data?.message || 'Error al cerrar sesión');
  }
};

// Puedes dejar los otros métodos como están si los usas (registerUser, getCurrentUser, etc.)

