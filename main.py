import asyncio

import LoadData
from darthVabot import Bot
import logging


async def main():
    # Configure logging
    logging.basicConfig(level=logging.DEBUG)
    logging.getLogger('discord').setLevel(logging.DEBUG)

    bot = Bot()
    try:
        await bot.load_extension('commands.utils.utils')
        await bot.load_extension('commands.vador')
        await bot.load_extension('commands.moderation.moderation')
        print('Cogs loaded successfully')
    except Exception as e:
        print(f'Failed to load cogs: {e}')
    try:
        await bot.start(LoadData.data['token'])
    except KeyboardInterrupt:
        await bot.close()

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot stopped manually.")