import discord
import asyncio
from discord import *


client = discord.Client()

@client.event
async def on_ready():
    client.loop.create_task(status_task())


async def status_task():
    while True:
        await client.change_presence(activity=discord.Streaming('your activity'), status=discord.Status.online)
        await asyncio.sleep(10)
        await client.change_presence(activity=discord.Streaming('your activity'), status=discord.Status.online)
        await asyncio.sleep(10)



client.run('')