import discord
from discord import *

client = discord.Client()




@client.event
async def kick():
    if message.content.startswith('&kick'):
        if message.author.guild_permissions.kick_members:
            split = message.content.split(' ')
            if len(split) == 2:
                member: Member = discord.utils.find(lambda m: split[1] in m.name, message.guild.members)
                if member:
                    await member.kick()
                    await message.channel.send(f'Member {member.name} gekickt!')
                else:
                    await message.channel.send(f'Kein user mit dem Namen {split[1]} gefunden!')

client.run('')