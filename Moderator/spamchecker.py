import discord
import asyncio
from discord.ext import commands
from discord.ext.commands import has_permissions



class SpamChecker(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
      print('Spam Checker is working.')
      while True:
          await asyncio.sleep(7)
          with open("./Database/spam_detect.txt","r+") as file:
              file.truncate(0)

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.channel.id == 764510929500373023 or message.channel.id == 872033582653255710:
            counter = 0
            with open("./Database/spam_detect.txt","r+") as file:
                for lines in file:
                    if lines.strip("\n") == str(message.author.id):
                        counter+=1
                file.writelines(f"{str(message.author.id)}\n")
                if counter > 4:
                    channel = self.client.get_channel(883990679955591178)
                    await channel.send(f"{message.author.mention} chat chậm thôi!!!!")
                    channel = self.client.get_channel(message.channel.id)
                    await channel.send(f"{message.author.mention} chat chậm thôi!!!!")
    


def setup(client):
    client.add_cog(SpamChecker(client))