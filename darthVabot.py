from discord.ext import commands

import LoadData
import parseCommand


class Bot(commands.Bot):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, command_prefix, intents):
        super().__init__(command_prefix, intents=intents)
        self._is_running = False

        # Adding all Cogs here
        self.add_cog(parseCommand.BaseCommand(self))

    def run(self, token, *args, **kwargs):
        if not self._is_running:
            self._is_running = True
            super().run(token, *args, **kwargs)
        else:
            print("Bot is already running.")
