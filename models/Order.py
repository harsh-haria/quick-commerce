from pydantic import BaseModel

from models.Address import Address

class Order(BaseModel):
    id: str
    user: str
    deliveryAddress: Address
    orderDate: str
    orderValue: float
    paymentMethod: str
    orderStatus: str
    invoice: str