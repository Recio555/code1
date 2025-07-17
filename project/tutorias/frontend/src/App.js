import { BrowserRouter } from "react-router-dom";
import AppRoutes from "./router/AppRoutes";
import { AuthProvider } from "./contexts/AuthContext";
import { SocketProvider } from "./contexts/SocketContext"; // ✅ Se añade el contexto de Socket

function App() {
  return (
    <BrowserRouter>
      <AuthProvider>
        <SocketProvider> {/* ✅ Se envuelve AppRoutes dentro de SocketProvider */}
          <AppRoutes />
        </SocketProvider>
      </AuthProvider>
    </BrowserRouter>
  );
}

export default App;



