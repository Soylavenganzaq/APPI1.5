import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import { login } from "../api";

export default function Login() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const nav = useNavigate();

  async function onSubmit(e) {
    e.preventDefault();
    try {
      const data = await login(username, password);
      localStorage.setItem("access_token", data.access_token);
      setError("");
      nav("/componentes");
    } catch (err) {
      setError("Error de autenticación");
    }
  }

  return (
    <div style={{ maxWidth: 420 }}>
      <h3>Iniciar sesión</h3>
      <form onSubmit={onSubmit}>
        <div>
          <label>Usuario</label><br />
          <input value={username} onChange={(e) => setUsername(e.target.value)} />
        </div>
        <div style={{ marginTop: 8 }}>
          <label>Contraseña</label><br />
          <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} />
        </div>
        <div style={{ marginTop: 12 }}>
          <button type="submit">Entrar</button>
        </div>
        {error && <p style={{ color: "red" }}>{error}</p>}
      </form>
    </div>
  );
}
