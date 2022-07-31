from enum import unique
import uuid
from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.dialects.postgresql import UUID
from db_config import Base


class BaseAudit():    
    name= Column(String(255), nullable=False, unique=True)
    logo= Column(String)
    desc= Column(Text)
    createDate= Column(DateTime)
    updateDate= Column(DateTime)


class Brand(BaseAudit, Base):
    __tablename__ = 'tb_brand'
    id= Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

class Car(BaseAudit, Base):
    __tablename__ = 'tb_car'
    id= Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    brand_id=  Column(UUID(as_uuid=True), default=uuid.uuid4)
