import discord
from discord import *
import asyncio



client = discord.Client()



@client.event
async def ban():
    if message.content.startswith('your ban command'):
        if message.author.guild_permissions.ban_members:
            split = message.content.split(' ')
            if len(split) == 2:
                member: Member = discord.utils.find(lambda m: split[1] in m.name, message.guild.members)
                if member:
                    await member.ban()
                    await message.channel.send(f'Member {member.name} gebannt!')
                else:
                    await message.channel.send(f'Kein user mit dem Namen {split[1]} gefunden!')


client.run('')
