from datetime import datetime

import pymongo
from beanie import Document, Indexed
from pydantic import BaseModel, Field
from typing import Optional

from app.server.models.geo import GeoType, GeoObject



class PropertyDeveloper(BaseModel):
    name: str
    description: str




class RetirementVillage(Document):
    name: str = Field(...)
    developer: PropertyDeveloper
    address: str = Field(...)
    geo: Indexed(GeoObject, index_type=pymongo.GEOSPHERE)
    latitude: float
    longitude: float
    description: str = Field(...)
    photos: list
    thumbnails: list
    service_charge: bool
    deferred_management_fee: bool
    purpose_built: bool
    callsystem: bool
    balconies: bool
    cafe_restaurant: bool
    bar: bool
    car_club: bool
    bus_service: bool
    cinema: bool
    gym: bool
    library: bool
    room_service: bool
    spa: bool
    parking: bool
    guest_parking: bool
    communal_lounge: bool
    gardens: bool
    courtyard: bool
    pets_allowed: bool
    salon: bool
    wheelchair_access: bool
    wifi_in_home: bool
    wifi_in_communal_areas: bool
    dateAmended: datetime = datetime.now()


    class Settings:
        name = "RetirementVillage"

    class Config:
        schema_extra = {
            "example": {
                "name": "The Orchards",
                "developer": {"name":"RVs are us", "description":"Fab Retirement Village"},
                "address": "xyz",
                "geo": "xyz",
                "latitude": 50.1,
                "longitude": 1.3,
                "description": "xyz",
                "photos": [],
                "thumbnails": [],
                "service_charge": True,
                "deferred_management_fee": True,
                "purpose_built": True,
                "callsystem": True,
                "balconies": True,
                "cafe_restaurant": True,
                "bar": True,
                "car_club": True,
                "bus_service": True,
                "cinema": True,
                "gym": True,
                "library": True,
                "room_service": True,
                "spa": True,
                "parking": True,
                "guest_parking": True,
                "communal_lounge": True,
                "gardens": True,
                "courtyard": True,
                "pets_allowed": True,
                "salon": True,
                "wheelchair_access": True,
                "wifi_in_home": True,
                "wifi_in_communal_areas": True,
                "dateAmended": "2022-05-17T13:53:17.196000"
            }
        }

class UpdateRetirementVillage(BaseModel):
    name: Optional[str]
    developer: Optional[PropertyDeveloper]
    address: Optional[str]
    geo: Optional[GeoObject]
    latitude: Optional[float]
    longitude: Optional[float]
    description: Optional[str]
    photos: Optional[list]
    thumbnails: Optional[list]
    service_charge: Optional[bool]
    deferred_management_fee: Optional[bool]
    purpose_built: Optional[bool]
    callsystem: Optional[bool]
    balconies: Optional[bool]
    cafe_restaurant: Optional[bool]
    bar: Optional[bool]
    car_club: Optional[bool]
    bus_service: Optional[bool]
    cinema: Optional[bool]
    gym: Optional[bool]
    library: Optional[bool]
    room_service: Optional[bool]
    spa: Optional[bool]
    parking: Optional[bool]
    guest_parking: Optional[bool]
    communal_lounge: Optional[bool]
    gardens: Optional[bool]
    courtyard: Optional[bool]
    pets_allowed: Optional[bool]
    salon: Optional[bool]
    wheelchair_access: Optional[bool]
    wifi_in_home: Optional[bool]
    wifi_in_communal_areas: Optional[bool]
    dateAmended: Optional[datetime]





    class Config:
        schema_extra = {
            "example": {
                "name": "The Orchards",
                "developer": "xyz",
                "address": "xyz",
                "geo": "xyz",
                "latitude": 50.1,
                "longitude": 1.3,
                "description": "xyz",
                "photos": [],
                "thumbnails": [],
                "service_charge": True,
                "deferred_management_fee": True,
                "purpose_built": True,
                "callsystem": True,
                "balconies": True,
                "cafe_restaurant": True,
                "bar": True,
                "car_club": True,
                "bus_service": True,
                "cinema": True,
                "gym": True,
                "library": True,
                "room_service": True,
                "spa": True,
                "parking": True,
                "guest_parking": True,
                "communal_lounge": True,
                "gardens": True,
                "courtyard": True,
                "pets_allowed": True,
                "salon": True,
                "wheelchair_access": True,
                "wifi_in_home": True,
                "wifi_in_communal_areas": True,
                "dateAmended": datetime.now()            }

        }






