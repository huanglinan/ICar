from sqlalchemy.orm import Session
from uuid import UUID
from datetime import datetime
from entities.dto_models import BrandDTO
from entities.models import Brand
import logging

# Get All Brands


def get_brands(db: Session):
    try:
        return db.query(Brand).all()
    except Exception as e:
        logging.error('Error: ', e)
    return None


# Get a Brand
def get_brand_by_id(db: Session, id: UUID):
    try:
        return db.query(Brand).filter(Brand.id == id).first()
    except Exception as e:
        logging.error('Error: ', e)
    return None


# Search a Brand
def search_brand_by_name(db: Session, name: str):
    try:
        return db.query(Brand).filter( Brand.name.ilike(f'%{name}%')).all()
    except Exception as e:
        logging.error('Error: ', e)
    return None

# Create a Brand
def create_brand(db: Session, brandDTO: BrandDTO):
    try:
        #print(brandDTO.is_active)
        new_brand = Brand(
            name=brandDTO.name,
            logo=brandDTO.logo,
            desc=brandDTO.desc,
            is_active=brandDTO.is_active,
            createDate=datetime.now(),
            updateDate=datetime.now()
        )
        db.add(new_brand)
        db.commit()
        return new_brand
    except Exception as e:
        logging.error('Error: ', e)
    return None


# Delete a Brand
def delete_brand(db: Session, id: UUID):
    try:
        brand = get_brand_by_id(db, id)
        if brand is None:
            raise Exception('not found brand with id {id}')
        db.delete(brand)
        db.commit()
    except Exception as e:
        logging.error('Error: ', e) 
    
def update_brand(db: Session, brandDTO: BrandDTO):
    try:
        db.add(brandDTO)
        db.commit()
        return brandDTO
    except Exception as e:
        logging.error('Error: ', e)
    return None