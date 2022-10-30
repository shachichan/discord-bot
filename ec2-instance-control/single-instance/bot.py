import discord
from discord.ext import commands
import time
import boto3
# Required py-cord extension by pip3 install py-cord

client = commands.Bot()

ec2 = boto3.resource('ec2', region_name='us-west-2') # Change AWS region to your region
instance = ec2.Instance('i-xxxxxxxxxxxxx') # Change instance id to your instance id

@client.event
async def on_ready():
    print("Bot ready!")
    await client.change_presence(activity=discord.Game(name="/help")) # Change the status of the bot


@client.slash_command(description="About Server")
async def help(ctx):
    embed=discord.Embed(title="Server Controller", color=0xffff00)
    embed.add_field(name="Server domain", value="sv.example.com", inline=False)
    embed.add_field(name="Server start", value="Type /start", inline=False)
    embed.add_field(name="Server stop", value="Type /stop", inline=False)
    embed.add_field(name="Server reboot", value="Type /reboot", inline=False)
    embed.add_field(name="Server status", value="Type /status", inline=False)
    await ctx.respond(embed=embed)


@client.slash_command(description="Server start")
async def start(ctx): # Trigger
    if instance.state['Name'] != ('pending', 'running', 'stopping', 'stopped'):
        instance.load()
    if instance.state['Name'] == 'running':
        await ctx.respond("Server is already running!")
        return
    if InstanceStart():
        await ctx.respond(f"{ctx.user.mention} Please wait, Server is about to start...")
        time.sleep(30)
        await ctx.send(f"{ctx.user.mention} Server has been started successfully!")
        await ctx.send("Server Status: " + instance.state['Name'])
        await ctx.send("Server ID: " + instance.id)
        await ctx.send("Server IP: " + instance.public_ip_address)
    else:
        await ctx.respond(f"{ctx.user.mention} An error occurred.")

@client.slash_command(description="Server stop")
async def stop(ctx): # Trigger
    if instance.state['Name'] != ('pending', 'running', 'stopping', 'stopped'):
        instance.load()
    if instance.state['Name'] == 'stopped':
        await ctx.respond("Server is already stopped!")
        return
    if InstanceStop():
        await ctx.respond(f"{ctx.user.mention} Please wait, Server is about to stop...")
        time.sleep(60)
        await ctx.send(f"{ctx.user.mention} Server has been stopped successfully!")
        await ctx.send("Server Status: " + instance.state['Name'])
    else:
        await ctx.respond(f"{ctx.user.mention} An error occurred.")

@client.slash_command(description="Server reboot")
async def reboot(ctx): # Trigger
    if instance.state['Name'] != ('pending', 'running', 'stopping', 'stopped'):
        instance.load()
    if instance.state['Name'] == ('pending', 'stopping', 'stopped'):
        await ctx.respond("Server is not running!")
        return
    if InstanceRestart():
        await ctx.respond(f"{ctx.user.mention} Please wait, Server is about to reboot...")
        time.sleep(60)
        await ctx.send(f"{ctx.user.mention} Server has been rebooted successfully!")
        await ctx.send("Server Status: " + instance.state['Name'])
        await ctx.send("Server ID: " + instance.id)
        await ctx.send("Server IP: " + instance.public_ip_address)
    else:
        await ctx.respond(f"{ctx.user.mention} An error occurred.")

@client.slash_command(description="Check current server status")
async def status(ctx): # Trigger
    if instance.state['Name'] != ('pending', 'running', 'stopping', 'stopped'):
        instance.load()
    if InstanceStatus():
        await ctx.respond(f"{ctx.user.mention} Please wait, Getting server status...")
        await ctx.send("Server Status: " + instance.state['Name'])
        await ctx.send("Server ID: " + instance.id)
        await ctx.send("Server IP: " + instance.public_ip_address)
    else:
        await ctx.respond(f"{ctx.user.mention} An error occurred.")



def InstanceStart():
    try:
        instance.start()
        return True
    except:
        return False


def InstanceStop():
    try:
        instance.stop()
        return True
    except:
        return False


def InstanceRestart():
    try:
        instance.reboot()
        return True
    except:
        return False

def InstanceStatus():
    try:
        instance.state['Name']
        return True
    except:
        return False

client.run('TOKEN') # Replace TOKEN with your bot token