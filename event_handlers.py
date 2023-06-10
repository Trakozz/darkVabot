import discord
from discord.ext import commands

import LoadData
import parseCommand
from main import darth_vabot


@darth_vabot.event
async def on_ready():
    print(f"Bot is ready. Logged in as {darth_vabot.user}")

    guild_name = 'Les apétarocissons'  # Replace with the name of your server (guild)
    channel_name = 'labo-holistique'  # Replace with the name of your text channel
    guild = discord.utils.get(darth_vabot.guilds, name=guild_name)
    channel = discord.utils.get(guild.channels, name=channel_name, type=discord.ChannelType.text)
    print('ready')
    if guild:

        if channel:
            print('toto is ready to rock')
            with open('vador.gif', 'rb') as file:
                await channel.send(content='DarkVa\'bot is here! YOU DON’T KNOW THE POWER OF THE DARK SIDE! ',
                                   file=discord.File(file, filename='darkvabot.gif'))
        else:
            print(f'Text channel not found: {channel_name}')
    else:
        print(f'Guild not found: {guild_name}')
    print(f'Logged in as {darth_vabot.user.name}')
    # Get the desired text channel by its ID
    text_channel = darth_vabot.get_channel(LoadData.data['laboHolistic'])
    if text_channel:
        print(f'Bot will send messages to: {channel.name}')
    else:
        print('Text channel not found.')

def setup(bot):
    pass  # Leave it empty if not using a Cog

@commands.Cog.listener()
async def on_message(darth_vabot, message):
    """
    Event handler for the on_message event.
    This function will be called when a message is sent in any server or DM where the bot can see it.
    """
    # Add your code to process the message here
    print('coucou')


@commands.Cog.listener()
async def on_command(darth_vabot, ctx):
    await print(ctx.command)
    if ctx.command.name == 'ping':
        await parseCommand.BaseCommand.ping()
    if ctx.command.name == "quote":
        await parseCommand.BaseCommand.quote()


async def on_member_join(darth_vabot, member):
    """
    Event handler for the on_member_join event.
    This function will be called when a new member joins a server where the bot is present.
    """
    # Add your code to handle the member joining here


async def on_member_remove(darth_vabot, member):
    """
    Event handler for the on_member_remove event.
    This function will be called when a member leaves or is removed from a server where the bot is present.
    """
    # Add your code to handle the member leaving here

# Add more event handlers as needed...


# You can also define helper functions or classes related to event handling if necessary
