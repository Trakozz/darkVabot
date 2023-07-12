import pyaudio
import wave
from discord.ext import commands
import discord


class Audio(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def audioRec(self, ctx):
        # Set the audio parameters
        format = pyaudio.paInt16
        channels = 1
        sample_rate = 44100
        chunk = 1024
        record_seconds = 5
        output_file = "recorded_audio.wav"

        # Initialize the audio stream
        audio = pyaudio.PyAudio()
        stream = audio.open(format=format,
                            channels=channels,
                            rate=sample_rate,
                            input=True,
                            frames_per_buffer=chunk)

        # Record audio
        frames = []
        for i in range(0, int(sample_rate / chunk * record_seconds)):
            data = stream.read(chunk)
            frames.append(data)

        # Stop the audio stream
        stream.stop_stream()
        stream.close()
        audio.terminate()

        # Save audio to file
        with wave.open(output_file, 'wb') as wf:
            wf.setnchannels(channels)
            wf.setsampwidth(audio.get_sample_size(format))
            wf.setframerate(sample_rate)
            wf.writeframes(b''.join(frames))

        print(f"Audio saved as: {output_file}")


async def setup(bot):
    await bot.add_cog(Audio(bot))