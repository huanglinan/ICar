from datetime import datetime
from uuid import UUID
from fastapi import Depends
from entities.models import Car
from db_config import SessionLocal
from entities.dto_models import CarDTO
from entities.dto_models import ResponseDTO
from routes.base_router import BASE_URL, VERSION, get_db, send_error_resp, send_notfound_resp, send_succes_resp
from sqlalchemy.orm import Session
from fastapi import APIRouter
from services import car_service


PATH = "cars"
controller = APIRouter(prefix=f"/{BASE_URL}/{VERSION}/{PATH}", tags=[PATH])


@controller.get("", response_model=ResponseDTO)
async def get_cars(db: Session = Depends(get_db)):
    cars = car_service.get_cards(db)
    if(cars is not None):
        return send_succes_resp(cars)
    return send_notfound_resp()


@controller.get("/{id}", response_model=ResponseDTO)
async def get_car_by_id(id: UUID, db: Session = Depends(get_db)):
    selected: Car = car_service.get_car_by_id(db, id)
    if selected is not None:
        return send_succes_resp(selected)
    return send_notfound_resp()


@controller.post("", response_model=ResponseDTO)
async def create_car(new_car: CarDTO, db: SessionLocal = Depends(get_db)):
    try:
        car = car_service.create_car(db, new_car)
        if car is None:
            return send_error_resp(400, "Bad Request", "Failed to create resource")
    except Exception:
        return send_error_resp(400, "Bad Request", "Failed to create resource")
    return send_succes_resp(None)


@controller.delete("/{id}", response_model=ResponseDTO)
async def delete_car(id: UUID, db: SessionLocal = Depends(get_db)):
    selected: Car = car_service.get_car_by_id(db, id)
    if selected is not None:
        car_service.delete_car(selected)
        return send_succes_resp(None)
    return send_notfound_resp()


@controller.put("/{id}", response_model=ResponseDTO)
async def update_car(updateData: CarDTO, id: UUID, db: SessionLocal = Depends(get_db)):
    selected: Car = car_service.get_car_by_id(db, id)
    if selected is not None:
        if updateData.name is not None:
            selected.name = updateData.name
        if updateData.desc is not None:
            selected.desc = updateData.desc
        if updateData.logo is not None:
            selected.logo = updateData.logo
        selected.updateDate = datetime.now()
        return send_succes_resp(None)
    return send_notfound_resp()
