from fastapi import APIRouter, HTTPException, Depends, Query
from sqlalchemy.orm import Session
from models import Customer as CustomerModel
from schemas import Customer as CustomerSchema
from helpers.db import get_db


router = APIRouter(prefix="/customers", tags=["Customers"])

@router.post("/", response_model=CustomerSchema)
def create_customer(customer: CustomerSchema, db: Session = Depends(get_db)):
    # Check if the email already exists
    existing_customer = db.query(CustomerModel).filter(CustomerModel.email == customer.email).first()
    if existing_customer:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    # Create a new customer instance
    new_customer = CustomerModel(
        username=customer.username,
        email=customer.email,
        mobile=customer.mobile
    )
    db.add(new_customer)
    db.commit()
    db.refresh(new_customer)  # Fetch the latest data for the customer
    
    return new_customer

@router.get("/")
def get_customers_with_metadata(
    page: int = Query(1, ge=1),
    size: int = Query(10, ge=1),
    db: Session = Depends(get_db),
):
    offset = (page - 1) * size
    total_customers = db.query(CustomerModel).count()
    customers = db.query(CustomerModel).offset(offset).limit(size).all()
    return {
        "page": page,
        "size": size,
        "total_records": total_customers,
        "total_pages": (total_customers + size - 1) // size,  # Ceiling division
        "data": customers,
    }