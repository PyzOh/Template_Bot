import discord
from discord import *
import asyncio



client = discord.Client()

@client.event
async def change_presence():
    if message.content.startswith('c_p do_not_disturb'):
        split = message.content.split(' ')
        if len(split) == 2:
            if message.author.bot:
                return
            else:
                await client.change_presence(activity=discord.Game("your activity"), status=discord.Status.do_not_disturb)
                await asyncio.sleep(5)
                await client.change_presence(activity=discord.Game("your activity"), status=discord.Status.do_not_disturb)
                await asyncio.sleep(5)


client.run('')


#it's important to deaktivate the while True function!