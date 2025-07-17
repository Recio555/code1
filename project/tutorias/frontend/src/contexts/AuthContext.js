import {
  createContext,
  useContext,
  useState,
  useEffect,
  useCallback,
} from "react";
import { loginUser, logoutUser } from "../services/authService";

// Creamos el contexto con valor inicial null explícito
const AuthContext = createContext(null);

export const AuthProvider = ({ children }) => {
  const [token, setToken] = useState(null);
  const [user, setUser] = useState(null);
  const [isLoading, setIsLoading] = useState(true);

  // Cargar estado inicial desde localStorage
  useEffect(() => {
    const initializeAuth = () => {
      try {
        const storedToken = localStorage.getItem("token");
        const storedUser = localStorage.getItem("user");

        if (storedToken && storedUser) {
          setToken(storedToken);
          setUser(JSON.parse(storedUser));
        }
      } catch (error) {
        console.error("Error al cargar la sesión:", error);
      } finally {
        setIsLoading(false);
      }
    };

    initializeAuth();
  }, []);

  const logout = useCallback(async () => {
    setIsLoading(true);
    try {
      await logoutUser(); // Puede fallar silenciosamente
    } catch (err) {
      console.error("Error al cerrar sesión:", err);
    } finally {
      setToken(null);
      setUser(null);
      localStorage.removeItem("token");
      localStorage.removeItem("user");
      setIsLoading(false);
    }
  }, []);

  const login = useCallback(async (email, password) => {
    setIsLoading(true);
    try {
      const result = await loginUser(email, password);

      if (!result?.token) {
        throw new Error(result?.error || "No se recibió un token válido.");
      }

      const { token: accessToken, user: userData } = result;

      setToken(accessToken);
      setUser(userData || null);
      localStorage.setItem("token", accessToken);

      if (userData) {
        localStorage.setItem("user", JSON.stringify(userData));
      }

      return { success: true };
    } catch (error) {
      console.error("Error en login:", error.message || error);
      await logout(); // Limpiar sesión en caso de error
      return { success: false, error: error.message };
    } finally {
      setIsLoading(false);
    }
  }, [logout]);

  const isAuthenticated = !!token;

  if (isLoading) {
    return <div>Cargando sesión...</div>; // puedes usar un spinner aquí
  }

  return (
    <AuthContext.Provider
      value={{
        token,
        user,
        isLoading,
        login,
        logout,
        isAuthenticated,
      }}
    >
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = () => {
  const context = useContext(AuthContext);
  if (!context) {
    throw new Error("useAuth debe usarse dentro de un AuthProvider");
  }
  return context;
};

