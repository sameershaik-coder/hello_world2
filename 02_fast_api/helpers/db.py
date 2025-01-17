from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL = "postgresql+psycopg2://postgres:Test@123@localhost/fastapi02"

engine = create_engine(DATABASE_URL)

local_session = sessionmaker(bind=engine)

# Create a base class for declarative class definitions
Base = declarative_base()


def get_db():
    return local_session 