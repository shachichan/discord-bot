import discord
from discord.ext import commands
import time
import boto3
# Required py-cord extension by pip3 install py-cord

client = commands.Bot()

ec2 = boto3.resource('ec2', region_name='us-west-2') # Change AWS region to your region
instance1 = ec2.Instance('i-xxxxxxxxxxxxxxxxx') # Change first instance id to your instance id
instance2 = ec2.Instance('i-xxxxxxxxxxxxxxxxx') # Change second instance id to your instance id


@client.event
async def on_ready():
    print("Bot ready!")
    await client.change_presence(activity=discord.Game(name="/help"))


@client.slash_command(description="About Server")
async def help(ctx):
    embed=discord.Embed(title="Server Controller", color=0xffff00)
    embed.add_field(name="Server domain", value="sv.example.com", inline=False)
    embed.add_field(name="Description", value="It's easy to manage the server with domain on the list.", inline=False)
    embed.add_field(name="Server start", value="Type /start", inline=False)
    embed.add_field(name="Server stop", value="Type /stop", inline=False)
    embed.add_field(name="Server reboot", value="Type /reboot", inline=False)
    embed.add_field(name="Server status", value="Type /status", inline=False)
    await ctx.respond(embed=embed)

# First Instance
@client.slash_command(description="Start First Server")
async def start1(ctx): # Trigger
    if instance1.state['Name'] != ('pending', 'running', 'stopping', 'stopped'):
        instance1.load()
    if instance1.state['Name'] == 'running':
        await ctx.respond("Server is already running!")
        return
    if InstanceStart1():
        await ctx.respond("Server starting!")
        time.sleep(30)
        await ctx.respond("Server started!")
        await ctx.send("Server status: " + instance1.state['Name'])
        await ctx.send("Server IP: " + instance1.public_ip_address)
    else:
        await ctx.respond("Server start failed!")

@client.slash_command(description="Stop First Server")
async def stop1(ctx): # Trigger
    if instance1.state['Name'] != ('pending', 'running', 'stopping', 'stopped'):
        instance1.load()
    if instance1.state['Name'] == 'stopped':
        await ctx.respond("Server is already stopped!")
        return
    if InstanceStop1():
        await ctx.respond("Server stopping!")
        time.sleep(30)
        await ctx.respond("Server stopped!")
        await ctx.send("Server status: " + instance1.state['Name'])
    else:
        await ctx.respond("Server stop failed!")

@client.slash_command(description="Reboot First Server")
async def reboot1(ctx): # Trigger
    if instance1.state['Name'] != ('pending', 'running', 'stopping', 'stopped'):
        instance1.load()
    if instance1.state['Name'] == 'stopped':
        await ctx.respond("Server is stopped!")
        return
    if InstanceRestart1():
        await ctx.respond("Server rebooting!")
        time.sleep(30)
        await ctx.respond("Server rebooted!")
        await ctx.send("Server status: " + instance1.state['Name'])
        await ctx.send("Server IP: " + instance1.public_ip_address)
    else:
        await ctx.respond("Server reboot failed!")

@client.slash_command(description="Status First Server")
async def status1(ctx): # Trigger
    if instance1.state['Name'] != ('pending', 'running', 'stopping', 'stopped'):
        instance1.load()
    if InstanceStatus1():
        await ctx.respond("Server status: " + instance1.state['Name'])
        await ctx.send("Server IP: " + instance1.public_ip_address)
    else:
        await ctx.respond("Server status failed!")

# Second Instance
@client.slash_command(description="Start Second Server")
async def start2(ctx): # Trigger
    if instance2.state['Name'] != ('pending', 'running', 'stopping', 'stopped'):
        instance2.load()
    if instance2.state['Name'] == 'running':
        await ctx.respond("Server is already running!")
        return
    if InstanceStart2():
        await ctx.respond("Server starting!")
        time.sleep(30)
        await ctx.respond("Server started!")
        await ctx.send("Server status: " + instance2.state['Name'])
        await ctx.send("Server IP: " + instance2.public_ip_address)
    else:
        await ctx.respond("Server start failed!")

@client.slash_command(description="Stop Second Server")
async def stop2(ctx): # Trigger
    if instance2.state['Name'] != ('pending', 'running', 'stopping', 'stopped'):
        instance2.load()
    if instance2.state['Name'] == 'stopped':
        await ctx.respond("Server is already stopped!")
        return
    if InstanceStop2():
        await ctx.respond("Server stopping!")
        time.sleep(30)
        await ctx.respond("Server stopped!")
        await ctx.send("Server status: " + instance2.state['Name'])
    else:
        await ctx.respond("Server stop failed!")

@client.slash_command(description="Reboot Second Server")
async def reboot2(ctx): # Trigger
    if instance2.state['Name'] != ('pending', 'running', 'stopping', 'stopped'):
        instance2.load()
    if instance2.state['Name'] == 'stopped':
        await ctx.respond("Server is stopped!")
        return
    if InstanceRestart2():
        await ctx.respond("Server rebooting!")
        time.sleep(30)
        await ctx.respond("Server rebooted!")
        await ctx.send("Server status: " + instance2.state['Name'])
        await ctx.send("Server IP: " + instance2.public_ip_address)
    else:
        await ctx.respond("Server reboot failed!")

@client.slash_command(description="Status Second Server")
async def status2(ctx): # Trigger
    if instance2.state['Name'] != ('pending', 'running', 'stopping', 'stopped'):
        instance2.load()
    if InstanceStatus2():
        await ctx.respond("Server status: " + instance2.state['Name'])
        await ctx.send("Server IP: " + instance2.public_ip_address)
    else:
        await ctx.respond("Server status failed!")



def InstanceStart1():
    try:
        instance1.start()
        return True
    except:
        return False


def InstanceStop1():
    try:
        instance1.stop()
        return True
    except:
        return False


def InstanceRestart1():
    try:
        instance1.reboot()
        return True
    except:
        return False

def InstanceStatus1():
    try:
        instance1.state['Name']
        return True
    except:
        return False

def InstanceStart2():
    try:
        instance2.start()
        return True
    except:
        return False

def InstanceStop2():
    try:
        instance2.stop()
        return True
    except:
        return False

def InstanceRestart2():
    try:
        instance2.reboot()
        return True
    except:
        return False

def InstanceStatus2():
    try:
        instance2.state['Name']
        return True
    except:
        return False

client.run('TOKEN') # Replace TOKEN with your bot token