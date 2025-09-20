from flask import Flask
from controllers.component_controller import computador_bp

app = Flask(__name__)

# Registrar el blueprint de bandas
app.register_blueprint(computador_bp)

if __name__ == "__main__":
    app.run(debug=True)