import discord
import random
from discord.ext import commands
from hentai import Utils, Format, Sort



class Hentai(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Hentai is working.')

    @commands.command()
    async def re210(self, ctx):
        hentai = Utils.get_random_hentai()
        embed = discord.Embed(title='Công cụ recommend 210 cho anh em:>',
                              description=' ',
                              colour=discord.Colour.blue())
        embed.add_field(name='Tên', value=hentai.title(Format.Pretty), inline=False)
        embed.add_field(name='Link', value=hentai.url, inline=False)
        embed.set_image(url=hentai.image_urls[0])
        await ctx.send(embed=embed)       



def setup(client):
    client.add_cog(Hentai(client))