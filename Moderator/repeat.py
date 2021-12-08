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
      print('Kick is working.')

    
    @commands.command()
    # @has_permissions(kick_members=True)
    async def repeat(self, ctx, *args):
      mess = ctx.message
      await mess.delete()
      await ctx.send("{}".format(" ".join(args)))
    

def setup(client):
    client.add_cog(Repeat(client))