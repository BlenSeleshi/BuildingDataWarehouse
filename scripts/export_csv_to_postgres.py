import os
import psycopg2
import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine
import csv

# Load environment variables from .env file
load_dotenv(r'C:\Users\Blen\OneDrive\Desktop\10Academy\BuildingDataWarehouse\.env')

# Fetch database connection parameters from environment variables
DB_HOST = os.getenv("DB_HOST").strip()
DB_PORT = os.getenv("DB_PORT").strip()
DB_NAME = os.getenv("DB_NAME").strip()
DB_USER = os.getenv("DB_USER").strip()
DB_PASSWORD = os.getenv("DB_PASSWORD").strip()

def create_table(table_name):
    """
    Create a table in PostgreSQL based on the CSV structure.
    
    :param table_name: Name of the target table.
    """
    try:
        # Establish a connection to the database
        connection = psycopg2.connect(
            host=DB_HOST,
            port=int(DB_PORT),
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )

        # Create cursor object
        cur = connection.cursor()

        # SQL query to create the table
        create_table_query = f"""
        CREATE TABLE IF NOT EXISTS {table_name} (
            id SERIAL PRIMARY KEY,
            channel_title VARCHAR(255),
            channel_username VARCHAR(255),
            message_id BIGINT,
            message TEXT,
            date TIMESTAMPTZ
        );
        """
        
        # Execute the table creation query
        cur.execute(create_table_query)

        print(f"Table '{table_name}' created successfully.")

        # Commit changes
        connection.commit()
        cur.close()
        connection.close()

    except Exception as e:
        print(f"An error occurred while creating the table: {e}")

def import_csv_to_postgres(csv_file_path, table_name):
    """
    Import CSV file to PostgreSQL table.

    :param csv_file_path: Path to the CSV file.
    :param table_name: Name of the target table.
    """
    try:
        # Establish a connection to the database
        connection = psycopg2.connect(
            host=DB_HOST,
            port=int(DB_PORT),
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )

        # Open CSV file and load into a DataFrame
        df = pd.read_csv(csv_file_path, encoding='utf-8', quoting=csv.QUOTE_ALL, escapechar='\\')

        # Ensure DataFrame column names match the table columns
        df.columns = ['channel_title', 'channel_username', 'message_id', 'message', 'date']
        
        # Create SQLAlchemy engine to facilitate DataFrame to SQL
        engine = create_engine(f'postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}')
        
        # Write the DataFrame to the specified table in PostgreSQL
        df.to_sql(table_name, engine, if_exists='replace', index=False)
        
        print(f"CSV file '{csv_file_path}' imported successfully into '{table_name}' table")

    except Exception as e:
        print(f"An error occurred during CSV import: {e}")

    finally:
        if connection:
            connection.close()

# Set function parameters
csv_file_path = r'C:\Users\Blen\OneDrive\Desktop\10Academy\BuildingDataWarehouse\data\cleaned_data.csv'
table_name = 'raw_data'

# Create the table and import CSV data
create_table(table_name)
import_csv_to_postgres(csv_file_path, table_name)
