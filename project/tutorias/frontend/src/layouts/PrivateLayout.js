import { Outlet, NavLink, useNavigate, useLocation } from "react-router-dom";
import { useAuth } from "../contexts/AuthContext";
import { useEffect, useState } from "react";
import "../components/styles/layout.css"; // Asegúrate de tener este archivo CSS

const PrivateLayout = () => {
  const { logout, user, isAuthenticated } = useAuth();
  const navigate = useNavigate();
  const location = useLocation();
  const [isMenuOpen, setIsMenuOpen] = useState(false);

  // Cerrar menú al cambiar de ruta
  useEffect(() => {
    setIsMenuOpen(false);
  }, [location]);

  // Redirigir si no está autenticado
  useEffect(() => {
    if (!isAuthenticated) {
      navigate("/login", { state: { from: location }, replace: true });
    }
  }, [isAuthenticated, navigate, location]);

  const handleLogout = async () => {
    try {
      await logout();
      navigate("/login", { replace: true });
    } catch (error) {
      console.error("Error al cerrar sesión:", error);
    }
  };

  // Estilo activo para NavLink
  const navLinkStyle = ({ isActive }) => ({
    fontWeight: isActive ? "600" : "400",
    color: isActive ? "#2c3e50" : "#555",
    backgroundColor: isActive ? "#f0f4f8" : "transparent"
  });

  if (!isAuthenticated) {
    return null; // O un componente de carga
  }

  return (
    <div className="private-layout">
      <header className="private-header">
        <div className="header-content">
          <div className="brand-container">
            <NavLink to="/dashboard" className="brand-link">
              <span className="app-name"><h3>TUTORIA GLOVAL</h3></span>
              {user?.role && (
                <span className="user-role-badge">{user.role}</span>
              )}
            </NavLink>
          </div>

          {/* Menú móvil */}
          <button
            className="menu-toggle"
            aria-label="Toggle navigation"
            aria-expanded={isMenuOpen}
            onClick={() => setIsMenuOpen(!isMenuOpen)}
          >
            <span className="hamburger-line"></span>
            <span className="hamburger-line"></span>
            <span className="hamburger-line"></span>
          </button>

          <nav className={`main-nav ${isMenuOpen ? "open" : ""}`}>
            <ul className="nav-list">
              <li className="nav-item">
                <NavLink
                  to="/dashboard"
                  className="nav-link"
                  style={navLinkStyle}
                  end
                >
                  Dashboard
                </NavLink>
              </li>
              <li className="nav-item">
                <NavLink
                  to="/profile"
                  className="nav-link"
                  style={navLinkStyle}
                >
                  Perfil
                </NavLink>
              </li>
              <li className="nav-item">
                <NavLink
                  to="/settings"
                  className="nav-link"
                  style={navLinkStyle}
                >
                  Configuración
                </NavLink>
              </li>
              <li className="nav-item">
                <NavLink
                  to="/aula"
                  className="nav-link"
                  style={navLinkStyle}
                >
                  Aula Virtual
                </NavLink>
              </li>
              
              {/* Menú adicional según roles */}
              {user?.role === "admin" && (
                <li className="nav-item">
                  <NavLink
                    to="/admin"
                    className="nav-link"
                    style={navLinkStyle}
                  >
                    Admin
                  </NavLink>
                </li>
              )}
            </ul>
          </nav>

          <div className="user-section">
            {user && (
              <div className="user-info">
                <span className="user-name">{user.name || user.email}</span>
                {user.avatar && (
                  <img
                    src={user.avatar}
                    alt="User avatar"
                    className="user-avatar"
                  />
                )}
              </div>
            )}
            <NavLink
                  to=""
                  onClick={handleLogout}
                  className="nav-link"
                  style={navLinkStyle}
                >
                  Salir
            </NavLink>
          </div>
        </div>
      </header>

      <main className="private-main">
        <Outlet />
      </main>

      <footer className="private-footer">
        <p>© {new Date().getFullYear()} MiApp. Todos los derechos reservados.</p>
        <div className="footer-links">
          <NavLink to="/privacy" className="footer-link">
            Privacidad
          </NavLink>
          <NavLink to="/terms" className="footer-link">
            Términos
          </NavLink>
        </div>
      </footer>
    </div>
  );
};

export default PrivateLayout;

