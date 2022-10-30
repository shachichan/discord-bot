import discord
from discord.ext import commands
import re

intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(intents = intents)

@client.event
async def on_ready():
    print("Bot serving contents!")
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Spam Detector"))

@client.event
async def on_message(ctx):
    if ctx.author.bot:
        return
    urls = re.findall('http[s]?://(discord.gg/|discord.com/)([a-zA-Z0-9]+)', ctx.content)
    if urls:
        await ctx.delete()
        await ctx.channel.send(f'{ctx.author.mention} You are not allowed to post Discord Invite here!')

@client.event
async def on_message_edit(before, after):
    if after.author.bot:
        return
    urls = re.findall('http[s]?://(discord.gg/|discord.com/)([a-zA-Z0-9]+)', after.content)
    if urls:
        await after.delete()
        await after.channel.send(f'{after.author.mention} You are not allowed to post Discord Invite here!')

client.run('TOKEN')