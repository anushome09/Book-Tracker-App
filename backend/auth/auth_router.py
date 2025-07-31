from fastapi import APIRouter, HTTPException, status
from backend.auth.jwt_handler import create_access_token
from backend.schemas.token import Token, LoginRequest
from backend.crud.users import get_user_by_email
import bcrypt

router = APIRouter()

# Function for Sign In
@router.post("/login", response_model=Token)
def login_user(credentials: LoginRequest):
    
    # Checking the user
    user = get_user_by_email(credentials.email)
    
    if not user:
        raise HTTPException(status_code=401, detail="Invalid email or password")
    if not bcrypt.checkpw(credentials.password.encode(), user['password'].encode()):
        raise HTTPException(status_code=401, detail="Invalid email or password")
    
    token = create_access_token(data={"sub": str(user["user_id"])})
    return {"access_token": token, "token_type": "bearer"}