from enum import Enum
from typing import Tuple, Optional

from pydantic.main import BaseModel

from app.server.models.retirement_village import  RetirementVillage


class ResponseStatuses(str, Enum):
    OK = "OK"


class StatusResponse(BaseModel):
    status: ResponseStatuses


# class PropertiesByWordInput(BaseModel):
#     search_words: str
#     skip: Optional[int] = None
#     limit: Optional[int] = None





class RetirementVillagesAroundInput(BaseModel):
    coordinates: Tuple[float, float]
    text_location: str
    radius: float = 1000
    skip: int
    limit: int


class RetirementVillageWithDistance(RetirementVillage):
    distance: float