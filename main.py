from flask import Flask
from config.jwt import *
from controllers.component_controller import computador_bp
from controllers.user_controllers import user_bp
app = Flask(__name__)



# Configurar JWT
app.config['JWT_SECRET_KEY'] = JWT_SECRET_KEY
app.config['JWT_TOKEN_LOCATION'] = JWT_TOKEN_LOCATION
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = JWT_ACCESS_TOKEN_EXPIRES
app.config['JWT_HEADER_NAME'] = JWT_HEADER_NAME
app.config['JWT_HEADER_TYPE'] = JWT_HEADER_TYPE

# Registrar el blueprint de bandas
app.register_blueprint(computador_bp)
app.register_blueprint(user_bp)
if __name__ == "__main__":
    app.run(debug=True)