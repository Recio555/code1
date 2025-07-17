import axios from 'axios';

// Usa esta constante como base de tu API
const API_URI = "http://localhost:8001";



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
    console.log('estoy en api', data);
    return data;  // <-- Aquí retornas la data del login exitoso
  } catch (error) {
    console.error("Error al iniciar sesión:", error.message);
    return { error: error.message };  // <-- También retornas el error
  }
}


// Instancia de Axios para uso general
const api = axios.create({
  baseURL: API_URI,
});
console.log("La URL base de la API es:", api.defaults.baseURL);
export default api;
