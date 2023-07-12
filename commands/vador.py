from time import sleep

from discord.ext import commands
import discord
import asyncio
import os


class Vador(commands.Cog, name="Vador"):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def talk(self, ctx: commands.Context, *, text: str):
        """Make the bot say a given text prompt"""
        await ctx.message.delete()  # Delete the command message
        await ctx.send(text)  # Send the text as a response

    @commands.command()
    async def play(self, ctx: commands.Context):
        """Make the bot play an audio file"""
        # Check if the user is in a voice channel
        if not ctx.author.voice:
            await ctx.send("You are not connected to a voice channel.")
            return

        # Get the voice channel of the user
        voice_channel = ctx.author.voice.channel

        # Check if the bot is already in a voice channel
        if ctx.voice_client:
            await ctx.voice_client.move_to(voice_channel)
        else:
            # Connect to the voice channel
            try:
                voice_client = await voice_channel.connect()
            except discord.Forbidden:
                await ctx.send("I don't have permission to join the voice channel.")
                return
            except discord.ClientException:
                await ctx.send("I'm already in a voice channel.")
                return
            except Exception as e:
                await ctx.send(f"An error occurred while joining the voice channel: {e}")
                return

                # Play the audio file
            current_dir = os.path.dirname(os.path.abspath(__file__))
            audio_file = os.path.join(current_dir, '../audios/audio.wav')
            source = discord.FFmpegPCMAudio(audio_file)
            ctx.voice_client.play(source)

            # Wait for the audio to finish playing
            while ctx.voice_client.is_playing():
                await asyncio.sleep(1)

            # Disconnect from the voice channel
            await ctx.voice_client.disconnect()

    async def disconnect(self, ctx: commands.Context):
        if ctx.voice_client and ctx.voice_client.is_connected():
            await ctx.voice_client.disconnect()
            self.bot.voice_client = None


async def setup(bot: commands.Bot):
    await bot.add_cog(Vador(bot))
