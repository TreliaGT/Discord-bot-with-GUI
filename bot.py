# bot.py
import sys
import discord 
from dotenv import load_dotenv
import os
import threading
import asyncio
 
class botclass(discord.Client):
	load_dotenv()
	botchatid = int(os.getenv('BOTCHAT'))

	async def on_ready(self):
		print('We have logged in as {0.user}'.format(self))

	async def on_message(self , message):
		if message.author == self.user:
			return
			
		if message.content.startswith('$text'):
			channel = self.get_channel(self.botchatid)
			await channel.send('Hello There')
			
		if message.content.startswith('$info'):
			channel = self.get_channel(self.botchatid)
			await channel.send("Hello")
		
	async def message(self , message):
		channel = self.get_channel(self.botchatid)
		await self.send(message)
		

class loadbot(threading.Thread): 
	
	def __init__(self):
		threading.Thread.__init__(self)
		self.botrun()
		
	def botrun(self):
		load_dotenv()
		token = os.getenv('TOKEN')
		bot = botclass()
		bot.run(token)








