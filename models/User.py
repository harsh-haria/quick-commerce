from pydantic import BaseModel

from models.Address import Address

class Card(BaseModel):
    no: str
    expiryMonth: int
    expiryYear: int

class User(BaseModel):
    id: str | None = None
    firstName: str
    lastName: str
    mobileNo: list[str]
    address: list[Address]
    cart: list[str] | None = None
    cards: list[Card] | None = None
    pastOrders: list[str] | None = None
 
