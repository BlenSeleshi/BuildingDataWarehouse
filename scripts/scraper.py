import os
import csv
import logging
from telethon import TelegramClient
from dotenv import load_dotenv

# Load environment variables
load_dotenv('.env')
api_id = os.getenv('TG_API_ID')
api_hash = os.getenv('TG_API_HASH')
phone = os.getenv('phone')

# Setup logging configuration
logging.basicConfig(
    filename='scraper.log', 
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s',
    filemode='a'  
)
logger = logging.getLogger()

# Function to scrape data from a single channel
async def scrape_channel(client, channel_username, writer, media_dir):
    try:
        entity = await client.get_entity(channel_username)
        channel_title = entity.title  # Extract the channel's title
        logger.info(f"Scraping channel: {channel_title} ({channel_username})")
        
        count = 0  # Track number of messages scraped
        async for message in client.iter_messages(entity, limit=10000):
            media_path = None
            if message.media and hasattr(message.media, 'photo'):
                # Create a unique filename for the photo
                filename = f"{channel_username}_{message.id}.jpg"
                media_path = os.path.join(media_dir, filename)
                # Download the media to the specified directory if it's a photo
                await client.download_media(message.media, media_path)
                # Log that the media was saved
                logger.info(f"Saved .jpg from message {message.id} to {media_path}")
            
            # Write the channel title along with other data
            writer.writerow([channel_title, channel_username, message.id, message.message, message.date, media_path])
            count += 1

        logger.info(f"Finished scraping {count} messages from {channel_username}")
    
    except Exception as e:
        logger.error(f"Error scraping {channel_username}: {e}")

# Initialize the client
client = TelegramClient('scraping_session', api_id, api_hash)

async def main():
    await client.start()
    
    # Create a directory for media files
    media_dir = 'photos'
    os.makedirs(media_dir, exist_ok=True)
    
    # Open the CSV file and prepare the writer
    with open('telegram_data.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Channel Title', 'Channel Username', 'ID', 'Message', 'Date', 'Media Path'])  # Include channel title in the header
        
        # List of channels to scrape
        channels = [
            '@anotherChannel',  # Add more channels as needed
            '@exampleChannel'
        ]
        
        # Iterate over channels and scrape data into the single CSV file
        for channel in channels:
            logger.info(f"Starting scraping for {channel}")
            await scrape_channel(client, channel, writer, media_dir)
            logger.info(f"Completed scraping for {channel}")

    logger.info("All channels scraped successfully")

# Run the scraping process
with client:
    client.loop.run_until_complete(main())
