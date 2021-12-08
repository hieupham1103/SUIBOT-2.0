import discord
import random
import json
import SubFunction
from discord.ext import commands
from discord.ext.commands import has_permissions
from discord.ext.commands import CheckFailure

vanmaulist = './Database/vanmau.json'

class Vanmau(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
      print('Van Mau is working.')

    
    @commands.command()
    async def vanmau(self, ctx, member: discord.Member = 'None'):
        answer = 'None'

        if str(member) == 'None':
            member = ctx.author

        with open(vanmaulist,"r") as f:
            ans_users = json.load(f)

        if str(member.id) in ans_users and len(ans_users[str(member.id)]) > 0:
            random_index = random.randint(1, len(ans_users[str(member.id)]))
            answer = ans_users[str(member.id)][str(random_index)]

        else:
            answer = "Đồng chí này chưa có văn mẫu!!"
        await ctx.send(answer)

        with open(vanmaulist,"w") as f:
            json.dump(ans_users, f)


    @commands.command()
    async def addvanmau(self, ctx, *args):
        with open(vanmaulist,"r") as f:
            ans_users = json.load(f)

        answer = format(" ".join(args))
        if not str(ctx.author.id) in ans_users:
            ans_users[str(ctx.author.id)] = {}
        ans_users[str(ctx.author.id)][str(len(ans_users[str(ctx.author.id)])+1)] = answer
        await ctx.send("Done!!")
        # await ctx.send(str(len(ans_users[str(ctx.author.id)])+1))

        with open(vanmaulist,"w") as f:
            json.dump(ans_users, f)

    
    @commands.command()
    async def listvanmau(self, ctx, member: discord.Member = 'None'):
        if str(member) == 'None':
            member = ctx.author

        with open(vanmaulist,"r") as f:
            ans_users = json.load(f)

        if not str(member.id) in ans_users:
            await ctx.send("Bạn chưa có văn mẫu riêng!!")
            return
        
        embed = discord.Embed(title='S.U.I Van Mau Setting',
                              description='-----',
                              colour=discord.Colour.blue())
        embed.set_thumbnail(url=member.avatar_url)
        for answer in ans_users[str(member.id)]:
            vanmau = ans_users[str(member.id)][str(answer)]
            embed.add_field(name=f"{answer}: {vanmau[0:50]}", value='---', inline=False)
        await ctx.send(embed=embed)

        with open(vanmaulist,"w") as f:
            json.dump(ans_users, f)
        
    @commands.command()
    async def delvanmau(self, ctx, delnum = 'None'):
        if delnum == "None":
            await ctx.send('Hãy điền số')
            return
        with open(vanmaulist,"r") as f:
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

        with open(vanmaulist,"w") as f:
            json.dump(ans_users, f)


def setup(client):
    client.add_cog(Vanmau(client))