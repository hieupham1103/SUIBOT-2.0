import discord
import random
import asyncio
import json
from discord.ext import commands
import hentai
from hentai import Utils, Format, Sort, Hentai

hentaipath = './Database/hentai_claim.json'

class Hentai(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Hentai Gacha is working.')

    @commands.command()
    # @commands.cooldown(rate=1, per=30)
    async def re210(self, ctx):
        # with open(hentaipath,"r") as f:
        #     hentaiclaim = json.load(f)
        hentai = Utils.get_random_hentai()

        embed = discord.Embed(title='Công cụ recommend 210 cho anh em:>',
                              description=' ',
                              colour=discord.Colour.blue())
        embed.add_field(name='Tên', value=hentai.title(Format.Pretty), inline=False)
        embed.add_field(name='Link', value=hentai.url, inline=False)
        embed.set_image(url=hentai.image_urls[0])
        # if str(hentai.id) in hentaiclaim["history"]:
        #     embed.add_field(name='_____', value=f'<@{hentaiclaim["history"][str(hentai.id)]}> đã liếm bộ này', inline=False)
        mess = await ctx.send(embed=embed)  
        # with open(hentaipath,"w") as f:
        #     json.dump(hentaiclaim, f)   
        # # mess = await ctx.send('TEST')


        # def check_react(reaction, user):
        #     if reaction.message.id != mess.id:
        #         return False
        #     if user != ctx.message.author:
        #         return False
        #     return True
            
        # try:
        #     react, user = await self.client.wait_for('reaction_add', check=check_react, timeout=10)

        # except asyncio.TimeoutError:
        #     pass
        #     # print('timeout')
        # else:
        #     with open(hentaipath,"r") as f:
        #         hentaiclaim = json.load(f)
            
        #     if not str(hentai.id) in hentaiclaim["history"]:
        #         if not str(user.id) in hentaiclaim["user"]:
        #             hentaiclaim["user"][str(user.id)] = {}
        #         hentaiclaim["history"][str(hentai.id)] = str(user.id)
        #         hentaiclaim["user"][str(user.id)][str(len(hentaiclaim["user"][str(user.id)])+1)] = hentai.id



        #         await ctx.send(f'{user.mention} đã liếm bộ {hentai.id} :>>>')

        #     else:
        #         await ctx.send(f'{hentai.id} đã bị liếm bởi {hentaiclaim["history"][str(hentai.id)]}:>')

        #     with open(hentaipath,"w") as f:
        #         json.dump(hentaiclaim, f)
                
    # @re210.error
    # async def re210_error(self, ctx: commands.Context, error):
    #     if isinstance(error, commands.CommandOnCooldown):
    #         await ctx.send(f"Đợi {round(error.retry_after)}s")
            





def setup(client):
    client.add_cog(Hentai(client))