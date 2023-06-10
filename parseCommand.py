import random

from discord.ext import commands

import LoadData


class BaseCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        latency = round(self.bot.latency * 1000)  # Latency in milliseconds
        await ctx.send(f"Pong ! Latency: {latency}ms")

    @commands.command()
    async def quote(self, channel):
        await channel.send(content=LoadData.quotes[str(random.randint(1, len(LoadData.quotes)))])

