# Separated repos: Backend (API) + Frontend (estático)

He separado el frontend estático dentro de `frontend/` y he actualizado el backend para que únicamente exponga endpoints JSON.

Qué cambié (resumen):
- `frontend/` creado con `index.html`, `computadores.html`, `static/css/login.css` y `static/js/app.js`.
- Backend ya no sirve plantillas ni la UI (`/login` GET y `/computadores/ui` fueron eliminadas).
- Añadí CORS en `main.py` para permitir llamadas desde el frontend alojado en otro origen.

Instrucciones rápidas:
- Levantar backend: `python main.py` (por defecto en `http://127.0.0.1:5000`).
- Levantar frontend: `cd frontend && python -m http.server 8080` y abrir `http://127.0.0.1:8080/index.html`.

Si quieres, puedo inicializar repos git locales separados (`git init`) para backend y frontend y preparar los commits iniciales.
p