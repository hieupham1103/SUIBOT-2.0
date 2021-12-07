import discord
import json
from PIL import Image, ImageChops, ImageDraw, ImageFont


mod = 901421416887496741

def circle(pfp,size = (215,215)):
    
    pfp = pfp.resize(size, Image.ANTIALIAS).convert("RGBA")
    
    bigsize = (pfp.size[0] * 3, pfp.size[1] * 3)
    mask = Image.new('L', bigsize, 0)
    draw = ImageDraw.Draw(mask) 
    draw.ellipse((0, 0) + bigsize, fill=255)
    mask = mask.resize(pfp.size, Image.ANTIALIAS)
    mask = ImageChops.darker(mask, pfp.split()[-1])
    pfp.putalpha(mask)
    return pfp

def rolefilter(ctx, member: discord.Member):
    guild = ctx.guild
    if discord.utils.get(guild.roles, id=mod) in member.roles:
        role = 'MOD'
    else:
        role = 'THƯỜNG DÂN'
    return role

def bgfilter(member):
    background = Image.open("./file/profilecard.png").convert("RGBA")

    with open("./Database/background.json","r") as f:
      bgs = json.load(f)
      
    if str(member.id) in bgs:
        if bgs[str(member.id)] == "1":
            background = Image.open("./file/profilecard.png").convert("RGBA")
        if bgs[str(member.id)] == "2":
            background = Image.open("./file/profilecard2.png").convert("RGBA")
        if bgs[str(member.id)] == "3":
            background = Image.open("./file/profilecard3.png").convert("RGBA")
        if bgs[str(member.id)] == "4":
            background = Image.open("./file/profilecard4.png").convert("RGBA")
        if bgs[str(member.id)] == "5":
            background = Image.open("./file/profilecard5.png").convert("RGBA")

    with open("./Database/background.json","w") as f:
        json.dump(bgs, f)

    return background
