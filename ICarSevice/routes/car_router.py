from uuid import UUID
from fastapi import HTTPException
from base_router import BASE_URL, VERSION, get_db
from fastapi import APIRouter

PATH = "cars"
BASE_PATH = "/{BASE_URL}/{VERSION}/{PATH}"

controller = APIRouter()


# @controller.get("{BASE_PATH}")
# async def get_cars():
#     if(cars is not None):
#         return ResponseMessage(
#             status=200,
#             message=SUCCESS,
#             data=cars
#         )
#     raise HTTPException(
#         status_code=404,
#         detail="No car found!"
#     )


# @controller.get("{BASE_PATH}/{id}")
# async def get_car_by_id(id: UUID4):
#     if(cars is not None):
#         selected: Car = None
#         try:
#             selected = next(item for item in cars if item.id == id)
#         except StopIteration:
#             pass

#         if selected is not None:
#             return ResponseMessage(
#                 status=00,
#                 message=SUCCESS,
#                 data=selected
#             )
#     raise HTTPException(
#         status_code=404,
#         detail="No car found!"
#     )


# @controller.post("{BASE_PATH}")
# async def create_car(newCar: Car):
#     try:
#         newCar.id = uuid4()
#         newCar.createDate = datetime.now()
#         newCar.updateDate = datetime.now()
#         cars.append(newCar)
#     except Exception:
#         raise HTTPException(
#             status_code=400,
#             detail="Cannot Create new Car!"
#         )
#     return ResponseMessage(
#         status=00,
#         message=SUCCESS,
#         data=None
#     )


# @controller.delete("{BASE_PATH}/{id}")
# async def delete_car(id: UUID):
#     if(cars is not None):
#         selected: Car = None
#         try:
#             selected = next(item for item in cars if item.id == id)
#         except StopIteration:
#             pass

#         if selected is not None:
#             cars.remove(selected)
#             return ResponseMessage(
#                 status=00,
#                 message=SUCCESS,
#                 data=None
#             )
#     raise HTTPException(
#         status_code=404,
#         detail="No car found!"
#     )


# @controller.put("{BASE_PATH}/{id}")
# async def update_car(updateData: BrandUpdateMessage, id: UUID):
#     if(cars is not None):
#         selected: Car = None
#         try:
#             selected = next(item for item in cars if item.id == id)
#         except StopIteration:
#             pass

#         if selected is not None:
#             if updateData.name is not None:
#                 selected.name = updateData.name
#             if updateData.desc is not None:
#                 selected.desc = updateData.desc
#             if updateData.logo is not None:
#                 selected.logo = updateData.logo
#             selected.updateDate = datetime.now()
#             return ResponseMessage(
#                 status=00,
#                 message=SUCCESS,
#                 data=None
#             )
#     raise HTTPException(
#         status_code=404,
#         detail="No car found!"
#     )
