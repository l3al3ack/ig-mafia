import discord
from discord.ext import commands
from discord.utils import get

class join(commands.Cog):

    def __init__(self, client):
        self.client = client

    
    @commands.command(pass_context=True, aliases=['j', 'joi'])
    async def join(self, ctx):
        channel = ctx.message.author.voice.channel
        voice = get(self.client.voice_clients, guild=ctx.guild)

        if voice and voice.is_connected():
            await voice.move_to(channel)
        else:
            voice = await channel.connect()

        await voice.disconnect()

        if voice and voice.is_connected():
            await voice.move_to(channel)
        else:
            voice = await channel.connect()
            print(f"The bot has connected to {channel}\n")

        await ctx.send(f"Joined {channel}")


def setup(client):
    client.add_cog(join(client))