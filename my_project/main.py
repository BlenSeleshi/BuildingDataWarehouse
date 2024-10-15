# main.py
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db, engine
import models, crud, schemas

# Create the database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Get transformed telegram data
@app.get("/transformed_data/", response_model=list[schemas.TransformedTelegramData])
def read_transformed_data(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    data = crud.get_transformed_data(db, skip=skip, limit=limit)
    return data

# Get extracted objects info
@app.get("/extracted_objects/", response_model=list[schemas.ExtractedObjectsInfo])
def read_extracted_objects(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    objects = crud.get_extracted_objects(db, skip=skip, limit=limit)
    return objects
