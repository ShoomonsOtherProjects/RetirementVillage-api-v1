from beanie import PydanticObjectId
from fastapi import APIRouter, HTTPException
from typing import List, Union
from bson.son import SON


from fastapi_pagination import Page, paginate, add_pagination


from app.server.models.retirement_village import RetirementVillage, UpdateRetirementVillage
from app.server.models.geo import  GeoObject

from app.server.models.interface_models import (

    StatusResponse,

    # PropertiesByWordInput,
    ResponseStatuses,
    RetirementVillageWithDistance,
    RetirementVillagesAroundInput
)
router = APIRouter()


##Retirement Villages###

@router.post("/", response_description="Retirement village added to the database")
async def add_retirement_village(retirementvillage: RetirementVillage) -> dict:
    await retirementvillage.create()
    return {"message": "Retirement Village added successfully"}

@router.get("/{id}", response_description="Retirement village record retrieved")
async def get_retirement_village_record(id: PydanticObjectId) -> RetirementVillage:
    retirementvillage = await RetirementVillage.get(id)
    return retirementvillage


@router.get("/", response_description="Retirement Village records retrieved")
async def get_retirement_villages() -> List[RetirementVillage]:
    retirementvillages = await RetirementVillage.find_all().to_list()
    return retirementvillages


@router.put("/{id}", response_description="Retirement Village record updated")
async def update_retirement_village_data(id: PydanticObjectId, req: UpdateRetirementVillage) -> RetirementVillage:
    req = {k: v for k, v in req.dict().items() if v is not None}
    update_query = {"$set": {
        field: value for field, value in req.items()
    }}

    review = await RetirementVillage.get(id)
    if not review:
        raise HTTPException(
            status_code=404,
            detail="Retirement Village record not found!"
        )

    await retirementvillage.update(update_query)
    return retirementvillage


@router.delete("/retirement_villages/{id}", response_description="Retirement Village record deleted from the database")
async def delete_retirement_village_data(id: PydanticObjectId) -> dict:
    record = await RetirementVillage.get(id)

    if not record:
        raise HTTPException(
            status_code=404,
            detail="Retirement Village record not found!"
        )

    await record.delete()
    return {
        "message": "Record deleted successfully"
    }



@router.post("/locationsearch", response_model=List[RetirementVillageWithDistance])
async def places_by_radius(input_data: RetirementVillagesAroundInput):
    point = GeoObject(coordinates=input_data.coordinates)
    print("point.dict(), input_data.radius, input_data.skip, input_data.limit")
    print(point.dict())
    print(input_data.radius)
    print(input_data.skip)
    print(input_data.limit)
    return await RetirementVillage.aggregate(
        [
            {
                "$geoNear": {
                    "near": point.dict(),
                    "distanceField": "distance",
                    "maxDistance": input_data.radius,
                }
            }
            ,
            {
                "$sort": SON([("_id", 1)])

            }
            ,
            {
                "$skip": input_data.skip
            }
            ,
            {
                "$limit": input_data.limit
            }
        ],
        projection_model=RetirementVillageWithDistance
    ).to_list()
