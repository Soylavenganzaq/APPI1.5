from flask import Flask, redirect, send_from_directory, jsonify
import os
from models.db import Base
from config.database import engine
from config.jwt import * #Importar jwt de la carpeta config
from controllers.component_controller import computador_bp
from controllers.user_controllers import user_bp, register_jwt_error_handlers
from flask_cors import CORS
from flask_jwt_extended import JWTManager
app = Flask(__name__)
#Agregar el jwt de la carpeta config
# Allow cross-origin requests so frontend served from a different origin can call the API
CORS(app)

#Agregar el jwt de la carpeta config
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


# Ruta raíz: devolver información simple sobre la API (no sirve frontend)
@app.route('/')
def index():
    return jsonify({'message': 'API backend. Sirve endpoints JSON. Coloca el frontend en un repo separado.'}), 200


# Manejar favicon.ico: servir si existe en static, sino devolver 204 (vacio)
@app.route('/favicon.ico')
def favicon():
    fav_path = os.path.join(app.root_path, 'static', 'favicon.ico')
    if os.path.exists(fav_path):
        return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico')
    return ('', 204)


# Nota: la UI ahora se sirve desde el repositorio frontend; el backend expone solo JSON.


@app.route('/logout', methods=['POST'])
def logout():
    # Logout stateless: cliente debe borrar el token. Esta ruta existe para que el cliente
    # pueda notificar al servidor y recibe una respuesta 200.
    return jsonify({'message': 'Logged out'}), 200

if __name__ == "__main__":
    # Crear tablas automáticamente si no existen
    print("Verificando y creando tablas de base de datos si es necesario...")
    Base.metadata.create_all(engine)
    print("Tablas listas.")
    app.run(debug=True)