import discord
import json
from SubFunction import circle, rolefilter, bgfilter
from discord.ext import commands
from io import BytesIO
from PIL import Image, ImageChops, ImageDraw, ImageFont

class Profile(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
      print('Profile is working.')

    @commands.command()
    async def setbg(self, ctx, index):
        if int(index) > 5:
          await ctx.send("Hiện tại chỉ có BG từ 1 đến 5")
          return
        with open("./Database/background.json","r") as f:
          bgs = json.load(f)

        member = ctx.author
        bgs[str(member.id)]=index

        await ctx.send("DONE!!!")

        with open("./Database/background.json","w") as f:
          json.dump(bgs, f)


    @commands.command()
    async def info(self, ctx, member: discord.Member = 'None'):
        if member == 'None':
          member = ctx.author

        role = rolefilter(ctx,member)
        name = str(member)
        joined = member.joined_at.strftime("%b %Y")
        # base = Function.basefilter(member)
        background = bgfilter(member)
        base = bgfilter(member)
        # base = Image.open("./file/profilecard4.png").convert("RGBA")
        draw = ImageDraw.Draw(base)
        font = ImageFont.truetype("./font/SVN-Nexa_Light.ttf",44)

        pfp = member.avatar_url_as(size=256)
        data = BytesIO(await pfp.read())
        pfp = Image.open(data).convert("RGBA")
        name = f"{name[:20]}.." if len(name)>20 else name

        pfp = circle(pfp,(215,215))

        draw.text((340,200),name,font = font)
        draw.text((564,314),role,font = font)
        draw.text((544,561),joined,font = font)

        base.paste(pfp,(56,158),pfp)
        background.paste(base,(0,0),base)

        with BytesIO() as a:
          background.save(a,"PNG")
          a.seek(0)
          await ctx.send(file = discord.File(a,"profile.png"))

    

def setup(client):
    client.add_cog(Profile(client))