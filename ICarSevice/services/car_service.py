
from sqlalchemy.orm import Session
from uuid import UUID
from datetime import datetime
import logging
from ICarSevice.entities.dto_models import CarDTO
from ICarSevice.entities.models import Car


# Get All cards
def get_cards(db: Session):
    try:
        return db.query(Car).all()
    except Exception as e:
        logging.error('Error: ', e)
    return None


# Get a Car
def get_car_by_id(db: Session, id: UUID):
    try:
        return db.query(Car).filter(Car.id == id).first()
    except Exception as e:
        logging.error('Error: ', e)
    return None


# Create a Car
def create_car(db: Session, carDTO: CarDTO):
    try:
        new_car = Car(
            name=carDTO.name,
            logo=carDTO.logo,
            desc=carDTO.logo,
            brand_id=carDTO.brand_id,
            createDate=datetime.now(),
            updateDate=datetime.now()
        )
        db.add(new_car)
        db.commit()
        db.refresh()
        return new_car
    except Exception as e:
        logging.error('Error: ', e)
    return None


# Delete a Car
def delete_car(db: Session, id: UUID):
    try:
        car = get_car_by_id(db, id)
        if car is None:
            raise Exception('not found car with id {id}')
        db.delete(car)
        db.commit()
    except Exception as e:
        logging.error('Error: ', e)
