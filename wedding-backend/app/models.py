from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class CompanyBase(BaseModel):
    name: str = Field(..., min_length=2, example="Dream Weddings")
    email: EmailStr = Field(..., example="admin@dreamweddings.com")

class CompanyCreate(CompanyBase):
    password: str = Field(..., min_length=6, example="Secret123!")

class CompanyUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None

class CompanyResponse(CompanyBase):
    id: str = None 
    collection_name: str

class Token(BaseModel):
    access_token: str
    token_type: str

class LoginRequest(BaseModel):
    email: EmailStr
    password: str