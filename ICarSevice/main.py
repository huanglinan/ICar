from fastapi import FastAPI
from db_config import engine
from entities import models
from routes import brand_router

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(brand_router.controller)