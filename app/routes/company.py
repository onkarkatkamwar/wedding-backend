from fastapi import APIRouter, HTTPException, status, Depends
from app.models import CompanyCreate, CompanyResponse, CompanyUpdate
from app.database import get_master_collection, get_tenant_collection
from app.security import get_password_hash
from fastapi.security import OAuth2PasswordBearer
from app.security import verify_password

router = APIRouter(prefix="/company", tags=["Company Management"])
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

@router.post("/register", response_model=CompanyResponse)
async def create_company(company: CompanyCreate):
    master_col = get_master_collection()
    
    # Check if exists
    if await master_col.find_one({"name": company.name}):
        raise HTTPException(status_code=400, detail="Company name already exists")
    if await master_col.find_one({"email": company.email}):
        raise HTTPException(status_code=400, detail="Email already registered")

    # Create dynamic collection logic
    tenant_col = get_tenant_collection(company.name)
    # Initialize tenant collection with a dummy config or admin profile
    await tenant_col.insert_one({
        "type": "config",
        "created_at": "now",
        "admin_email": company.email
    })

    new_company = {
        "name": company.name,
        "email": company.email,
        "password": get_password_hash(company.password),
        "collection_name": tenant_col.name
    }
    
    result = await master_col.insert_one(new_company)
    
    return {
        "name": new_company["name"],
        "email": new_company["email"],
        "collection_name": new_company["collection_name"],
        "id": str(result.inserted_id)
    }

@router.get("/{name}", response_model=CompanyResponse)
async def get_company(name: str):
    master_col = get_master_collection()
    company = await master_col.find_one({"name": name})
    if not company:
        raise HTTPException(status_code=404, detail="Company not found")
    
    return {
        "name": company["name"],
        "email": company["email"],
        "collection_name": company.get("collection_name", ""),
        "id": str(company["_id"])
    }

@router.delete("/{name}")
async def delete_company(name: str, token: str = Depends(oauth2_scheme)):
    # In a real app, verify token is from a super-admin or the company owner
    master_col = get_master_collection()
    company = await master_col.find_one({"name": name})
    
    if not company:
        raise HTTPException(status_code=404, detail="Company not found")

    # Drop the dynamic collection
    tenant_col = get_tenant_collection(name)
    await tenant_col.drop()

    # Remove from master
    await master_col.delete_one({"name": name})
    
    return {"message": f"Company {name} and its data have been deleted."}