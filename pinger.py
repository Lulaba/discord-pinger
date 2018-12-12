import discord
from discord.ext import commands
import requests

requests.packages.urllib3.disable_warnings()

TOKEN = '' #SET YOUR BOT TOKEN HERE 

client = discord.Client()

keywords = ["fuck","shit","hello"] #SET YOUR KEY WORDS HERE


@client.event
async def on_message(message):
    for keyword in keywords:
        if keyword.lower() in message.content.lower() and message.channel.name == "rules": # SET YOUR CHANNEL NAME HERE
            await client.send_message(message.channel,"@everyone - keyword matched") #SET YOUR MESSAGE HERE YOU WANT TO USE     


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

while True:
    client.run(TOKEN)

