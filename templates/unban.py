from posixpath import split
import discord
from discord import *
import asyncio


client = discord.Client()


@client.event
async def unban():
    if message.content.startswith('$unban') and message.author.guild_permissions.ban_members:
        split = message.content.split(' ')
        if len(args) == 2:
            user: User = discord.utils.find(lambda m: split[1] in m.user.name, await message.guild.bans()).user
            if user:
                await message.guild.unban(user)
                await message.channel.send(f'User {user.name} entbannt.')
            else:
                await message.channel.send(f'Kein user mit dem Namen {split[1]} gefunden.')


client.run('')