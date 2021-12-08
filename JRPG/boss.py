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
      print('JRPG BOSS is working.')
      

    @commands.command()
    async def addboss(self, ctx, member: discord.Member, hp = 0):
        if hp == 0:
            return

        name = str(member)
        name = name[0:len(name)-5]
        with open(bossdata,"r") as f:
                boss = json.load(f)

        boss["boss"]["name"] = name
        boss["boss"]["hp"] = str(hp)
        boss["boss"]["phase"] = 1
        boss["boss"]["ava"] = str(member.avatar_url_as(size=256))

        with open(bossdata,"w") as f:
                json.dump(boss, f)

    @commands.command()
    async def boss(self, ctx):
        loop = True
        while(loop == True):
            with open(bossdata,"r") as f:
                boss = json.load(f)

            name = boss["boss"]["name"]
            hp = boss["boss"]["hp"]
            phase = boss["boss"]["phase"]
            ava = boss["boss"]["ava"]

            if  phase == 1:
                name = f'Boss {name}'
            elif phase == 2:
                name = f'Boss {name} the Chaos'
            response = requests.get(bgimg)
            image_bytes = BytesIO(response.content)
            background = Image.open(image_bytes).convert("RGBA")

            draw = ImageDraw.Draw(background)
            font = ImageFont.truetype("./font/SVN-Nexa_Light.ttf",50)
            font2 = ImageFont.truetype("./font/SVN-Nexa_Light.ttf",200)

            response = requests.get(ava)
            image_bytes = BytesIO(response.content)
            pfp = Image.open(image_bytes).convert("RGBA")

            draw.text((40,647),name,font = font)
            draw.text((348,759),str(hp),font = font2)
            draw.text((1508,759),str(phase),font = font2)

            pfp = SubFunction.circle(pfp,(430,430))


            background.paste(pfp,(745,100),pfp)

            with BytesIO() as a:
                background.save(a,"PNG")
                a.seek(0)
                channel = self.client.get_channel(bossroom)
                await channel.send(file = discord.File(a,"profile.png"))

            with open(bossdata,"w") as f:
                json.dump(boss, f)
            await asyncio.sleep(10)



def setup(client):
    client.add_cog(Boss(client))