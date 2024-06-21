import asyncio

from aiogram import Dispatcher, Bot

import config
from bot.handlers import router
from db import ping_server, import_data


dp = Dispatcher()
dp.include_router(router)


async def main():
    bot = Bot(token=config.BOT_TOKEN)
    await ping_server()
    await import_data()
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
