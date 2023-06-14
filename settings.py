from decouple import config

ACCESS_TOKEN_EXPIRE = 1  # hour
JWT_ALGORITHM = "HS256"
SECRET_KEY = config("SECRET_KEY")
