import discord
from discord.ext import commands

import LoadData
import event_handlers


def set_intents():
    intents = discord.Intents.default()
    intents.typing = False
    intents.message_content = True
    return intents


darth_vabot = commands.Bot(command_prefix=LoadData.data['prefix'], intents=set_intents())


def run_bot():
    bot_instance = darth_vabot
    bot_instance.run(LoadData.data['token'])


run_bot()

# async def on_message(message):
#     print(message.author)
#     print(darthVabot.user)
#     if message.author == darthVabot.user:
#         return
#
#     if message.content.startswith('!hello'):
#         print('on_message')
#         await parseCommand.BaseCommand.quote(message.channel)
