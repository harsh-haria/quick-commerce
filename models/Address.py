from pydantic import BaseModel

class Address(BaseModel):
    room: str
    floor: str
    building: str
    road: str
    landmark: str
    