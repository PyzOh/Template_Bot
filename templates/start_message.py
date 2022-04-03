import discord
from discord import *

client = discord.Client()


@client.event
async def on_ready():
    print('your cmd message')

client.run('')