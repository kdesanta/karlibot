import discord 
import os 
import random 
from dotenv import load_dotenv
from discord.ext import commands
from ec2_metadata import ec2_metadata

intents = discord.Intents.default() 
intents.message_content = True 
intents.members = True 
intents.presences = True


load_dotenv() 
  
client = commands.Bot(command_prefix="!", intents=intents) 
token = str(os.getenv('TOKEN'))


@client.event 
async def on_ready(): 
    print("Logged in as a bot {0.user}".format(client))

print(f'my ec2 metadata region: {ec2_metadata.region}')
print(f'my ec2 metadata instance: {ec2_metadata.instance_id}')

@client.event 
async def on_message(message): 
	username = str(message.author).split("#")[0] 
	channel = str(message.channel.name) 
	user_message = str(message.content) 

	print(f'Message {user_message} by {username} on {channel}') 

	if message.author == client.user: 
		return

	if channel == "desanta": 
		if user_message.lower() == "hello" or user_message.lower() == "hi": 
			await message.channel.send(f'Hello {username}') 
			return
		elif user_message.lower() == "bye": 
			await message.channel.send(f'Bye {username}') 
		elif user_message.lower() == "tell me a joke": 
			jokes = [" Can someone please shed more light on how my lamp got stolen?", 
					"Why is she called llene? She stands on equal legs.", 
					"What do you call a gazelle in a lions territory? Denzel."] 
			await message.channel.send(random.choice(jokes)) 
client.run(token)
