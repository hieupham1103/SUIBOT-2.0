import discord
import os
from discord.ext import commands

class SPD(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
      print('SPD is working.')

    
    @commands.command()
    async def spd(self, ctx, *args):
      mess = ctx.message
      await mess.delete()
      await ctx.send(file=discord.File('./file/spd.jpg'))

def setup(client):
    client.add_cog(SPD(client))