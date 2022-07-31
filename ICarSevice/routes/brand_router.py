from datetime import datetime
from uuid import UUID
from entities.dto_models import ResponseDTO
from entities.dto_models import BrandDTO
from entities.models import Brand
from routes.base_router import BASE_URL, VERSION, get_db, send_error_resp, send_notfound_resp, send_succes_resp
from sqlalchemy.orm import Session
from services import brand_service
from fastapi import APIRouter, Depends


PATH = "brands"
BASE_PATH = "/{BASE_URL}/{VERSION}/{PATH}"

controller = APIRouter()


@controller.get(BASE_PATH, response_model=ResponseDTO)
async def get_brands(db: Session = Depends(get_db)):
    brands = brand_service.get_brands(db)
    if(brands is not None):
        return send_succes_resp(brands)
    return send_notfound_resp()


@controller.get("{BASE_PATH}/{id}", response_model=ResponseDTO)
async def get_brand_by_id(id: UUID, db: Session = Depends(get_db) ):
    selectedBrand: Brand = brand_service.get_brand_by_id(db, id)
    if selectedBrand is not None:
        return send_succes_resp(selectedBrand)
    return send_notfound_resp()


@controller.post(BASE_PATH, response_model=ResponseDTO)
async def create_brand( new_brand: BrandDTO,db: Session = Depends(get_db)):
    try:
       brand_service.create_brand(db, new_brand)
    except Exception:
        return send_error_resp(400, "Bad Request", "Resource is failed to create")
    return send_succes_resp(None)


@controller.delete("{BASE_PATH}/{id}", response_model=ResponseDTO)
async def delete_brand( id: UUID, db: Session = Depends(get_db)):
    selectedBrand: Brand = brand_service.get_brand_by_id(db, id)
    if selectedBrand is not None:
        brand_service.delete_brand(selectedBrand)
        return send_succes_resp(None)
    return send_notfound_resp()


@controller.put("{BASE_PATH}/{id}", response_model=ResponseDTO)
async def update_brand( updateData: BrandDTO, id: UUID,db: Session = Depends(get_db)):
    selectedBrand: Brand = brand_service.get_brand_by_id(db, id)
    if selectedBrand is not None:
        if updateData.name is not None:
            selectedBrand.name = updateData.name
        if updateData.desc is not None:
            selectedBrand.desc = updateData.desc
        if updateData.logo is not None:
            selectedBrand.logo = updateData.logo
        selectedBrand.updateDate = datetime.now()
        return send_succes_resp(None)
    return send_notfound_resp()
