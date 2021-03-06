import discord
import json
from discord.ext import commands
from discord_together import DiscordTogether


with open("./config.json","r") as f:
    config = json.load(f)

class YT(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        self.togetherControl = await DiscordTogether(config["bottoken"])
        print('YT is working.')
    
    @commands.command()
    async def startYT(self,ctx):
        link = await self.togetherControl.create_link(ctx.author.voice.channel.id, 'youtube')
        await ctx.send(f"ẤN VÀO ĐỂ YT GO BỦBỦ!!\n{link}")
    
    @commands.command()
    async def startPO(self,ctx):
        link = await self.togetherControl.create_link(ctx.author.voice.channel.id, 'poker')
        await ctx.send(f"ẤN VÀO ĐỂ POKẺ GO BỦBỦ!!\n{link}")

    @commands.command()
    async def startCH(self,ctx):
        link = await self.togetherControl.create_link(ctx.author.voice.channel.id, 'chess')
        await ctx.send(f"ẤN VÀO ĐỂ CỜ DUA GO BỦBỦ!!\n{link}")

    @commands.command()
    async def startAM(self,ctx):
        link = await self.togetherControl.create_link(ctx.author.voice.channel.id, 'betrayal')
        await ctx.send(f"ẤN VÀO ĐỂ CHƠI AMOG SÚ GO BỦBỦ!!\n{link}")
    
    @commands.command()
    async def startFI(self,ctx):
        link = await self.togetherControl.create_link(ctx.author.voice.channel.id, 'fishing')
        await ctx.send(f"ẤN VÀO ĐỂ GIẢ LẬP NGƯ DÂN NHA TRANG GO BỦBỦ!!\n{link}")
    
    @commands.command()
    async def startSC(self,ctx):
        link = await self.togetherControl.create_link(ctx.author.voice.channel.id, 'spellcast')
        await ctx.send(f"ẤN VÀO ĐỂ NỐI TỪ GO BỦBỦ!!\n{link}")
    

def setup(client):
    client.add_cog(YT(client))