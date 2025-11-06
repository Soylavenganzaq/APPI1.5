const API_BASE = import.meta.env.VITE_API_BASE || "http://127.0.0.1:5000";

function getToken() {
  return localStorage.getItem("access_token");
}

function authHeaders() {
  const token = getToken();
  return token ? { Authorization: `Bearer ${token}` } : {};
}

export async function login(username, password) {
  const res = await fetch(`${API_BASE}/auth/login`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ username, password })
  });
  if (!res.ok) throw new Error("Login falló");
  return res.json(); // espera { access_token: "..." }
}

export async function fetchComponentes() {
  const res = await fetch(`${API_BASE}/componentes`, {
    headers: { "Content-Type": "application/json" }
  });
  if (!res.ok) throw new Error("Error al obtener componentes");
  return res.json();
}

export async function crearComponente(payload) {
  const res = await fetch(`${API_BASE}/componentes`, {
    method: "POST",
    headers: { "Content-Type": "application/json", ...authHeaders() },
    body: JSON.stringify(payload)
  });
  if (!res.ok) throw new Error("Error creando componente");
  return res.json();
}
