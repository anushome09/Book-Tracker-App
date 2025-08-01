from fastapi import FastAPI, Request 
from fastapi.staticfiles import StaticFiles   
from fastapi.templating import Jinja2Templates 
from fastapi.responses import HTMLResponse

from backend.auth import auth_router
from backend.routes import book, user
import os

app = FastAPI()

# Resolve correct paths relative to main.py
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES_DIR = os.path.join(BASE_DIR, "frontend", "templates")
STATIC_DIR = os.path.join(BASE_DIR, "frontend", "static")

templates = Jinja2Templates(directory=TEMPLATES_DIR)
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")


@app.get("/", response_class=HTMLResponse)
async def landing_page(request: Request):
    return templates.TemplateResponse("landing.html", {"request": request})

#app.include_router(user.router, prefix="/users", tags=["Users"])
#app.include_router(auth_router.router, prefix="/users", tags=["Users"])
#app.include_router(book.router, prefix="/book", tags= ["Books"])
