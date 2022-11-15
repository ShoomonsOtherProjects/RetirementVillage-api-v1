from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi_pagination import Page, paginate, add_pagination
from app.server.database import init_db
from app.server.routes.retirement_village import router as Router

# from fastapi.staticfiles import StaticFiles

app = FastAPI()


origins = [
    "http://localhost:5173",
    "http://localhost",
    "http://127.0.0.1:5173",
    "https://www.downsizeable.co.uk"

]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



app.include_router(Router, tags=["RetirementVillages"], prefix="/retirementvillages")

@app.on_event("startup")
async def start_db():
    await init_db()

@app.get("/", tags=["Root"])
async def read_root() -> dict:
    return {"message": "Welcome to your beanie powered app!"}

add_pagination(app)

# app.mount("/static", StaticFiles(directory="static"), name="static")
