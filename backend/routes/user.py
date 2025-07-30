from fastapi import APIRouter, HTTPException

from backend.crud.users import create_new_user
from backend.schemas.user import UserCreate


route = APIRouter()

# function (api) to register user
@route.post("/", status_code=201)
def register_user(user: UserCreate):
    try:
        user_id = create_new_user(user)
        return {"message": "User created successfully", "user_id": user_id}
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))