from fastapi import FastAPI
from backend.auth import auth_router
from backend.routes import book, user


app = FastAPI()

app.include_router(user.router, prefix="/users", tags=["Users"])
app.include_router(auth_router.router, prefix="/users", tags=["Users"])
app.include_router(book.router, prefix="/book", tags= ["Books"])
