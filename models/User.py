from pydantic import BaseModel

from Address import Address

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
    cart: list[str]
    cards: list[Card]
    pastOrders: list[str]
 
