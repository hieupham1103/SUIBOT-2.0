import discord
import os
import random
from discord.ext import commands
from discord.ext.commands import has_permissions


class Repeat(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
      print('REPEAT is working.')

    
    @commands.command()
    async def slaveoff(self, ctx):
        await ctx.send("Chế độ nô lệ: disable")

    @commands.command()
    async def slaveon(self, ctx):
        await ctx.send("Chế độ nô lệ: enable")

      
    

def setup(client):
    client.add_cog(Repeat(client))