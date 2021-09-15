import discord

client = discord.Client()

token = 'discord token here'

@client.event
async def on_connect():
    for channel in client.private_channels:
        if isinstance(channel, discord.GroupChannel): 
            await channel.leave() # leaves EVERY groupchat ur in (i used this to get myself untrapped L O L)
            print(f'left groupchat: {channel}')

client.run(token, bot = False)
