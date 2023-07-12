import discord
from discord.ext import commands
import LoadData
import logging

def set_intents():
    intents = discord.Intents.all()
    return intents


class Bot(commands.Bot):
    def __init__(self):
        super().__init__(LoadData.data['prefix'], intents=set_intents())

    async def on_ready(self):
        channel_name = 'labo-holistique'  # Replace with the name of your text channel
        channel = discord.utils.get(self.get_all_channels(), name=channel_name)
        print(channel.id)
        if channel:
            with open('vador.gif', 'rb') as file:
                await channel.send(content='DarkVa\'bot is here! YOU DON’T KNOW THE POWER OF THE DARK SIDE! ',
                                   file=discord.File(file, filename='darkvabot.gif'))
        else:
            print(f'Text channel not found: {channel_name}')
        print(f'Bot is ready. Logged in as  {self.user.name} ({self.user.id})')

    # async def print_registered_commands(self):
    #     await self.wait_until_ready()  # Wait until the bot is ready
    #     for command in self.walk_commands():
    #         print(command.name)
