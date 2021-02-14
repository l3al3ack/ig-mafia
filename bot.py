import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import os
import json
from discord.ext.commands import has_permissions
import time
from datetime import datetime
import random


intents = discord.Intents.default()
# we need members intent too
intents.members = True

client = commands.Bot(command_prefix = '.m')
client.remove_command("announce")

@client.event
async def on_ready():
    print("the bot is online")



@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    

@client.command()
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')





@client.command(pass_context=True)  
@commands.has_permissions(manage_messages=True)  
async def mafia(ctx,*,message):  
    embed = discord.Embed(title="IRanian Management",description=message,color=0x330099)
    embed.set_footer(text="Iranian Group", icon_url="https://cdn.discordapp.com/emojis/802808293734744104.gif?v=1")
    embed.set_image(url="https://cdn.discordapp.com/attachments/791275795037028363/802808734220943370/623e1dc4b844631e7ac54f459bffb6e8.jpg")
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/788352938769907742/789092949177925642/240_F_122808000_C8VABpdNryTGS8Mip4iQ0LxpC2pvOtvQ.jpg")    
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/791275795037028363/795613597564272660/image.gif")
    embed.timestamp = datetime.utcnow()
    
    await ctx.send(embed=embed)
    await ctx.message.delete()


client.run(os.environ['token'])