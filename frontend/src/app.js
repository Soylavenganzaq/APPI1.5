import React from "react";
import { Routes, Route, Link } from "react-router-dom";
import Login from "./pages/Login";
import ComponentesList from "./pages/ComponentesList";
import NuevoComponente from "./pages/NuevoComponente";
import PrivateRoute from "./components/PrivateRoute";

export default function App() {
  return (
    <div style={{ padding: 20, fontFamily: "Arial, sans-serif" }}>
      <nav style={{ marginBottom: 20 }}>
        <Link to="/">Home</Link> {" | "}
        <Link to="/componentes">Componentes</Link> {" | "}
        <Link to="/nuevo">Nuevo</Link> {" | "}
        <Link to="/login">Login</Link>
      </nav>

      <Routes>
        <Route path="/" element={<h2>Bienvenido al panel de Componentes</h2>} />
        <Route path="/login" element={<Login />} />
        <Route path="/componentes" element={<ComponentesList />} />
        <Route
          path="/nuevo"
          element={
            <PrivateRoute>
              <NuevoComponente />
            </PrivateRoute>
          }
        />
      </Routes>
    </div>
  );
}
