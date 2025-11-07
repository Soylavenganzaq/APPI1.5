from flask import Flask, redirect, send_from_directory
import os
from flask import render_template
from models.db import Base
from config.database import engine
from config.jwt import * #Importar jwt de la carpeta config
from controllers.component_controller import computador_bp
from controllers.user_controllers import user_bp, register_jwt_error_handlers
from flask_jwt_extended import JWTManager
app = Flask(__name__)

#Agregar el jwt de la carpeta config
app.config['JWT_SECRET_KEY'] = JWT_SECRET_KEY
app.config['JWT_TOKEN_LOCATION'] = JWT_TOKEN_LOCATION
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = JWT_ACCESS_TOKEN_EXPIRES #Configurar el tiempo en el que se debe volver a autenticar a la aplicación
app.config['JWT_HEADER_NAME'] = JWT_HEADER_NAME 
app.config['JWT_HEADER_TYPE'] = JWT_HEADER_TYPE

# Registrar el blueprint de bandas. Realizar un registro del controlador dentro del main para poder crear un nuevo registro
app.register_blueprint(computador_bp)
app.register_blueprint(user_bp)

# Configurar JWT
app.config['JWT_SECRET_KEY'] = JWT_SECRET_KEY
app.config['JWT_TOKEN_LOCATION'] = JWT_TOKEN_LOCATION
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = JWT_ACCESS_TOKEN_EXPIRES
app.config['JWT_HEADER_NAME'] = JWT_HEADER_NAME
app.config['JWT_HEADER_TYPE'] = JWT_HEADER_TYPE

jwt = JWTManager(app)


# Registrar manejadores personalizados de error JWT
register_jwt_error_handlers(app)


# Ruta raíz: redirige a /login para evitar 404 al visitar '/'
@app.route('/')
def index():
    return redirect('/login')


# Manejar favicon.ico: servir si existe en static, sino devolver 204 (vacio)
@app.route('/favicon.ico')
def favicon():
    fav_path = os.path.join(app.root_path, 'static', 'favicon.ico')
    if os.path.exists(fav_path):
        return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico')
    return ('', 204)


# Servir la página de gestión de computadores (interfaz CRUD)
@app.route('/computadores/ui')
def computadores_ui_page():
    # Página UI separada del endpoint API que también usa /computadores
    return render_template('computadores.html')

if __name__ == "__main__":
    # Crear tablas automáticamente si no existen
    print("Verificando y creando tablas de base de datos si es necesario...")
    Base.metadata.create_all(engine)
    print("Tablas listas.")
    app.run(debug=True)