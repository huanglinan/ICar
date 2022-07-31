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
    return ResponseDTO(
        code=404,
        status="NOT FOUND",
        message="Resource not found",
        data=None
    ).dict(exclude_none=True)


def send_error_resp(_code: int, _status: str, _msg: str):
    return ResponseDTO(
        code=_code,
        status=_status,
        message=_msg,
        data=None
    ).dict(exclude_none=True)


def send_succes_resp(data: object):
    return ResponseDTO(
        code=200,
        status="OK",
        message="success",
        data=data
    ).dict(exclude_none=True)
