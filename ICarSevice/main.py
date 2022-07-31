from sys import prefix
from fastapi import FastAPI
from db_config import engine
from entities import models
from routes import brand_router, car_router

models.Base.metadata.create_all(bind=engine)

app = FastAPI(prefix="/api/v1")

app.include_router(brand_router.controller)
app.include_router(car_router.controller)