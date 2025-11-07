
#Configuración de JWT para autenticación y autorización
import os
from datetime import timedelta

# Corregir nombre de variable de entorno y proveer un valor por defecto para desarrollo
JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY') or os.getenv('JWT_SERCRET_KEY') or 'dev-jwt-secret'
JWT_TOKEN_LOCATION = ["headers"]
# Flask-JWT-Extended acepta timedelta para expiración
JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)
JWT_HEADER_NAME = "Authorization"
JWT_HEADER_TYPE = "Bearer"