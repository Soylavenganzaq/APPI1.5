import React, { useState } from "react";
import { crearComponente } from "../api";
import { useNavigate } from "react-router-dom";

export default function NuevoComponente() {
  const [nombre, setNombre] = useState("");
  const [descripcion, setDescripcion] = useState("");
  const [categoria_id, setCategoriaId] = useState("");
  const [error, setError] = useState("");
  const nav = useNavigate();

  async function onSubmit(e) {
    e.preventDefault();
    try {
      await crearComponente({ nombre, descripcion, categoria_id: categoria_id || null });
      nav("/componentes");
    } catch (err) {
      setError("Error creando componente");
    }
  }

  return (
    <div style={{ maxWidth: 600 }}>
      <h3>Nuevo componente</h3>
      <form onSubmit={onSubmit}>
        <div>
          <label>Nombre</label><br />
          <input value={nombre} onChange={(e) => setNombre(e.target.value)} />
        </div>
        <div style={{ marginTop: 8 }}>
          <label>Descripción</label><br />
          <textarea value={descripcion} onChange={(e) => setDescripcion(e.target.value)} />
        </div>
        <div style={{ marginTop: 8 }}>
          <label>Categoria ID</label><br />
          <input value={categoria_id} onChange={(e) => setCategoriaId(e.target.value)} />
        </div>
        <div style={{ marginTop: 10 }}>
          <button type="submit">Crear</button>
        </div>
        {error && <p style={{ color: "red" }}>{error}</p>}
      </form>
    </div>
  );
}
