import discord
import random
import json
import asyncio
import requests
import SubFunction
from io import BytesIO
from discord.ext import commands
from PIL import Image, ImageChops, ImageDraw, ImageFont

bgimg = 'https://media.discordapp.net/attachments/877375163786739722/885352314737680414/bossbase.png?width=1920&height=1080'
bossroom = 872033582653255710
bossdata = './Database/jrpg_boss.json'

class Boss(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
      print('JRPG PLAYER is working.')

    @commands.command()
    async def info(self, ctx, member: discord.Member):
        pass        

    @commands.command()
    async def attack(self, ctx, dmg: int):
        with open(bossdata,"r") as f:
                boss = json.load(f)
            

        boss["boss"]["hp"] = str (int(boss["boss"]["hp"]) - dmg)

        with open(bossdata,"w") as f:
                json.dump(boss, f)



def setup(client):
    client.add_cog(Boss(client))