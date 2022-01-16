# made this because people actually dont have embed massdm's :joy:
# anythng that happens to your discord account isnt my problem :joy:

import discord

client = discord.Client()
color = 0xFF0000
token = input(f'Token -> ')
tt = "Title here" # Change Embed Title here
desc = "Text here" # Change Embed description here
thumbn = "https://cdn.discordapp.com/attachments/852596305406853140/881215847539019846/dcfae76d14ff6129.gif" # link only!

@client.event
async def on_connect():
  for user in client.user.friends:
    try:
      em = discord.Embed(title = tt, description = desc, color = color)
      em.set_thumbnail(url = thumbn)
      await user.send(embed = em)
      print(f"messaged: {user.name}")
    except:
       print(f"couldnt message: {user.name}")

client.run(token, bot = False)
