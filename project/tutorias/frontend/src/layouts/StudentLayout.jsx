import { Outlet, NavLink, useNavigate } from "react-router-dom";
import { useAuth } from "../contexts/AuthContext";
import { useEffect } from "react";
import "../components/styles/layout.css";

const StudentLayout = () => {
  const { logout, user, isAuthenticated } = useAuth();
  const navigate = useNavigate();

  useEffect(() => {
    if (!isAuthenticated) {
      navigate("/login", { replace: true });
    } else if (user?.role !== "student") {
      navigate("/unauthorized", { replace: true });
    }
  }, [isAuthenticated, user?.role, navigate]);

  const navLinkStyle = ({ isActive }) => ({
    fontWeight: isActive ? "600" : "400",
    color: isActive ? "#2c3e50" : "#555",
    backgroundColor: isActive ? "#f0f4f8" : "transparent"
  });

  if (!isAuthenticated || user?.role !== "student") {
    return null;
  }

  return (
    <div className="student-layout">
      <header className="student-header">
        <div className="header-content">
          <NavLink to="/student/dashboard" className="brand-link">
            <span className="app-name">Tutorías Matemáticas</span>
            <span className="user-role-badge">Estudiante</span>
          </NavLink>

          <nav className="student-nav">
            <ul className="nav-list">
              <li>
                <NavLink 
                  to="/student/dashboard" 
                  style={navLinkStyle}
                  end
                >
                  Inicio
                </NavLink>
              </li>
              <li>
                <NavLink 
                  to="/student/find-tutors" 
                  style={navLinkStyle}
                >
                  Buscar Tutores
                </NavLink>
              </li>
              <li>
                <NavLink 
                  to="/student/my-sessions" 
                  style={navLinkStyle}
                >
                  Mis Sesiones
                </NavLink>
              </li>
              <li>
                <NavLink 
                  to="/student/progress" 
                  style={navLinkStyle}
                >
                  Mi Progreso
                </NavLink>
              </li>
            </ul>
          </nav>

          <div className="student-actions">
            <button onClick={logout} className="logout-btn">
              Cerrar Sesión
            </button>
          </div>
        </div>
      </header>

      <main className="student-main">
        <Outlet />
      </main>

      <footer className="student-footer">
        <p>Soporte: estudiantes@tutorias.com</p>
        <p>Horario de atención: Lunes a Viernes 8am - 6pm</p>
      </footer>
    </div>
  );
};

export default StudentLayout;