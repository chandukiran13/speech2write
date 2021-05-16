import discord
import os
from keep_alive import keep_alive
from discord.ext import commands
from sp2wr import convert as convert_sentence

intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix = "-> " ,intents = intents)



@client.event
async def on_ready():
  print(f'We have logged in as {client.user}')
       
@client.event
async def on_message(message):
  if message.author.bot:
    return
  
  await client.process_commands(message)

@client.command()
async def convert(ctx,*,arg):
  await ctx.send(convert_sentence(arg.lower()))
  





keep_alive()
client.run(os.getenv('TOKEN'))