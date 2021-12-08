import discord
import random
import json
from discord.ext import commands
from discord.ext.commands import has_permissions
from discord.ext.commands import CheckFailure

ans_ping = './Database/ping_answers.json'

class Ping(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
      print('Ping is working.')

    
    @commands.command()
    async def ping(self, ctx):
        answer = 'None'
        with open(ans_ping,"r") as f:
            ans_users = json.load(f)

        if str(ctx.author.id) in ans_users and len(ans_users[str(ctx.author.id)]) > 0:
            random_index = random.randint(1, len(ans_users[str(ctx.author.id)]))
            answer = ans_users[str(ctx.author.id)][str(random_index)]

        else:
            answer = [
                    'Tôi đang được bảo trì, nên đùng làm phiền!!',
                    'Không liên quan nhưng đồng chí đã like Fanpage SUITEAM chưa? https://www.facebook.com/mgk.transteam'
                ]
            answer = random.choice(answer)
        await ctx.send(answer)

        with open(ans_ping,"w") as f:
            json.dump(ans_users, f)


    @commands.command()
    @has_permissions(kick_members=True)
    async def addping(self, ctx, *args):
        with open(ans_ping,"r") as f:
            ans_users = json.load(f)

        answer = format(" ".join(args))
        if not str(ctx.author.id) in ans_users:
            ans_users[str(ctx.author.id)] = {}
        ans_users[str(ctx.author.id)][str(len(ans_users[str(ctx.author.id)])+1)] = answer
        await ctx.send("Done!!")
        # await ctx.send(str(len(ans_users[str(ctx.author.id)])+1))

        with open(ans_ping,"w") as f:
            json.dump(ans_users, f)
    @addping.error
    async def addping_error(self, ctx, error):
        if isinstance(error, CheckFailure):
            await ctx.send("Tôi chỉ nghe lệnh từ cấp trên!")

    
    @commands.command()
    async def listping(self, ctx):
        with open(ans_ping,"r") as f:
            ans_users = json.load(f)

        if not str(ctx.author.id) in ans_users:
            await ctx.send("Bạn chưa có câu trả lời riêng!!")
            return
        
        embed = discord.Embed(title='S.U.I Ping Setting',
                              description='-----',
                              colour=discord.Colour.blue())
        embed.set_thumbnail(url=ctx.author.avatar_url)
        for answer in ans_users[str(ctx.author.id)]:
            embed.add_field(name=f"{answer}: {ans_users[str(ctx.author.id)][str(answer)]}", value='---', inline=False)
        await ctx.send(embed=embed)

        with open(ans_ping,"w") as f:
            json.dump(ans_users, f)
        
    @commands.command()
    @has_permissions(kick_members=True)
    async def delping(self, ctx, delnum = 'None'):
        if delnum == "None":
            await ctx.send('Hãy điền số')
            return
        with open(ans_ping,"r") as f:
            ans_users = json.load(f)
        
        # del ans_users[str(ctx.author.id)][str(delnum)]

        i = int(delnum)

        # await ctx.send(len(ans_users[str(ctx.author.id)]))

        while i < len(ans_users[str(ctx.author.id)]):
            ans_users[str(ctx.author.id)][str(i)] = ans_users[str(ctx.author.id)][str(i+1)]
            # print(i)
            i += 1

        del ans_users[str(ctx.author.id)][str(len(ans_users[str(ctx.author.id)]))]

        await ctx.send('Done!!')

        with open(ans_ping,"w") as f:
            json.dump(ans_users, f)
    @delping.error
    async def delping_error(self, ctx, error):
        if isinstance(error, CheckFailure):
            await ctx.send("Tôi chỉ nghe lệnh từ cấp trên!")


def setup(client):
    client.add_cog(Ping(client))