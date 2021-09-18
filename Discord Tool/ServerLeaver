import discord
import time
import os
from  colorama import Fore

client = discord.Client()

token = 'token here'

@client.event
async def on_connect():
        os.system(f'cls & title [Account Nuker]')
        for guild in client.guilds:
            try:
                servers = client.get_guild(guild.id)
                await servers.leave()
                print(f'{Fore.LIGHTBLACK_EX}[{Fore.CYAN}!{Fore.LIGHTBLACK_EX}] {Fore.CYAN}left: {guild}')
            except:
                    print(f'{Fore.LIGHTBLACK_EX}[{Fore.CYAN}!{Fore.LIGHTBLACK_EX}] {Fore.RED}couldnt leave: {guild}')


client.run(token, bot = False)
