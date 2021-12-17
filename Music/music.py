from operator import index
import discord
import json
import discordSuperUtils
from discordSuperUtils import MusicManager
from discord.ext import commands


with open("./config.json","r") as f:
    config = json.load(f)

client_id = config["clientid"]
client_secret = config["clientsecret"]


class Music(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.MusicManager = MusicManager(self.client, spotify_support=False)

    @commands.Cog.listener()
    async def on_ready(self):
        print('Music is working.')

    @discordSuperUtils.CogManager.event(discordSuperUtils.MusicManager)
    async def on_play(self, ctx, player):
        await ctx.send(f"Đang bật: {player}")


    @commands.command()
    async def join(self, ctx):
        await self.MusicManager.play(ctx, 'https://www.youtube.com/watch?v=jhFDyDgMVUI')
        if await self.MusicManager.join(ctx):
            await ctx.send("Bot đã vào voice!")
    
    @commands.command()
    async def leave(self, ctx):
        if await self.MusicManager.leave(ctx):
            await ctx.send("Bot đã ra khỏi voice")

    @commands.command()
    async def check(self, ctx):
        if player := await self.MusicManager.now_playing(ctx):
            duration_played = await self.MusicManager.get_player_played_duration(ctx, player)
            # You can format it, of course.

            await ctx.send(f"Đang bật: {player}, \n"
                           f"Thời gian: {duration_played}/{player.duration}")

    @commands.command()
    async def play(self, ctx, *, query: str):
        if not ctx.voice_client or not ctx.voice_client.is_connected():
            await self.MusicManager.join(ctx)

        async with ctx.typing():
            players = await self.MusicManager.create_player(query, ctx.author)

        if players:
            if await self.MusicManager.queue_add(players=players, ctx=ctx) and not await self.MusicManager.play(ctx):
                await ctx.send("Thêm vào queue")

        else:
            await ctx.send("Không tìm thấy")

    @commands.command()
    async def pause(self, ctx):
        if await self.MusicManager.pause(ctx):
            await ctx.send("Tạm ngưng...")

    @commands.command()
    async def resume(self, ctx):
        if await self.MusicManager.resume(ctx):
            await ctx.send("Tiếp tục...")
    
    @commands.command()
    async def volume(self, ctx, volume: int):
        await self.MusicManager.volume(ctx, volume)
    
    @commands.command()
    async def loop(self, ctx):
        is_loop = await self.MusicManager.loop(ctx)
        await ctx.send(f"Lặp: {is_loop}")
    
    @commands.command()
    async def queueloop(self, ctx):
        is_loop = await self.MusicManager.queueloop(ctx)
        await ctx.send(f"Loop queue: {is_loop}")

    @commands.command()
    async def skip(self, ctx, index: int = None):
        await self.MusicManager.skip(ctx, index)
        await ctx.send(f"Skip bài go brubru!!")

    @commands.command()
    async def queue(self, ctx):
        formatted_queue = [
            f"Title: '{x.title}\nRequester: {x.requester.mention}" for x in (await self.MusicManager.get_queue(ctx)).queue
        ]

        embeds = discordSuperUtils.generate_embeds(formatted_queue,
                                                   "Queue",
                                                   f"Đang bật: {await self.MusicManager.now_playing(ctx)}",
                                                   25,
                                                   string_format="{}")

        page_manager = discordSuperUtils.PageManager(ctx, embeds, public=True)
        await page_manager.run()

    @commands.command()
    async def remove(self, ctx, index: int = None):
        index -= 1
        await self.MusicManager.queue_remove(ctx,index)
        await ctx.send(f"Đã remove trong queue!!")

    

def setup(client):
    client.add_cog(Music(client))
