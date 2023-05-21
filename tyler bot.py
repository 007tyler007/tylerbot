import discord
form discord.ext import commands
@clients= commands.Bot(commnad_prefix='td/')
sync def on_ready():
    print("bot is ready")

@client.command()
async def hello(ctx):
    await ctx.send("hi")

client.run("token")
