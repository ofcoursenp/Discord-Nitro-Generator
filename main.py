import string
import random
from discord_webhook import DiscordWebhook,DiscordEmbed
import time
lcase = string.ascii_lowercase
ucase = string.ascii_uppercase
num = [1,2,3,4,5,6,7,8,9,0]

add = ""
for j in range(0,999999):
    for i in range(0,16):
        n = random.randint(1,3)
        if n == 1:
            choice = random.choice(lcase)
        if n == 2:
            choice = random.choice(ucase)
        if n == 3:
            choice = str(random.choice(num))
        
        add = add+choice
    
    time.sleep(1)
    data = "http://discord.gift/"+add+"\n"
    webhook = DiscordWebhook(url='Your Webhook Here {For more info go to https://github.com/ofcoursenp/Discord-Nitro-Generator }',username="Test",content=data)
    response = webhook.execute()
    add = ""





