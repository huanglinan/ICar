import uuid
from sqlalchemy import Boolean, Column, String, Text, DateTime
from sqlalchemy.dialects.postgresql import UUID
from db_config import Base


class BaseAudit():
    name = Column(String(255), nullable=False, unique=True)
    desc = Column(Text)
    is_active = Column(Boolean)
    createDate = Column(DateTime)
    updateDate = Column(DateTime)


class Brand(BaseAudit, Base):
    __tablename__ = 'tb_brand'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    logo = Column(UUID(as_uuid=True))


class Car(BaseAudit, Base):
    __tablename__ = 'tb_car'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    brand_id = Column(UUID(as_uuid=True))
    logo = Column(UUID(as_uuid=True))


class Logo(BaseAudit, Base):
    __tablename__ = 'tb_logo'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    file = Column(String)
