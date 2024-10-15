# crud.py
from sqlalchemy.orm import Session
from models import TransformedTelegramData, ExtractedObjectsInfo

# Read data from TransformedTelegramData
def get_transformed_data(db: Session, skip: int = 0, limit: int = 10):
    return db.query(TransformedTelegramData).offset(skip).limit(limit).all()

# Read data from ExtractedObjectsInfo
def get_extracted_objects(db: Session, skip: int = 0, limit: int = 10):
    return db.query(ExtractedObjectsInfo).offset(skip).limit(limit).all()
    
