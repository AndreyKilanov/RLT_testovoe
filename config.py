from dotenv import load_dotenv
import os

load_dotenv(dotenv_path='infra/.env')

# Bot settings
BOT_TOKEN = os.getenv("BOT_TOKEN")

# DB sittings
DB_ADMIN_NAME = os.getenv("DB_ADMIN_NAME")
DB_ADMIN_PASSWORD = os.getenv("DB_ADMIN_PASSWORD")
DB_NAME = os.getenv("DB_NAME")
DB_COLLECTION_NAME = os.getenv("DB_COLLECTION_NAME")
# if used locally
# DB_URI = f'mongodb://{DB_ADMIN_NAME}:{DB_ADMIN_PASSWORD}@localhost:27017/'
# if used in docker
DB_URI = f'mongodb://{DB_ADMIN_NAME}:{DB_ADMIN_PASSWORD}@mongo:27017/'
