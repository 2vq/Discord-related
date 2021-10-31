# not originally made by me
import discord
import json
import os
import asyncio
import time
from colorama import Fore as f
from discord.ext import commands

token = '' # token here
prefix = '$' # prefix here
twitch = 'https://twitch.tv/---' # you can change this ?
deltime = 1 # you could change this but i recommend not to change it lmfao


client = commands.Bot(command_prefix = prefix, case_insensitive = True, self_bot = True)
client.remove_command('help')

@client.event
async def on_ready():
    os.system(f'cls & title [Discord Status Tool] - {client.user}')
    print(f'''
{f.LIGHTBLACK_EX}[{f.LIGHTMAGENTA_EX}*{f.LIGHTBLACK_EX}] Type {f.LIGHTMAGENTA_EX}{prefix}help {f.LIGHTBLACK_EX}anywhere to get help

{f.LIGHTBLACK_EX}[{f.LIGHTMAGENTA_EX}*{f.LIGHTBLACK_EX}] Connected To: {f.LIGHTMAGENTA_EX}{client.user}
{f.LIGHTBLACK_EX}[{f.LIGHTMAGENTA_EX}*{f.LIGHTBLACK_EX}] UserID: {f.LIGHTMAGENTA_EX}{client.user.id}
{f.LIGHTBLACK_EX}[{f.LIGHTMAGENTA_EX}*{f.LIGHTBLACK_EX}] Name: {f.LIGHTMAGENTA_EX}{client.user.name}
{f.LIGHTBLACK_EX}[{f.LIGHTMAGENTA_EX}*{f.LIGHTBLACK_EX}] Total Friends: {f.LIGHTMAGENTA_EX}{len(client.user.friends)}
{f.LIGHTBLACK_EX}[{f.LIGHTMAGENTA_EX}*{f.LIGHTBLACK_EX}] Total Guilds: {f.LIGHTMAGENTA_EX}{len(client.guilds)} 
    ''')

@client.event
async def on_command_error(ctx, error):
   if isinstance(error, commands.CommandNotFound):
       print(f'{f.LIGHTBLACK_EX}[{f.RED}-{f.LIGHTBLACK_EX}]{f.LIGHTBLACK_EX} {f.RED}{ctx.message.content} {f.LIGHTBLACK_EX}wasnt found!')
   pass

@client.command()
async def help(ctx):
    await ctx.message.delete()
    await ctx.send('Check print logs!', delete_after = deltime)
    print(f'''
{f.LIGHTBLACK_EX}[{f.LIGHTMAGENTA_EX}!{f.LIGHTBLACK_EX}] {f.LIGHTMAGENTA_EX}play {f.LIGHTBLACK_EX}[msg]
{f.LIGHTBLACK_EX}[{f.LIGHTMAGENTA_EX}!{f.LIGHTBLACK_EX}] {f.LIGHTMAGENTA_EX}stream {f.LIGHTBLACK_EX}[msg]
{f.LIGHTBLACK_EX}[{f.LIGHTMAGENTA_EX}!{f.LIGHTBLACK_EX}] {f.LIGHTMAGENTA_EX}watch {f.LIGHTBLACK_EX}[msg]
{f.LIGHTBLACK_EX}[{f.LIGHTMAGENTA_EX}!{f.LIGHTBLACK_EX}] {f.LIGHTMAGENTA_EX}listen {f.LIGHTBLACK_EX}[msg]
{f.LIGHTBLACK_EX}[{f.LIGHTMAGENTA_EX}!{f.LIGHTBLACK_EX}] {f.LIGHTMAGENTA_EX}compete {f.LIGHTBLACK_EX}[msg]''')

@client.command()
async def play(ctx, *, msg):
    await ctx.message.delete()
    print(f'{f.LIGHTBLACK_EX}[{f.LIGHTMAGENTA_EX}+{f.LIGHTBLACK_EX}] {f.LIGHTMAGENTA_EX}{ctx.message.content} {f.LIGHTBLACK_EX}was used!')
    await client.change_presence(activity = discord.Game(name = f'{msg}'))

@client.command()
async def stream(ctx, *, msg):
    await ctx.message.delete()
    print(f'{f.LIGHTBLACK_EX}[{f.LIGHTMAGENTA_EX}+{f.LIGHTBLACK_EX}] {f.LIGHTMAGENTA_EX}{ctx.message.content} {f.LIGHTBLACK_EX}was used!')
    await client.change_presence(activity = discord.Streaming(name = f'{msg}', url = f'{twitch}'))

@client.command()
async def watch(ctx, *, msg):
    await ctx.message.delete()
    print(f'{f.LIGHTBLACK_EX}[{f.LIGHTMAGENTA_EX}+{f.LIGHTBLACK_EX}] {f.LIGHTMAGENTA_EX}{ctx.message.content} {f.LIGHTBLACK_EX}was used!')
    await client.change_presence(activity = discord.Activity(type = discord.ActivityType.watching, name = f'{msg}'))

@client.command()
async def listen(ctx, *, msg):
    await ctx.message.delete()
    print(f'{f.LIGHTBLACK_EX}[{f.LIGHTMAGENTA_EX}+{f.LIGHTBLACK_EX}] {f.LIGHTMAGENTA_EX}{ctx.message.content} {f.LIGHTBLACK_EX}was used!')
    await client.change_presence(activity = discord.Activity(type = discord.ActivityType.listening, name = f'{msg}'))

@client.command()
async def compete(ctx, *, msg):
    await ctx.message.delete()
    print(f'{f.LIGHTBLACK_EX}[{f.LIGHTMAGENTA_EX}+{f.LIGHTBLACK_EX}] {f.LIGHTMAGENTA_EX}{ctx.message.content} {f.LIGHTBLACK_EX}was used!')
    await client.change_presence(activity = discord.Activity(type = discord.ActivityType.competing, name = f'{msg}'))

@client.command()
async def purge(ctx, amount: int): 
    await ctx.message.delete()
    print(f'{f.LIGHTBLACK_EX}[{f.LIGHTMAGENTA_EX}+{f.LIGHTBLACK_EX}] {f.LIGHTMAGENTA_EX}{ctx.message.content} {f.LIGHTBLACK_EX}was used!')
    async for message in ctx.message.channel.history(limit = amount).filter(lambda m: m.author == client.user).map(lambda m: m):
        try:
           await message.delete()
           print(f'{f.LIGHTBLACK_EX}[ {f.LIGHTMAGENTA_EX}{message.content}{f.LIGHTBLACK_EX} ] {f.LIGHTBLACK_EX}has been {f.LIGHTMAGENTA_EX}deleted')
        except:
            pass
            print(f'{f.LIGHTBLACK_EX}[{f.LIGHTMAGENTA_EX}{message.content}{f.LIGHTBLACK_EX}]{f.RED} Couldn\'t be deleted')

client.run(token, bot = False)
