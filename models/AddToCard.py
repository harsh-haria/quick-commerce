from pydantic import BaseModel

class AddToCard(BaseModel):
    productId: str
    userId: str