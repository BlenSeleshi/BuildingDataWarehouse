# schemas.py
from pydantic import BaseModel
from typing import Optional

class TransformedTelegramData(BaseModel):
    products: str
    
    class Config:
        orm_mode = True

class ExtractedObjectsInfo(BaseModel):
    image: str
    name: str
    confidence: float
    x_min: float
    y_min: float
    x_max: float
    y_max: float

    class Config:
        orm_mode = True
