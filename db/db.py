import datetime
from pathlib import Path

import bson
from motor.motor_asyncio import AsyncIOMotorClient

import config

client = AsyncIOMotorClient(config.DB_URI)

db = client[config.DB_NAME]
collection = db[config.DB_COLLECTION_NAME]


async def ping_server():
    try:
        await client.admin.command('ping')
        print('MongoDB успешно подключен!')
    except Exception as e:
        print(e)


async def import_data():
    path_data = Path(__file__).parent.parent / 'data'

    if await collection.count_documents({}) == 0:
        with open(f'{path_data}/{config.DB_COLLECTION_NAME}.bson', 'rb') as f:
            data = bson.decode_all(f.read())

        try:
            result = await collection.insert_many(data)
            print(f'Импортировано документов: {len(result.inserted_ids)}')
        except Exception as e:
            print(e)


async def get_list_dates(dt_from: datetime, dt_upto: datetime) -> list:
    extract_data = collection.find({'dt': {'$gte': dt_from, '$lte': dt_upto}})
    return [day async for day in extract_data]
