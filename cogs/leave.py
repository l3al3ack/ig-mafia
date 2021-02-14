import discord
from discord.ext import commands

class join(commands.Cog):

    def __init__(self, client):
        self.client = client

    
    @commands.command(pass_context=True)
    async def leave(self, ctx):
        server = ctx.message.server
        voice_client = self.client.voice_client_in(server)
        await voice_client.disconnect()
    


def setup(client):
    client.add_cog(leave(client))




