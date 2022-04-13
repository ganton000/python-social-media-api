from pydantic import BaseSettings
import os
#from dotenv import load_dotenv
#load_dotenv()

class Settings(BaseSettings):
    DATABASE_USERNAME: str
    DATABASE_PASSWORD: str
    DATABASE_HOST: str
    DATABASE_PORT: str
    DATABASE_NAME: str
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int

    class Config:
        #env_file = 'fastapi/app/.env'
        #env_file = ".env"
        #env_file = os.path.expanduser('~/.env')
        env_file = f"{os.path.dirname(os.path.abspath(__file__))}/./.env"
        #env_file = "/Users/georgeanton/Desktop/Python_Projects/fastapi/app/.env"

settings = Settings()