import { Outlet, NavLink, useNavigate, useLocation } from "react-router-dom";
import { useAuth } from "../contexts/AuthContext";
import { useEffect, useState } from "react";
import "../components/styles/global.css";

const PublicLayout = () => {
  const { isAuthenticated, logout, user, isLoading } = useAuth();
  const navigate = useNavigate();
  const location = useLocation();
  const [isMenuOpen, setIsMenuOpen] = useState(false);

  // Cerrar menú al cambiar de ruta
  useEffect(() => {
    setIsMenuOpen(false);
  }, [location]);

  const handleLogout = async () => {
    try {
      await logout();
      navigate("/", { replace: true }); // Redirige al home reemplazando el historial
    } catch (error) {
      console.error("Error al cerrar sesión:", error);
    }
  };

  // Estilo activo para NavLink
  const navLinkStyle = ({ isActive }) => ({
    fontWeight: isActive ? "bold" : "normal",
    color: isActive ? "#2c3e50" : "#34495e",
    textDecoration: isActive ? "underline" : "none"
  });

  return (
    <div className="layout-container">
      <header className="header">
        <nav className="nav-bar">
          {/* Logo o marca */}
          <div className="nav-brand">
            <NavLink to="/" end className="nav-link">
             Tutorias
            </NavLink>
          </div>

          {/* Menú para móviles */}
          <button 
            className="menu-toggle"
            aria-label="Toggle menu"
            aria-expanded={isMenuOpen}
            onClick={() => setIsMenuOpen(!isMenuOpen)}
          >
            <span className="hamburger"></span>
          </button>

          {/* Navegación principal */}
          <div className={`nav-links ${isMenuOpen ? "open" : ""}`}>
            <NavLink to="/" end className="nav-link" style={navLinkStyle}>
              Home
            </NavLink>
            <NavLink to="/about" className="nav-link" style={navLinkStyle}>
              About
            </NavLink>
            <NavLink to="/contact" className="nav-link" style={navLinkStyle}>
              Contact
            </NavLink>

            {/* Menú de usuario */}
            <div className="user-menu">
              {isLoading ? (
                <div className="loading-spinner"></div>
              ) : isAuthenticated ? (
                <>
                  {user && (
                    <span className="welcome-message">
                      Hola, {user.name || user.email}
                    </span>
                  )}
                  <button
                    onClick={handleLogout}
                    className="logout-button"
                    aria-label="Cerrar sesión"
                  >
                    Logout
                  </button>
                </>
              ) : (
                <NavLink 
                  to="/login" 
                  className="nav-link login-link" 
                  style={navLinkStyle}
                  state={{ from: location }}
                >
                  Login
                </NavLink>
              )}
            </div>
          </div>
        </nav>
      </header>

      <main className="main-content">
        <Outlet />
      </main>

      <footer className="footer">
        <p>© {new Date().getFullYear()} Mi Aplicación. Todos los derechos reservados.</p>
      </footer>
    </div>
  );
};

export default PublicLayout;


