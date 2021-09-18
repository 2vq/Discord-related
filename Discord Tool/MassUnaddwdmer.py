import discord
import time
import os
from  colorama import Fore

client = discord.Client()

token = 'token here'

@client.event
async def on_connect():
        os.system(f'cls & title [MassDM/Unadd]')
        for user in client.user.friends:
            try:
                await user.send(f'{user.mention} unadding everyone re-add me')
                time.sleep(1)
                await user.remove_friend()
                print(f"{Fore.LIGHTBLACK_EX}[{Fore.CYAN}!{Fore.LIGHTBLACK_EX}] {Fore.CYAN}Messaged/Unadded: {user}")
            except:
                    print(f"{Fore.LIGHTBLACK_EX}[{Fore.CYAN}!{Fore.LIGHTBLACK_EX}] {Fore.CYAN}couldnt message/unadd: {user}")


client.run(token, bot = False)
