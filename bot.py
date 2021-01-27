import discord
import asyncio
client = discord.Client()


import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '?')

@client.event
async def on_ready():
    print('Logged in to {0.user}'.format(client))

@client.event
async def on_member_join(member):
    welcome = discord.Embed(
        color = discord.Color.green(),
        title = 'Welcome to Kierans Projects!',
        description = f'Welcome to the server {member.mention}! '
    )
    await member.send(embed=welcome)



@client.command()
async def say(ctx, *, text):
    if ctx.message.author.id == 504764660306673666:
        message = ctx.message
        await message.delete()

        await ctx.send(f"{text}")

    if ctx.message.author.id == 617073426082955456:
        message = ctx.message
        await message.delete()

        await ctx.send(f"{text}")
    
    if ctx.message.author.id == 318814695526236162:
        message = ctx.message
        await message.delete()

        await ctx.send(f"{text}")

    if ctx.message.author.id == 419067333122719755:
        message = ctx.message
        await message.delete()

        await ctx.send(f"{text}")
    
    if ctx.message.author.id == 406895061352054784:
        message = ctx.message
        await message.delete()

        await ctx.send(f"{text}")

@client.command()
async def cpt(ctx, *, text):
    if ctx.message.author.id == 504764660306673666:
        message = ctx.message
        await message.delete()

        say = discord.Embed(
                description = f"{text}",
                colour = discord.Colour.blue())
    
        await ctx.send(embed=say)
    else:
        await ctx.send('You cannot use this command')


@client.command()
async def hug(ctx, *, mention):
        await ctx.send('If you need any support while using our bot. Make sure you check out the discord server for support. \n \n https://wherryproject.xyz/links/discord')



@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! `{round (client.latency * 1000)}ms`')


@client.command()
async def support(ctx):
    await ctx.send('If you need any support while using our bot. Make sure you check out the discord server for support. \n \n https://wherryproject.xyz/links/discord')    

@client.command()
async def pogchamp(ctx):
    await ctx.send('https://tenor.com/view/pogchamp-pog-pogey-poggers-twitch-gif-14340727')

@client.command()
async def subscribe(ctx):
    await ctx.send('https://www.youtube.com/c/Kieran%E2%80%99sTransportDiaries')
 

@client.command()
async def credits(ctx):
    await ctx.send('This bot was made by `CrownPointTMD` for the Kierans Transport Daries discord server. Check out his github: \n \n https://github.com/CrownPointTMD  \n \n The bot was also made with help from Oli.  \n https://www.youtube.com/c/OliEatsPringles')

@client.command()
async def geegee(ctx):
    await ctx.send('"Alright Kieran you asked for this. Geegee."  \n \n  https://cdn.discordapp.com/attachments/779853627467497502/782524339358400512/video0.mp4')

@client.command()
async def battle(ctx):
    await ctx.send('https://www.youtube.com/watch?v=z_buNwsYNAc&list=PLlJddkadYDcAV7pkLp4JIgo_ajoACL5eg&index=15&ab_channel=Flygalia')

@client.command()
async def twitter(ctx):
    await ctx.send('https://twitter.com/SimRailROBLOX')

@client.command()
async def pog(ctx):
    await ctx.send('https://www.youtube.com/watch?v=NFB6Y2Qt8ag&ab_channel=Monstercat%3AUncaged')

@client.command()
async def orangejuice(ctx):
    await ctx.send('Enjoy a nice, Fresh glass of OJ, Here You go! https://cdn.discordapp.com/attachments/764437197205143562/792486826853924894/image.png')
