from sys import prefix
from fastapi import FastAPI
from db_config import engine
from entities import models
from routes import brand_router, car_router
from fastapi.middleware.cors import CORSMiddleware

models.Base.metadata.create_all(bind=engine)

app = FastAPI(prefix="/api/v1")

origins = [
    "http://localhost",
    "http://localhost:4200",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(brand_router.controller)
app.include_router(car_router.controller)

