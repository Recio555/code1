import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
import { useState, useEffect } from "react";

// Importa tus componentes
import TutorLoginForm from "./TutorLoginForm";
import StudentLoginForm from "./StudentLoginForm"; // Suponemos que existe
import Dashboard from "./Dashboard"; // Suponemos que existe
import NotFound from "./NotFound"; // Suponemos que existe

// Layout con protección de rutas
const ProtectedRoute = ({ children }) => {
  const [isAuthenticated, setIsAuthenticated] = useState(false);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    // Función para verificar si el usuario está autenticado
    const checkAuth = async () => {
      try {
        // Aquí verificarías el token almacenado en localStorage o cookies
        const token = localStorage.getItem("authToken");
        
        if (!token) {
          setIsAuthenticated(false);
          return;
        }
        
        // Opcional: Validar el token con el backend
        const response = await fetch("/api/auth/verify", {
          headers: {
            Authorization: `Bearer ${token}`
          }
        });
        
        if (response.ok) {
          setIsAuthenticated(true);
        } else {
          // Token inválido, eliminar
          localStorage.removeItem("authToken");
          setIsAuthenticated(false);
        }
      } catch (error) {
        console.error("Error verificando autenticación:", error);
        setIsAuthenticated(false);
      } finally {
        setLoading(false);
      }
    };
    
    checkAuth();
  }, []);

  // Muestra un indicador de carga mientras verifica la autenticación
  if (loading) {
    return (
      <div className="flex items-center justify-center h-screen">
        <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-500"></div>
      </div>
    );
  }

  // Redirige a login si no está autenticado
  if (!isAuthenticated) {
    return <Navigate to="/login/tutor" replace />;
  }

  // Si está autenticado, muestra el contenido protegido
  return children;
};

const AppRouter = () => {
  return (
    <BrowserRouter>
      <Routes>
        {/* Rutas públicas */}
        <Route path="/login">
          <Route path="tutor" element={<TutorLoginForm />} />
          <Route path="student" element={<StudentLoginForm />} />
          <Route index element={<Navigate to="/login/tutor" replace />} />
        </Route>
        
        {/* Página de inicio - redirige al dashboard si está autenticado */}
        <Route path="/" element={<Navigate to="/dashboard" replace />} />
        
        {/* Rutas protegidas */}
        <Route 
          path="/dashboard" 
          element={
            <ProtectedRoute>
              <Dashboard />
            </ProtectedRoute>
          } 
        />
        
        {/* Ruta para manejar URLs no existentes */}
        <Route path="*" element={<NotFound />} />
      </Routes>
    </BrowserRouter>
  );
};

export default AppRouter;