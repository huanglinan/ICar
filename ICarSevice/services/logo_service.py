from sqlalchemy.orm import Session
from uuid import UUID
from datetime import datetime
from entities.dto_models import LogoDTO
from entities.models import Logo
import logging


# Get a Brand
def get_logo_by_id(db: Session, id: UUID):
    try:
        return db.query(Logo).filter(Logo.id == id).first()
    except Exception as e:
        logging.error('Error: ', e)
    return None


# Create a Brand
def create_logo(db: Session, logoDTO: LogoDTO):
    try:
        new = Logo(
            name=logoDTO.name,
            file=logoDTO.file,
            desc=logoDTO.desc,
            createDate=datetime.now(),
            updateDate=datetime.now()
        )
        db.add(new)
        db.commit()
        return new
    except Exception as e:
        logging.error('Error: ', e)
    return None

# Delete a Brand


def delete_logo(db: Session, id: UUID):
    try:
        logo = get_logo_by_id(db, id)
        if logo is None:
            raise Exception('not found logo with id {id}')
        db.delete(logo)
        db.commit()
    except Exception as e:
        logging.error('Error: ', e)
