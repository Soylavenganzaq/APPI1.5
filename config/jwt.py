<<<<<<< HEAD
import os
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
JWT_TOKEN_LOCATION = ["headers"] 
JWT_ACCESS_TOKEN_EXPIRES = 2600 #Tiempo definido para el límite de autenticación en la aplicación en segundos, en este caso funciona si lo estas usando o si no. 3600=1hr tiempo estánda
=======
#Configuración de JWT para autenticación y autorización
import os
JWT_SECRET_KEY = os.getenv('JWT_SERCRET_KEY')
JWT_TOKEN_LOCATION = ["headers"]
JWT_ACCESS_TOKEN_EXPIRES = 3600  # 1 hora
>>>>>>> dev
JWT_HEADER_NAME = "Authorization"
JWT_HEADER_TYPE = "Bearer"