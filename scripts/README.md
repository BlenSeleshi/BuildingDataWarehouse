Here's a sample README file for your project that includes descriptions of the two scripts you provided. Feel free to customize any sections to better fit your project needs!

---

# Telegram Scraper and Data Importer

## Overview

This project consists of two main scripts: `scrapper.py` and `import_to_postgres.py`. The first script scrapes messages from specified Telegram channels and stores them in a CSV file. The second script imports this CSV file into a PostgreSQL database.

## Prerequisites

Before running the scripts, ensure you have the following installed:

- Python 3.x
- PostgreSQL
- Required Python packages (listed below)

## Installation

1. Clone this repository or download the scripts directly.
2. Create a `.env` file in the project root directory with the following environment variables:

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

3. Install the required Python packages:

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
```

## Scripts

### 1. `scrapper.py`

This script scrapes messages from specified Telegram channels and saves them into a CSV file.

#### How to Use:

1. Ensure your `.env` file is correctly configured with Telegram API credentials.
2. Modify the list of channels to scrape in the `main()` function if needed.
3. Run the script:

```bash
python scrapper.py
```

#### Output:

- A CSV file named `raw_data.csv` will be created in the same directory, containing the scraped data.

### 2. `export_csv_to_postgres.py`

This script imports the scraped data from the CSV file into a PostgreSQL database.

#### How to Use:

1. Ensure your `.env` file is correctly configured with PostgreSQL connection parameters.
2. Update the path of the CSV file in the script if necessary.
3. Run the script:

```bash
python import_to_postgres.py
```

#### Output:

- The data from `raw_data.csv` will be imported into a PostgreSQL table named `raw_data`. If the table already exists, it will be replaced.

## Logging

The `scrapper.py` script uses logging to keep track of the scraping process. The log will be saved in a file named `scraper.log`.

## Troubleshooting

- Ensure that the Telegram API credentials are correct and that the phone number is registered with Telegram.
- Verify that PostgreSQL is running and accessible with the provided connection parameters.
- Check the logs for any errors during the scraping or importing process.

## License

This project is licensed under the MIT License.

---

Feel free to modify this README file as needed to better fit your project or include any additional information that you think would be helpful for users!
