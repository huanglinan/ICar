from fastapi import HTTPException
from db_config import SessionLocal
from entities.dto_models import ResponseDTO

BASE_URL = "api"
VERSION = "v1"


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def send_notfound_resp():
    raise HTTPException(status_code=404, detail="Resource not found")


def send_error_resp(_code: int, _msg: str):
    raise HTTPException(status_code=_code, detail=_msg)


def send_succes_resp(data: object):
    return ResponseDTO(
        code=200,
        status="OK",
        message="success",
        data=data
    )
