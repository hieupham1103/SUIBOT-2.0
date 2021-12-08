import discord
import randomstuff
from discord.ext import commands

rsapi = 'r7CpEtWxeFEg'
rs = randomstuff.Client(api_key=rsapi)


class ChatAI(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('ChatAI is working.')

    @commands.command()
    async def chat(self, ctx, *,msg: str):
        answer = rs.get_ai_response(msg,
                                    name='Secret Universe Investigation Organization',
                                    age="12",
                                    master='HieeuSPhamJ',
                                    location='Viet Nam',
                                    birth_year='2009',
                                    email='phamdinhtrunghieu1103@gmail.com',
                                    company='Secret Universe Investigation Organization',
                                    birth_place='Viet Nam',
                                    gender = 'female'
        )
        await ctx.send(answer.message)




def setup(client):
    client.add_cog(ChatAI(client))