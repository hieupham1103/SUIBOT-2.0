import discord
from discord.ext import commands


class Kick(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
      print('Help is working.')

    
    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed(title='HƯỚNG DẪN CỦA S.U.I',
                              description='',
                              colour=discord.Colour.blue())
        embed.set_thumbnail(url=self.client.user.avatar_url)
        embed.add_field(name='s+ping', value='Gọi cho tôi', inline=False)
        embed.add_field(name='s+listping', value='Danh sách các câu trả lời cá nhân của lênh ping', inline=False)
        embed.add_field(name='s+addping <Câu trả lời>', value='Thêm câu trả lời cá nhân của lênh ping', inline=False)
        embed.add_field(name='s+delping <số thứ tự>', value='Xóa câu trả lời cá nhân của lênh ping', inline=False)
        embed.add_field(name='s+info <ping người khác nếu muốn>', value='Xem profile card', inline=False)
        embed.add_field(name='s+setbg', value='Chỉnh bg cho profile card của mình', inline=False)
        embed.add_field(
            name='s+mute <đối tượng> <thời gian> <lý do>',
            value='Nhốt ai đó vào tù (nếu không có thời gian sẽ là vĩnh viễn)',
            inline=False)
        embed.add_field(name='s+unmute <đối tượng>',
                        value='Ân xá cho tù nhân',
                        inline=False)
        embed.add_field(
            name='s+vanmau <đối tượng>',
            value=
            'Văn mẫu tất nhiên rồi!',
            inline=False)
        embed.add_field(name='s+listvanmau', value='Danh sách văn mẫu', inline=False)
        embed.add_field(name='s+addvanmau <văn mẫu>', value='Thêm văn mẫu', inline=False)
        embed.add_field(name='s+delvanmau <số thứ tự>', value='Xóa văn mẫu', inline=False)
        embed.add_field(name='s+join', value='Mời bot vào voice', inline=False)
        embed.add_field(name='s+play <tên bài hoặc link bài hát>', value='Bật nhac', inline=False)
        embed.add_field(name='s+queue', value='Coi queue nhạc', inline=False)
        embed.add_field(name='s+loop', value='Loop 1 bài nhạc', inline=False)
        embed.add_field(name='s+queueloop', value='Loop queue', inline=False)
        embed.add_field(name='s+remove <số thứ tự>', value='Xóa 1 bài nhạc trong queue', inline=False)
        embed.add_field(name='s+skip', value='skip nhạc trong queue', inline=False)
        embed.add_field(name='s+pause', value='Tạm dừng nhạc', inline=False)
        embed.add_field(name='s+resume', value='Tiếp tục nhạc', inline=False)
        embed.add_field(name='s+volume <số>', value='Chỉnh âm lượng', inline=False)
        embed.add_field(name='s+startYT', value='Coi Youtube cùng nhau qua discord?', inline=False)
        await ctx.send(embed=embed)
    

def setup(client):
    client.add_cog(Kick(client))