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
            await voice.disconnect()
            print(f"The bot has left {channel}")
            await ctx.send(f"Left {channel}")
        else:
            print("Bot was told to leave voice channel, but was not in one")
            await ctx.send("Don't think I am in a voice channel")
        


def setup(client):
    client.add_cog(join(client))