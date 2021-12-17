import discord
import os
import random
from discord.ext import commands
from discord.ext.commands import has_permissions

author = 480729328175415296

class Repeat(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
      print('Dev is working.')

    @commands.command()
    async def send(self,ctx, member: discord.Member):
        if ctx.author.id == author:
            while True:
                channel = await member.create_dm()
                await channel.send("ĐẤM NHAU KO!!! :gun~1:")
      
    

def setup(client):
    client.add_cog(Repeat(client))