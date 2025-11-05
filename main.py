from flask import Flask
from models.db import Base
from config.jwt import * #Importar jwt de la carpeta config
from config.jwt import *
from controllers.component_controller import computador_bp
from controllers.user_controllers import user_bp, register_jwt_error_handlers
from flask_jwt_extended import JWTManager

from controllers.component_controller import computador_bp
from controllers.user_controllers import user_bp
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

# Registrar el blueprint de libroas
app.register_blueprint(computador_bp)
app.register_blueprint(user_bp)

# Registrar manejadores personalizados de error JWT
register_jwt_error_handlers(app)

if __name__ == "__main__":
    # Crear tablas automáticamente si no existen
    print("Verificando y creando tablas de base de datos si es necesario...")
    Base.metadata.create_all(engine)
    print("Tablas listas.")
    app.run(debug=True)