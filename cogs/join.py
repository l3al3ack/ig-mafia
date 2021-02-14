import discord
from discord.ext import commands

class join(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        await self.client.change_presence(status=discord.Status.online, activity=discord.Activity(
            type=discord.ActivityType.playing, name="Iranian Group"
        ))
        print('Bot is online!')


    @commands.command(pass_context=True)
    async def join(self, ctx):
        channel = ctx.message.author.voice.voice_channel
        await self.client.join_voice_channel(channel)


def setup(client):
    client.add_cog(join(client))