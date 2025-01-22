from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import urllib.parse

DATABASE_URL = "postgresql+psycopg2://postgres:Test@123@localhost/fastapi02"

def get_url():
    POSTGRES_HOST = "127.0.0.1"
    POSTGRES_USER = "postgres"
    POSTGRES_PASSWORD = "Test@123"
    encoded_password = urllib.parse.quote_plus(POSTGRES_PASSWORD)
    #POSTGRES_HOST = config['postgres']['host']
    POSTGRES_PORT = 5432
    POSTGRES_DB = "fastapi02"

    SQLALCHEMY_DATABASE_URL = f"postgresql+psycopg2://{POSTGRES_USER}:{encoded_password}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
    print(f"Connecting to database: {SQLALCHEMY_DATABASE_URL}")  # Add this to debug
    return SQLALCHEMY_DATABASE_URL

DATABASE_URL = get_url()
engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a base class for declarative class definitions
Base = declarative_base()



def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()