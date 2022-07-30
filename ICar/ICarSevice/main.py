from datetime import datetime

from sre_constants import SUCCESS
from typing import List
from uuid import UUID, uuid4
from fastapi import FastAPI, HTTPException
from pydantic import UUID4

from ICarSevice.models import Brand, BrandUpdateMessage, Car, ResponseMessage

app = FastAPI()

brands: List[Brand] = [
    Brand(name="Toyota", logo="", desc="brand: toyota",
          createDate=datetime.now(), updateDate=datetime.now(), id=uuid4()),
    Brand(name="BMW", logo="", desc="brand: BMW",
          createDate=datetime.now(), updateDate=datetime.now(), id=uuid4()),
    Brand(name="Honda", logo="", desc="brand: Honda",
          createDate=datetime.now(), updateDate=datetime.now(), id=uuid4())
]

cars: List[Car] = [
    Car(name="Toyota car a1", logo="", desc="brand: toyota",
        createDate=datetime.now(), updateDate=datetime.now(), id=uuid4()),
    Car(name="BMW car a1", logo="", desc="brand: BMW",
        createDate=datetime.now(), updateDate=datetime.now(), id=uuid4()),
    Car(name="Honda car a1", logo="", desc="brand: Honda",
        createDate=datetime.now(), updateDate=datetime.now(), id=uuid4())
]


@app.get("/api/v1/brands")
async def getBrands():
    if(brands is not None):
        return ResponseMessage(
            status=200,
            message=SUCCESS,
            data=brands
        )
    raise HTTPException(
        status_code=404,
        detail="No brand found!"
    )


@app.get("/api/v1/brands/{id}")
async def getBrandById(id: UUID4):
    if(brands is not None):
        selectedBrand: Brand = None
        try:
            selectedBrand = next(item for item in brands if item.id == id)
        except StopIteration:
            pass

        if selectedBrand is not None:
            return ResponseMessage(
                status=00,
                message=SUCCESS,
                data=selectedBrand
            )
    raise HTTPException(
        status_code=404,
        detail="No brand found!"
    )


@app.post("/api/v1/brands")
async def createBrand(newBrand: Brand):
    try:
        newBrand.id = uuid4()
        newBrand.createDate = datetime.now()
        newBrand.updateDate = datetime.now()
        brands.append(newBrand)
    except Exception:
        raise HTTPException(
            status_code=400,
            detail="Cannot Create new Brand!"
        )
    return ResponseMessage(
        status=00,
        message=SUCCESS,
        data=None
    )


@app.delete("/api/v1/brands/{id}")
async def deleteBrand(id: UUID):
    if(brands is not None):
        selectedBrand: Brand = None
        try:
            selectedBrand = next(item for item in brands if item.id == id)
        except StopIteration:
            pass

        if selectedBrand is not None:
            brands.remove(selectedBrand)
            return ResponseMessage(
                status=00,
                message=SUCCESS,
                data=None
            )
    raise HTTPException(
        status_code=404,
        detail="No brand found!"
    )


@app.put("/api/v1/brands/{id}")
async def updateBrand(updateData: BrandUpdateMessage, id: UUID):
    if(brands is not None):
        selectedBrand: Brand = None
        try:
            selectedBrand = next(item for item in brands if item.id == id)
        except StopIteration:
            pass

        if selectedBrand is not None:
            if updateData.name is not None:
                selectedBrand.name = updateData.name
            if updateData.desc is not None:
                selectedBrand.desc = updateData.desc
            if updateData.logo is not None:
                selectedBrand.logo = updateData.logo
            selectedBrand.updateDate = datetime.now()
            return ResponseMessage(
                status=00,
                message=SUCCESS,
                data=None
            )
    raise HTTPException(
        status_code=404,
        detail="No brand found!"
    )


@app.get("/api/v1/cars")
async def getCars():
    if(cars is not None):
        return ResponseMessage(
            status=200,
            message=SUCCESS,
            data=cars
        )
    raise HTTPException(
        status_code=404,
        detail="No car found!"
    )


@app.get("/api/v1/cars/{id}")
async def getCarById(id: UUID4):
    if(cars is not None):
        selected: Car = None
        try:
            selected = next(item for item in cars if item.id == id)
        except StopIteration:
            pass

        if selected is not None:
            return ResponseMessage(
                status=00,
                message=SUCCESS,
                data=selected
            )
    raise HTTPException(
        status_code=404,
        detail="No car found!"
    )


@app.post("/api/v1/cars")
async def createCar(newCar: Car):
    try:
        newCar.id = uuid4()
        newCar.createDate = datetime.now()
        newCar.updateDate = datetime.now()
        cars.append(newCar)
    except Exception:
        raise HTTPException(
            status_code=400,
            detail="Cannot Create new Car!"
        )
    return ResponseMessage(
        status=00,
        message=SUCCESS,
        data=None
    )


@app.delete("/api/v1/cars/{id}")
async def deleteCar(id: UUID):
    if(cars is not None):
        selected: Car = None
        try:
            selected = next(item for item in cars if item.id == id)
        except StopIteration:
            pass

        if selected is not None:
            cars.remove(selected)
            return ResponseMessage(
                status=00,
                message=SUCCESS,
                data=None
            )
    raise HTTPException(
        status_code=404,
        detail="No car found!"
    )


@app.put("/api/v1/cars/{id}")
async def updateCar(updateData: BrandUpdateMessage, id: UUID):
    if(cars is not None):
        selected: Car = None
        try:
            selected = next(item for item in cars if item.id == id)
        except StopIteration:
            pass

        if selected is not None:
            if updateData.name is not None:
                selected.name = updateData.name
            if updateData.desc is not None:
                selected.desc = updateData.desc
            if updateData.logo is not None:
                selected.logo = updateData.logo
            selected.updateDate = datetime.now()
            return ResponseMessage(
                status=00,
                message=SUCCESS,
                data=None
            )
    raise HTTPException(
        status_code=404,
        detail="No car found!"
    )
