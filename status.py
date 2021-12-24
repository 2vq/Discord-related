# since discord.py is ass heres this
import discord
import requests
import os
import fade
from discord.ext import commands

def cls():
    os.system('cls')

token = input(f'Enter Discord Account Token: ')
cls()
prefix = input(f'Enter Command Prefix: ')
fifteen = commands.Bot(command_prefix = prefix, case_insensitive = True, self_bot = True)

text = f'''
███████╗████████╗ █████╗ ████████╗██╗   ██╗███████╗
██╔════╝╚══██╔══╝██╔══██╗╚══██╔══╝██║   ██║██╔════╝
███████╗   ██║   ███████║   ██║   ██║   ██║███████╗
╚════██║   ██║   ██╔══██║   ██║   ██║   ██║╚════██║
███████║   ██║   ██║  ██║   ██║   ╚██████╔╝███████║
╚══════╝   ╚═╝   ╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚══════╝
                  fifteen#2007
'''

faded = fade.purpleblue(text)

headers = {
    'authorization': token,
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.306 Chrome/78.0.3904.130 Electron/7.1.11 Safari/537.36',
    'content-type': 'application/json'
}

@fifteen.event
async def on_ready():
    cls()
    print(faded)
    print(f'connected to: {fifteen.user}')

@fifteen.command(aliases = ['afk'])
async def idle(ctx):
    await ctx.message.delete()
    try:
        status = {
            'status': 'idle'
        }
        requests.patch(f'https://canary.discordapp.com/api/v9/users/@me/settings', headers = headers, json = status)
        print(f'Discord Status successfully changed to \'Idle\'')
    except:
        print(f'failed')
        pass

@fifteen.command(aliases = ['on'])
async def online(ctx):
    await ctx.message.delete()
    try:
        status = {
            'status': 'online'
        }
        requests.patch(f'https://canary.discordapp.com/api/v9/users/@me/settings', headers = headers, json = status)
        print(f'Discord Status successfully changed to \'online\'')
    except:
        print(f'failed')
        pass

@fifteen.command(aliases = ['donotdisturb'])
async def dnd(ctx):
    await ctx.message.delete()
    try:
        status = {
            'status': 'dnd'
        }
        requests.patch(f'https://canary.discordapp.com/api/v9/users/@me/settings', headers = headers, json = status)
        print(f'Discord Status successfully changed to \'Do Not Disturb (DND)\'')
    except:
        print(f'failed')
        pass

@fifteen.command(aliases = ['offline'])
async def invisible(ctx):
    await ctx.message.delete()
    try:
        status = {
            'status': 'invisible'
        }
        requests.patch(f'https://canary.discordapp.com/api/v9/users/@me/settings', headers = headers, json = status)
        print(f'Discord Status successfully changed to \'invisible\'')
    except:
        print(f'failed')
        pass

fifteen.run(token, bot = False)
