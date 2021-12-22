import discord
import random
import os
import json
from discord.ext import commands
from hentai import Utils, Format, Sort, Option, Path, Hentai


hentaipath = './Database/hentai_claim.json'

class nHentai(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Hentai checklist is working.')

    # @commands.command()
    # async def check210(self, ctx, code):
    #     with open(hentaipath,"r") as f:
    #         hentaiclaim = json.load(f)
    #     hentai = Hentai(code)
    #     # Hentai.exists(hentai.id)
    #     # print(hentai.title(Format.Pretty))
    #     embed = discord.Embed(title='Công cụ recommend 210 cho anh em:>',
    #                           description=' ',
    #                           colour=discord.Colour.blue())
    #     embed.add_field(name='Tên', value=hentai.title(Format.Pretty), inline=False)
    #     embed.add_field(name='Link', value=hentai.url, inline=False)
    #     embed.set_image(url=hentai.image_urls[0])
    #     if str(hentai.id) in hentaiclaim["history"]:
    #         embed.add_field(name='_____', value=f'<@{hentaiclaim["history"][str(hentai.id)]}> đã liếm bộ này', inline=False)
    #     await ctx.send(embed=embed)  
    #     with open(hentaipath,"w") as f:
    #         json.dump(hentaiclaim, f)   

    # @commands.command()
    # async def list210(self, ctx):
    #     with open(hentaipath,"r") as f:
    #         hentaiclaim = json.load(f)

    #     if not str(ctx.author.id) in hentaiclaim["user"]:
    #         await ctx.send("Bạn chưa liếm bộ nào!!")
    #         return
        
    #     embed = discord.Embed(title='S.U.I Liếm list',
    #                           description='-----',
    #                           colour=discord.Colour.blue())
    #     embed.set_thumbnail(url=ctx.author.avatar_url)
    #     user = "user"
    #     for hentai in hentaiclaim[user][str(ctx.author.id)]:
    #         embed.add_field(name=f'''{hentai}: {hentaiclaim[user][str(ctx.author.id)][str(hentai)]}''', value='---', inline=False)
    #     await ctx.send(embed=embed)

    #     with open(hentaipath,"w") as f:
    #         json.dump(hentaiclaim, f)  

def setup(client):
    client.add_cog(nHentai(client))