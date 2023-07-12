from discord.ext import commands


class Utils(commands.Cog, name="Utils"):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx: commands.Context):
        """Check the bot latency"""
        latency = round(self.bot.latency * 1000)  # Latency in milliseconds
        await ctx.send(f"Pong ! Latency: {latency}ms")

    @commands.command()
    async def list_commands(self, ctx: commands.Context):
        """List all existing commands"""
        command_list = []
        for cog_name, cog in self.bot.cogs.items():
            for command in cog.get_commands():
                command_list.append(command.name)
        command_list.sort()  # Optional: Sort the command names alphabetically
        command_str = "\n".join(command_list)
        await ctx.send(f"List of commands:\n{command_str}")

    @commands.command()
    async def prune(self, ctx: commands.Context, num_messages: int):
        """Delete n messages"""
        await ctx.channel.purge(limit=num_messages + 1)


async def setup(bot: commands.Bot):
    await bot.add_cog(Utils(bot))
