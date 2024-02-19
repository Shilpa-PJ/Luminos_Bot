# import aiohttp
# aiohttp_session = aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False))

import discord
import decouple
import asyncio

from discord.ext import commands





Luminos = commands.Bot(command_prefix="/",intents=discord.Intents.all())


intents = discord.Intents.default()
intents.members = True


@Luminos.event
async def on_ready():
    print(f'{Luminos.user} has connected to Discord!')

@Luminos.event
async def on_member_join(member):
    channel = member.guild.system_channel
    if channel is not None:
        await channel.send(f'Welcome {member.mention} to the server!')



@Luminos.event
async def on_member_join(member):
    welcome_channel = Luminos.get_channel('1191259877218189322/1208346845592424489')
    message = f"Welcome to Shilpa's server{member.name}"
    await welcome_channel.send(message)
    await member.send(message)

@Luminos.event
async def on_message(message):
    if message.author.bot:
        return
    await message.reply("hello! how can i help you?")





Luminos.run(decouple.config("TOKEN"))