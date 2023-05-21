#bot.py
from keep_alive import keep_alive
import os
import random
import requests
import json
from tylerbotvid import truth ,dare
import discord
from discord.ext import commands
from dotenv import load_dotenv



load_dotenv()




client=commands.Bot(command_prefix="td/")


@client.command()
async def hello(ctx):
    await ctx.send("bsdk sonne ka katora diya hai tu bheek hi maang , ek kaam kar gogi ko bula gogi ko...")

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, aa gaye subha subha bezzati karne XD'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return

   
  
    

   
    if  message.content == 'td/truth':
        response = random.choice(truth)
        await message.channel.send(response)
    if message.content == 'td/dare':
        response = random.choice(dare)
        await message.channel.send(response)

    
        
    if message.content == 'raise-exception':
        raise discord.DiscordException


@client.event
async def on_message(message):

    if message.content.startswith("maths"):
            await message.channel.send("mehul ke bete 99.9999% aye the ,md  usne sameer bansal puri solve kari thi...")
            await message.channel.send(
            "https://media.tenor.com/images/3b311c940c28b55c88f21285f9161fc7/tenor.gif")
    if message.content.startswith("chemistry"):
        await message.channel.send("CUM-on childron, fasht take out your textbooks")
        await message.channel.send(
            "https://sticker.ly/s/HVS8YZ")
    if message.content.startswith("baba"):
        await message.channel.send("bawaji ki baat karta hai " + str(message.author) +
                                   " ruk abhi bulta hu bawa ji ko:")
        await message.channel.send("https://media1.tenor.com/images/533348e8589eb7981c398bd7b7fedc36/tenor.gif?itemid=23015471")

    if message.content.startswith("manzil"):
         await message.channel.send("https://media.tenor.com/images/c2740a1db628b39d8632f30e2c612f44/tenor.gif")
         
         await message.channel.send(
            "aisi baate mere maalik ke bina ,ruka abhi ping karta hu aane do mere maalik ko ,unke sath karna man-zeel ki baate")

         await message.channel.send("sethji aa jao <@!709661391367438397> apke charcha ka vishawye aya hai")

    if message.content.startswith("td/jainkicrush"):
         await message.channel.send("abhi tanzil hai ,lekin ab khatam ,ab fir wapis ho gayi ....in short ")
         await message.channel.send(
            "https://media.tenor.com/images/7ae75c8c70b723bd5e0e79e70b96f979/tenor.gif")
         await message.channel.send("sole credits to this thing goes to akkchhat geete")
    if message.content.startswith(":tamatar"):
         await message.channel.send("tamatar bhejne wala geete lund hai XD")
    if message.content.startswith("td/mondaymotivation"):
         await message.channel.send("https://media.tenor.com/images/d31a87d168f7d3ce760f2e9190c0fd7c/tenor.gif")
         await message.channel.send("bulati nahi hai magar jane ka hai (zyda nahi thodu sa)")
         await message.channel.send("https://c.tenor.com/anHGmrKtWwQAAAAM/bulati-hai-magar-jane-ka-nahi.gif")
    if message.content.startswith("td/hariflip"):
         await message.channel.send("https://c.tenor.com/X0XhvCYLnbEAAAAC/shashitharoorhairflip-tharoorianhairflip-hairflip-shashitharoorflip.gif")
    if message.content.startswith("apni history batao"):
         await message.channel.send("Mera naam Tyler Durden , mujhe mere maalik Aayush Jain ne bnaya hai.Mai apki kaafi seva kar sakta hu mere maalik ke dwara.")
        
    if message.content.startswith("sedlyfgeete"):
         await message.channel.send("https://media.tenor.com/images/477f7fef8f7920ac6c5f8c1724502f95/tenor.gif")    

keep_alive()
my_secret = os.environ['token']
client.run(os.environ['token'])

