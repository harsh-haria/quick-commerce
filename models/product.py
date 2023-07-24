from pydantic import BaseModel

class ProductSize(BaseModel):
    length: float
    width: float
    height: float

class Review(BaseModel):
    id: str 
    title: str
    description: str
    rating: float
    date: str
    user: str | None = None
    images: list[str] | None = None

class Product(BaseModel):
    id: str | None = None
    title: str
    productDescription: str
    brand: str
    modelNo: str
    mrp: float
    costPrice: float
    sellingPrice: float
    seller: str
    countryOfOrigin: str
    genericName: str
    manufacturer: str
    sizeLength: ProductSize
    weight: float
    category: str
    dateFirstAvailable: str
    reviews: Review | None = None
    netQuantityAvailable: float
    netQuantityUnit: str
    categoryRank: int
    expirationDate: str
    isReturnable: bool
    vegNonveg: bool
    isCertified: bool
    extraDetailsBrand: str
    warehouse: str
    productImages: list[str]
