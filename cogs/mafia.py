import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import os
import time
from datetime import datetime
from discord.ext.commands import has_permissions
import random
import json


class mafia(commands.Cog):

    def __init__(self, client):
        self.client = client

    
    @commands.command()
    async def p3(self, ctx):        
        embed = discord.Embed(
            title = 'نقش های پیشنهادی برای بازی',
            description = 'تعداد بازیکنان 3 نفر',
            colour = discord.Colour.red()        
        )

        embed.set_footer(text="Iranian Group", icon_url="https://cdn.discordapp.com/emojis/802808293734744104.gif?v=1")
        embed.set_image(url='https://cdn.discordapp.com/attachments/791275795037028363/802886639126052894/image.gif')
        embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/791275795037028363/795613597564272660/image.gif')
        embed.add_field(name='دان بدون تیر', value='1نفر', inline=False)
        embed.add_field(name='شهروند', value='2 نفر', inline=False)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/791275795037028363/795613597564272660/image.gif")
        embed.timestamp = datetime.utcnow()
        await ctx.send(embed=embed)
        await ctx.message.delete()


    @commands.command()
    async def p4(self, ctx):        
        embed = discord.Embed(
            title = 'نقش های پیشنهادی برای بازی',
            description = 'تعداد بازیکنان 4 نفر',
            colour = discord.Colour.red()        
        )

        embed.set_footer(text="Iranian Group", icon_url="https://cdn.discordapp.com/emojis/802808293734744104.gif?v=1")
        embed.set_image(url='https://cdn.discordapp.com/attachments/791275795037028363/802886639126052894/image.gif')
        embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/791275795037028363/795613597564272660/image.gif')
        embed.add_field(name='دان بدون تیر', value='1 نفر', inline=False)
        embed.add_field(name='شهروند', value='3 نفر', inline=False)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/791275795037028363/795613597564272660/image.gif")
        embed.timestamp = datetime.utcnow()
        await ctx.send(embed=embed)
        await ctx.message.delete()


    @commands.command()
    async def p5(self, ctx):        
        embed = discord.Embed(
            title = 'نقش های پیشنهادی برای بازی',
            description = 'تعداد بازیکنان 5 نفر',
            colour = discord.Colour.red()        
        )

        embed.set_footer(text="Iranian Group", icon_url="https://cdn.discordapp.com/emojis/802808293734744104.gif?v=1")
        embed.set_image(url='https://cdn.discordapp.com/attachments/791275795037028363/802886639126052894/image.gif')
        embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/791275795037028363/795613597564272660/image.gif')
        embed.add_field(name='دان', value='1', inline=False)
        embed.add_field(name='شهروند', value='4 نفر', inline=False)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/791275795037028363/795613597564272660/image.gif")
        embed.timestamp = datetime.utcnow()
        await ctx.send(embed=embed)
        await ctx.message.delete()

    @commands.command()
    async def p6(self, ctx):        
        embed = discord.Embed(
            title = 'نقش های پیشنهادی برای بازی',
            description = 'تعداد بازیکنان 6 نفر',
            colour = discord.Colour.red()        
        )

        embed.set_footer(text="Iranian Group", icon_url="https://cdn.discordapp.com/emojis/802808293734744104.gif?v=1")
        embed.set_image(url='https://cdn.discordapp.com/attachments/791275795037028363/802886639126052894/image.gif')
        embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/791275795037028363/795613597564272660/image.gif')
        embed.add_field(name='دان', value='1 نفر', inline=False)
        embed.add_field(name='پلیس خائن', value='1 نفر', inline=False)
        embed.add_field(name='دکتر', value='1 نفر', inline=False)
        embed.add_field(name='شهروند', value='3 نفر', inline=False)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/791275795037028363/795613597564272660/image.gif")
        embed.timestamp = datetime.utcnow()
        await ctx.send(embed=embed)
        await ctx.message.delete()


    @commands.command()
    async def p7(self, ctx):        
        embed = discord.Embed(
            title = 'نقش های پیشنهادی برای بازی',
            description = 'تعداد بازیکنان 7 نفر',
            colour = discord.Colour.red()        
        )

        embed.set_footer(text="Iranian Group", icon_url="https://cdn.discordapp.com/emojis/802808293734744104.gif?v=1")
        embed.set_image(url='https://cdn.discordapp.com/attachments/791275795037028363/802886639126052894/image.gif')
        embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/791275795037028363/795613597564272660/image.gif')
        embed.add_field(name='دان', value=' نفر1', inline=False)
        embed.add_field(name='پلیس خائن', value='1 نفر', inline=False)
        embed.add_field(name='شهروند', value='5 نفر', inline=False)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/791275795037028363/795613597564272660/image.gif")
        embed.timestamp = datetime.utcnow()
        await ctx.send(embed=embed)
        await ctx.message.delete()


    @commands.command()
    async def p8(self, ctx):        
        embed = discord.Embed(
            title = 'نقش های پیشنهادی برای بازی',
            description = 'تعداد بازیکنان 8 نفر',
            colour = discord.Colour.red()        
        )

        embed.set_footer(text="Iranian Group", icon_url="https://cdn.discordapp.com/emojis/802808293734744104.gif?v=1")
        embed.set_image(url='https://cdn.discordapp.com/attachments/791275795037028363/802886639126052894/image.gif')
        embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/791275795037028363/795613597564272660/image.gif')
        embed.add_field(name='دان', value='1 نفر', inline=False)
        embed.add_field(name='ترور', value='1 نفر', inline=False)
        embed.add_field(name='دکتر', value='1 نفر', inline=False)
        embed.add_field(name='کارآگاه', value='1 نفر', inline=False)
        embed.add_field(name='شهروند', value='4 نفر', inline=False)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/791275795037028363/795613597564272660/image.gif")
        embed.timestamp = datetime.utcnow()
        await ctx.send(embed=embed)
        await ctx.message.delete()
    

    @commands.command()
    async def p9(self, ctx):        
        embed = discord.Embed(
            title = 'نقش های پیشنهادی برای بازی',
            description = 'تعداد بازیکنان 9 نفر',
            colour = discord.Colour.red()        
        )

        embed.set_footer(text="Iranian Group", icon_url="https://cdn.discordapp.com/emojis/802808293734744104.gif?v=1")
        embed.set_image(url='https://cdn.discordapp.com/attachments/791275795037028363/802886639126052894/image.gif')
        embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/791275795037028363/795613597564272660/image.gif')
        embed.add_field(name='دان', value='1 نفر', inline=False)
        embed.add_field(name='مافیا ساده', value='2 نفر', inline=False)
        embed.add_field(name='دکتر', value='1 نفر', inline=False)
        embed.add_field(name='کارآگاه', value='1 نفر', inline=False)
        embed.add_field(name='شهروند', value='4 نفر', inline=False)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/791275795037028363/795613597564272660/image.gif")
        embed.timestamp = datetime.utcnow()
        await ctx.send(embed=embed)
        await ctx.message.delete()


    @commands.command()
    async def p10(self, ctx):        
        embed = discord.Embed(
            title = 'نقش های پیشنهادی برای بازی',
            description = 'تعداد بازیکنان 10 نفر',
            colour = discord.Colour.red()        
        )

        embed.set_footer(text="Iranian Group", icon_url="https://cdn.discordapp.com/emojis/802808293734744104.gif?v=1")
        embed.set_image(url='https://cdn.discordapp.com/attachments/791275795037028363/802886639126052894/image.gif')
        embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/791275795037028363/795613597564272660/image.gif')
        embed.add_field(name='دان', value='1 نفر', inline=False)
        embed.add_field(name='ترور', value='2 نفر', inline=False)
        embed.add_field(name='مافیا ساده', value='1 نفر', inline=False)
        embed.add_field(name='دکتر', value='1 نفر', inline=False)
        embed.add_field(name='کارآگاه', value='1 نفر', inline=False)
        embed.add_field(name='(1x) اسنایپر', value='1 نفر', inline=False)
        embed.add_field(name='شهروند', value='4 نفر', inline=False)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/791275795037028363/795613597564272660/image.gif")
        embed.timestamp = datetime.utcnow()
        await ctx.send(embed=embed)
        await ctx.message.delete()
    

    @commands.command()
    async def p11(self, ctx):        
        embed = discord.Embed(
            title = 'نقش های پیشنهادی برای بازی',
            description = 'تعداد بازیکنان 11 نفر',
            colour = discord.Colour.red()        
        )

        embed.set_footer(text="Iranian Group", icon_url="https://cdn.discordapp.com/emojis/802808293734744104.gif?v=1")
        embed.set_image(url='https://cdn.discordapp.com/attachments/791275795037028363/802886639126052894/image.gif')
        embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/791275795037028363/795613597564272660/image.gif')
        embed.add_field(name='دان', value='1 نفر', inline=False)
        embed.add_field(name='ترور', value='2 نفر', inline=False)
        embed.add_field(name='دکتر', value='1 نفر', inline=False)
        embed.add_field(name='کارآگاه', value='1 نفر', inline=False)
        embed.add_field(name='(2x) اسنایپر', value='1 نفر', inline=False)
        embed.add_field(name='شهروند', value='5 نفر', inline=False)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/791275795037028363/795613597564272660/image.gif")
        embed.timestamp = datetime.utcnow()
        await ctx.send(embed=embed)
        await ctx.message.delete()



    @commands.command()
    async def p12(self, ctx):        
        embed = discord.Embed(
            title = 'نقش های پیشنهادی برای بازی',
            description = 'تعداد بازیکنان 12 نفر',
            colour = discord.Colour.red()        
        )

        embed.set_footer(text="Iranian Group", icon_url="https://cdn.discordapp.com/emojis/802808293734744104.gif?v=1")
        embed.set_image(url='https://cdn.discordapp.com/attachments/791275795037028363/802886639126052894/image.gif')
        embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/791275795037028363/795613597564272660/image.gif')
        embed.add_field(name='دان', value='1 نفر', inline=False)
        embed.add_field(name='ترور', value='2 نفر', inline=False)
        embed.add_field(name='مافیا ساده', value='1 نفر', inline=False)
        embed.add_field(name='ناتاشا', value='1 نفر', inline=False)
        embed.add_field(name='دکتر', value='1 نفر', inline=False)
        embed.add_field(name='کارآگاه', value='1 نفر', inline=False)
        embed.add_field(name='(2x) اسنایپر', value='1 نفر', inline=False)
        embed.add_field(name='شهروند', value='4 نفر', inline=False)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/791275795037028363/795613597564272660/image.gif")
        embed.timestamp = datetime.utcnow()
        await ctx.send(embed=embed)
        await ctx.message.delete()









def setup(client):
    client.add_cog(mafia(client))