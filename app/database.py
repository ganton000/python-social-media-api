#Connection with postgresql session/environment
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
#from dotenv import load_dotenv
#import os
from app.config import settings

#Load environment variables
#load_dotenv()
username= settings.DATABASE_USERNAME
password= settings.DATABASE_PASSWORD
host = settings.DATABASE_HOST
port = settings.DATABASE_PORT
database_name = settings.DATABASE_NAME


SQLALCHEMY_DATABASE_URL = f'postgresql://{username}:{password}@{host}:{port}/{database_name}'

#Connects to Postgresql Driver to connect to DB
engine = create_engine(SQLALCHEMY_DATABASE_URL)

#Starts session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#Model to define Postgresql Tables
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



#import psycopg2
#from dotenv import load_dotenv
#import os
#from psycopg2.extras import RealDictCursor
#import time
#Connect to Postgresql Database
#while True:
#    try:

#        load_dotenv()
#        username= os.environ.get('USERNAME')
#        password= os.environ.get('PASSWORD')
#        host = os.environ.get('HOST')
#        database = os.environ.get('DATABASE')

#        conn = psycopg2.connect(host=host, database=database,\
#        user=username, password=password, cursor_factory=RealDictCursor)

#        cursor = conn.cursor()
#        print('Database connection was successful!')
#        break

#    except Exception as error:
#        print(f'Connecting to database failed: {error}')
#        time.sleep(2)