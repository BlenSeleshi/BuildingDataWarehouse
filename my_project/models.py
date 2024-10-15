# models.py
from sqlalchemy import Column, String, Float, Integer
from database import Base

class TransformedTelegramData(Base):
    __tablename__ = 'transformed_telegram_data'

    # Example columns (replace with your actual product columns)
    products = Column(String, primary_key=True, index=True)

class ExtractedObjectsInfo(Base):
    __tablename__ = 'extracted_objects_info'

    image = Column(String, primary_key=True)
    name = Column(String, index=True)
    confidence = Column(Float)
    x_min = Column(Float)
    y_min = Column(Float)
    x_max = Column(Float)
    y_max = Column(Float)
