

from datetime import datetime
from typing import Optional
from pydantic import UUID4, BaseModel


class BaseAudit(BaseModel):
    name: str
    logo: str
    desc: str
    createDate: Optional[datetime]
    updateDate: Optional[datetime]


class Brand(BaseAudit):
    id: Optional[UUID4]


class Car(BaseAudit):
    id: Optional[UUID4]


class ResponseMessage(BaseModel):
    status: int
    message: str
    data: Optional[object]

class BrandUpdateMessage(BaseModel):
    name: Optional[str]
    logo: Optional[str]
    desc: Optional[str]
 