# Building a Data Warehouse for Ethiopian Medical Business Data

## Overview

This project aims to build a data warehouse to store and manage data related to Ethiopian medical business information scraped from Telegram channels. The project consists of multiple scripts and notebooks that facilitate data collection, processing, and serving through an API.

## Table of Contents

- [Installation](#installation)
- [Telegram Scraper](#telegram-scraper)
  - [Requirements](#requirements)
  - [Scripts](#scripts)
    - [1. `scrapper.py`](#1-scrapperpy)
    - [2. `export_csv_to_postgres.py`](#2-export_csv_to_postgrespy)
- [YOLO Implementation](#yolo-implementation)
  - [Removing Duplicate Images](#removing-duplicate-images)
  - [Object Detection](#object-detection)
  - [Saving Detection Information](#saving-detection-information)
- [Exporting Data to PostgreSQL](#exporting-data-to-postgresql)
- [FastAPI Integration](#fastapi-integration)
- [Usage](#usage)
- [Logging](#logging)
- [Troubleshooting](#troubleshooting)

## Installation

To set up the project environment, follow these steps:

1. Clone the repository:

   ```bash
   git clone <repository_url>
   cd <repository_name>
   ```

2. Create a virtual environment and activate it:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Create a `.env` file in the project root directory with the following environment variables:

   ```plaintext
   # Telegram API credentials
   TG_API_ID=<your_api_id>
   TG_API_HASH=<your_api_hash>
   phone=<your_phone_number>

   # PostgreSQL connection parameters
   DB_HOST=<your_db_host>
   DB_PORT=<your_db_port>
   DB_NAME=<your_db_name>
   DB_USER=<your_db_user>
   DB_PASSWORD=<your_db_password>
   ```

4. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

   **Note:** Create a `requirements.txt` file with the following dependencies:

   ```plaintext
   pandas
   psycopg2
   sqlalchemy
   python-telegram-api
   python-dotenv
   torch
   opencv-python
   fastapi
   uvicorn
   ```

## Telegram Scraper

### Requirements

Before running the Telegram scraper, ensure you have the required packages installed, as outlined in the Installation section.

### Scripts

#### 1. `scrapper.py`

This script scrapes messages from specified Telegram channels and saves them into a CSV file.

**How to Use:**

1. Ensure your `.env` file is correctly configured with Telegram API credentials.
2. Modify the list of channels to scrape in the `main()` function if needed.
3. Run the script:

   ```bash
   python scrapper.py
   ```

**Output:**

- A CSV file named `raw_data.csv` will be created in the same directory, containing the scraped data.

#### 2. `export_csv_to_postgres.py`

This script imports the scraped data from the CSV file into a PostgreSQL database.

**How to Use:**

1. Ensure your `.env` file is correctly configured with PostgreSQL connection parameters.
2. Update the path of the CSV file in the script if necessary.
3. Run the script:

   ```bash
   python export_csv_to_postgres.py
   ```

**Output:**

- The data from `raw_data.csv` will be imported into a PostgreSQL table named `raw_data`. If the table already exists, it will be replaced.

## YOLO Implementation

### Removing Duplicate Images

This script removes duplicate images based on their file size to maintain data quality.

```python
def remove_duplicate_images_by_size(folder_path):
    # Function implementation
```

### Object Detection

We use a pre-trained YOLOv5 model to detect objects in images.

```python
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')
for img_name in os.listdir(image_folder):
    # Object detection implementation
```

### Saving Detection Information

Detection results are consolidated into a CSV file for further processing.

```python
all_detections.to_csv('all_detections.csv', index=False)
```

## Exporting Data to PostgreSQL

The extracted data is transformed and exported to a PostgreSQL database.

```python
load_dotenv()
connection_string = f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'
engine = create_engine(connection_string)
filtered_df.to_sql('extracted_objects_info', engine, if_exists='replace', index=False)
```

## FastAPI Integration

The FastAPI application exposes the collected data through API endpoints.

### Creating the FastAPI Application

```python
app = FastAPI()

@app.get("/extracted_objects/")
def read_extracted_objects(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_extracted_objects(db, skip=skip, limit=limit)
```

## Usage

1. Start the FastAPI server:

   ```bash
   uvicorn main:app --reload
   ```

2. Access the API documentation at `http://127.0.0.1:8000/docs`.

3. Use the API to retrieve extracted object data from the PostgreSQL database.

## Logging

The `scrapper.py` script uses logging to keep track of the scraping process. The log will be saved in a file named `scraper.log`.

## Troubleshooting

- Ensure that the Telegram API credentials are correct and that the phone number is registered with Telegram.
- Verify that PostgreSQL is running and accessible with the provided connection parameters.
- Check the logs for any errors during the scraping or importing process.
