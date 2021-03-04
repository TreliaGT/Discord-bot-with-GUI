# bot.py
import sys
import discord 
import asyncio
from dotenv import load_dotenv
import os
from gui import app 
import tkinter as tk
import _thread
import threading
load_dotenv()
client = discord.Client()
botchatid = int(os.getenv('BOTCHAT'))
token = os.getenv('TOKEN')
checker = threading.Event()
loop = asyncio.new_event_loop()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

	
@client.event
async def on_message(message):
    if message.author == client.user:
        return
        
    if message.content.startswith('$text'):
        channel = client.get_channel(botchatid)
        await channel.send('Hello There')
        
    if message.content.startswith('$info'):
        channel = client.get_channel(botchatid)
        await channel.send("Hello")
	
    await client.process_commands(message)
    
def lup():
    loop.run_until_complete(client.start(token))


#threading.Thread(target=lup,args=(client.run(token),)).start()
#threading.Thread(target=app).start()

app();






