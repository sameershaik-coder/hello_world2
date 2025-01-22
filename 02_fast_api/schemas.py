from pydantic import BaseModel

class Customer(BaseModel):
    id:int
    username:str
    email:str
    mobile:int

    class Config:
        orm_mode = True  # Enables ORM compatibility for SQLAlchemy models