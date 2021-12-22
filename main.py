import discord
import os
import json
from discord.ext import commands
from discord.ext.commands.core import command


with open("./config.json","r") as f:
    config = json.load(f)

chungChannel = 764510929500373023


client = commands.Bot(command_prefix='s+')
client.remove_command('help')


@client.event
async def on_ready():
    print('Running')

# for filename in os.listdir('./Moderator'):
#     if filename.endswith('.py'):
#         client.load_extension(f'Moderator.{filename[:-3]}')

# for filename in os.listdir('./Music'):
#     if filename.endswith('.py'):
#         client.load_extension(f'Music.{filename[:-3]}')

# for filename in os.listdir('./ProfileCard'):
#     if filename.endswith('.py'):
#         client.load_extension(f'ProfileCard.{filename[:-3]}')

# for filename in os.listdir('./Gametogether'):
#     if filename.endswith('.py'):
#         client.load_extension(f'Gametogether.{filename[:-3]}')

for filename in os.listdir('./DevZone'):
    if filename.endswith('.py'):
        client.load_extension(f'DevZone.{filename[:-3]}')




client.run(config["bottoken"])
