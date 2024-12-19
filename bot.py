import asyncio
from db import create_table
from handlers import dp, bot  # Импортируем bot
from config import API_TOKEN

async def main():
    await create_table()
    await dp.start_polling(bot)  # Передаем bot в start_polling

if __name__ == "__main__":
    asyncio.run(main())
