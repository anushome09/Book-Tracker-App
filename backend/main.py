from fastapi import FastAPI
from backend.auth import auth_router
from backend.routes import user


app = FastAPI()

app.include_router(user.route, prefix="/users", tags=["Users"])
app.include_router(auth_router.router)

