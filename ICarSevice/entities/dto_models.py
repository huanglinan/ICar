from datetime import datetime
from typing import List, Optional
from uuid import UUID
from pydantic import BaseModel, Field


class BaseAudit(BaseModel):
    id: Optional[UUID]
    name: Optional[str] = None
    logo: Optional[str] = None
    desc: Optional[str] = None
    createDate: Optional[datetime] = None
    updateDate: Optional[datetime] = None


class BrandDTO(BaseAudit):
    class Config:
        orm_mode = True


class BrandRequestDTO(BaseAudit):
    parameter: BrandDTO = Field(...)


class CarDTO(BaseAudit):
    brand_id: Optional[UUID]
    class Config:
        orm_mode = True


class CarRequestDTO(BaseAudit):
    parameter: CarDTO = Field(...)


class ResponseDTO(BaseModel):
    code: int
    status: str
    message: str
    data: Optional[object]
