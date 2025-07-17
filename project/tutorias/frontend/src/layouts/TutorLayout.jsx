import { Outlet, NavLink, useNavigate } from "react-router-dom";
import { useAuth } from "../contexts/AuthContext";
import { useEffect, useState } from "react";
import "../components/styles/layout.css";

const TutorLayout = () => {
  const { logout, user, isAuthenticated } = useAuth();
  const navigate = useNavigate();
  const [availabilityStatus, setAvailabilityStatus] = useState(false);

  useEffect(() => {
    if (!isAuthenticated) {
      navigate("/login", { replace: true });
    } else if (user?.role !== "tutor") {
      navigate("/unauthorized", { replace: true });
    }
  }, [isAuthenticated, user?.role, navigate]);

  const navLinkStyle = ({ isActive }) => ({
    fontWeight: isActive ? "600" : "400",
    color: isActive ? "#2c3e50" : "#555",
    backgroundColor: isActive ? "#f0f4f8" : "transparent"
  });

  const toggleAvailability = () => {
    setAvailabilityStatus(!availabilityStatus);
    // Aquí iría la lógica para actualizar en backend
  };

  if (!isAuthenticated || user?.role !== "tutor") {
    return null;
  }

  return (
    <div className="tutor-layout">
      <header className="tutor-header">
        <div className="header-content">
          <NavLink to="/tutor/dashboard" className="brand-link">
            <span className="app-name">Tutorías Matemáticas</span>
            <span className="user-role-badge">Tutor</span>
          </NavLink>

          <nav className="tutor-nav">
            <ul className="nav-list">
              <li>
                <NavLink 
                  to="/tutor/dashboard" 
                  style={navLinkStyle}
                  end
                >
                  Panel
                </NavLink>
              </li>
              <li>
                <NavLink 
                  to="/tutor/schedule" 
                  style={navLinkStyle}
                >
                  Horario
                </NavLink>
              </li>
              <li>
                <NavLink 
                  to="/tutor/sessions" 
                  style={navLinkStyle}
                >
                  Sesiones
                </NavLink>
              </li>
              <li>
                <NavLink 
                  to="/tutor/students" 
                  style={navLinkStyle}
                >
                  Estudiantes
                </NavLink>
              </li>
              <li>
                <NavLink 
                  to="/tutor/resources" 
                  style={navLinkStyle}
                >
                  Recursos
                </NavLink>
              </li>
            </ul>
          </nav>

          <div className="tutor-actions">
            <button 
              onClick={toggleAvailability}
              className={`availability-toggle ${availabilityStatus ? 'available' : 'unavailable'}`}
            >
              {availabilityStatus ? 'Disponible' : 'No disponible'}
            </button>
            <button onClick={logout} className="logout-btn">
              Cerrar Sesión
            </button>
          </div>
        </div>
      </header>

      <aside className="tutor-sidebar">
        <div className="tutor-profile">
          {user?.avatar && (
            <img src={user.avatar} alt="Tutor" className="tutor-avatar" />
          )}
          <h3>{user?.name || "Tutor"}</h3>
          <p>Especialidad: {user?.specialty || "Matemáticas"}</p>
          <p>Calificación: ★★★★☆</p>
        </div>
      </aside>

      <main className="tutor-main">
        <Outlet />
      </main>

      <footer className="tutor-footer">
        <p>Soporte para tutores: tutores@tutorias.com</p>
        <p>Recuerda actualizar tu disponibilidad regularmente</p>
      </footer>
    </div>
  );
};

export default TutorLayout;