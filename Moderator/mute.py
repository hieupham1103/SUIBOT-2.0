import discord
import asyncio
from discord.ext import commands
from discord.ext.commands import has_permissions
from discord.ext.commands import CheckFailure

tunhan = 762694968930074644
mutechannel = 784235323781152769

class Mute(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
      print('Mute is working.')

    #s+mute
    @commands.command()
    @has_permissions(manage_messages=True)
    async def mute(self, ctx, member: discord.Member, time='___',*, reason: str = '___'):
        guild = ctx.guild
        mutedRole = discord.utils.get(guild.roles, id=tunhan)
        time_convert = {"s": 1, "m": 60, "h": 3600, "d": 86400}
        if time == '___':
            await member.add_roles(mutedRole, reason=reason)
            embed = discord.Embed(title='TÒA ÁN TỐI CAO',
                                  description='Lệnh bắt giữ',
                                  colour=discord.Colour.blue())
            embed.set_thumbnail(url=member.avatar_url)
            embed.add_field(name='Người kết án',
                            value=ctx.author.mention,
                            inline=False)
            embed.add_field(name='Tội phạm', value=member.mention, inline=False)
            embed.add_field(name='Thời gian thi hành án', value=time, inline=False)
            embed.add_field(name='Lý do', value=reason, inline=False)
            channel = self.client.get_channel(mutechannel)
            await ctx.send(embed=embed)
            await channel.send(embed=embed)
        else:
            tempmute = int(time[0]) * time_convert[time[-1]]
            await member.add_roles(mutedRole, reason=reason)
            embed = discord.Embed(title='TÒA ÁN TỐI CAO',
                                  description='Lệnh bắt giữ',
                                  colour=discord.Colour.blue())
            embed.set_thumbnail(url=member.avatar_url)
            embed.add_field(name='Người kết án',
                            value=ctx.author.mention,
                            inline=False)
            embed.add_field(name='Tội phạm', value=member.mention, inline=False)
            embed.add_field(name='Thời gian thi hành án', value=time, inline=False)
            embed.add_field(name='Lý do', value=reason, inline=False)
            channel = self.client.get_channel(mutechannel)
            await ctx.send(embed=embed)
            await channel.send(embed=embed)
            await asyncio.sleep(tempmute)
            await member.remove_roles(mutedRole)
    @mute.error
    async def mute_error(self, ctx, error):
        if isinstance(error, CheckFailure):
            await ctx.send("Tôi chỉ nghe lệnh từ cấp trên!")

    
    #s+unmute
    @commands.command()
    @has_permissions(manage_messages=True)
    async def unmute(self, ctx, member: discord.Member, *, reason='____'):
        guild = ctx.guild
        mutedRole = discord.utils.get(guild.roles, id=tunhan)
        await member.remove_roles(mutedRole, reason=reason)
        embed = discord.Embed(title='TÒA ÁN TỐI CAO',
                              description='Lệnh ân xá',
                              colour=discord.Colour.blue())
        embed.set_thumbnail(url=member.avatar_url)
        embed.add_field(name='Người ra lệnh',
                        value=ctx.author.mention,
                        inline=False)
        embed.add_field(name='Đối tượng', value=member.mention, inline=False)
        embed.add_field(name='Lý do', value=reason, inline=False)
        channel = self.client.get_channel(mutechannel)
        await ctx.send(embed=embed)
        await channel.send(embed=embed)
    @unmute.error
    async def unmute_error(self, ctx, error):
        if isinstance(error, CheckFailure):
            await ctx.send("Tôi chỉ nghe lệnh từ cấp trên!")


def setup(client):
    client.add_cog(Mute(client))