from fastapi import FastAPI
from routers import customers
from helpers.db import Base, engine

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Include the customers router
app.include_router(customers.router)