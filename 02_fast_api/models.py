from helpers.db import Base
from sqlalchemy import Column, Integer, String

class Customer(Base):
    __tablename__ = "customers"  # Adjust table name to match purpose

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    mobile = Column(Integer)