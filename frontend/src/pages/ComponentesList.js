import React, { useEffect, useState } from "react";
import { fetchComponentes } from "../api";

export default function ComponentesList() {
  const [items, setItems] = useState([]);
  const [error, setError] = useState("");

  useEffect(() => {
    (async () => {
      try {
        const data = await fetchComponentes();
        setItems(data);
      } catch (err) {
        setError("No se pudieron cargar componentes");
      }
    })();
  }, []);

  return (
    <div>
      <h3>Componentes</h3>
      {error && <p style={{ color: "red" }}>{error}</p>}
      <ul>
        {items.map((c) => (
          <li key={c.id}>
            <b>{c.nombre}</b> — {c.descripcion || "sin descripción"} (cat: {c.categoria_id})
          </li>
        ))}
      </ul>
    </div>
  );
}
