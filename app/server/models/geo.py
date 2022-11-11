from pydantic import BaseModel, Field
from enum import Enum
from typing import Tuple



class GeoType(str, Enum):
    point = "Point"


class GeoObject(BaseModel):
    type: GeoType = GeoType.point
    coordinates: Tuple[float, float]