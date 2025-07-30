from fastapi import FastAPI
from backend.routes import user


app = FastAPI()

app.include_router(user.route, prefix="/users", tags=["Users"])


