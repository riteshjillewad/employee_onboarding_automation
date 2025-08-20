from pydantic import BaseModel, Field, EmailStr
from datetime import date

class Employee(BaseModel):
    name: str
    address: str
    phone: str
    email: EmailStr
    position: str
    duration: int
    start_date: date
    age: int
    gender: str
    end_date: date | None = None # This will be calculated later