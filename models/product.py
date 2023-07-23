from pydantic import BaseModel

#model under construction :p
class Product(BaseModel):
    id: str | None = None
    title: str
    brand: str
    modelNo: str
    mrp: float
    costPrice: float
    sellingPrice: float
    seller: str
    countryOfOrigin: str
