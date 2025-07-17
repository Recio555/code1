import { Routes, Route, Navigate, useLocation } from "react-router-dom";
import PublicLayout from "../layouts/PublicLayout";
import PrivateLayout from "../layouts/PrivateLayout";
import HomePage from "../components/pages/HomePage";
import About from "../components/pages/About";
import Contact from "../components/pages/Contact";
import Dashboard from "../components/pages/Dashboard";
import Profile from "../components/pages/Profile";
import Settings from "../components/pages/Settings";
import { useAuth } from "../contexts/AuthContext";
import LoginForm from "../components/LoginForm";
import RegisterForm from "../components/RegisterForm";
import VirtualClassroom from "../components/aulaVirtual/aula";

// Ruta privada que redirige a /login con la ruta original como query
const PrivateRoute = ({ children }) => {
  const { token } = useAuth();
  const location = useLocation();

  return token ? (
    children
  ) : (
    <Navigate to={`/login?redirectTo=${encodeURIComponent(location.pathname)}`} replace />
  );
};

const AppRoutes = () => {
  return (
    <Routes>
      {/* Rutas públicas */}
      <Route element={<PublicLayout />}>
        <Route path="/" element={<HomePage />} />
        <Route path="/about" element={<About />} />
        <Route path="/contact" element={<Contact />} />
        <Route path="/login" element={<LoginForm />} />
        <Route path="/register" element={<RegisterForm />} />
      </Route>

      {/* Rutas privadas */}
      <Route
        element={
          <PrivateRoute>
            <PrivateLayout />
          </PrivateRoute>
        }
      >
        <Route path="/dashboard" element={<Dashboard />} />
        <Route path="/profile" element={<Profile />} />
        <Route path="/settings" element={<Settings />} />
        <Route path="/aula/:sessionId" element={<VirtualClassroom />} />
      </Route>

      {/* Ruta por defecto */}
      <Route path="*" element={<Navigate to="/" />} />
    </Routes>
  );
};

export default AppRoutes;


