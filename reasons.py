'''
This bot returns an AI generated macro from Inspirobot.me. 
Just message "$inspire" to receive your reason to keep on keeping on.
'''

import discord
from discord.ext import commands
import requests
from requests.exceptions import RequestException


bot = commands.Bot(command_prefix='$')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


@bot.command()
async def inspire(ctx):

    # sends GET request to Inspirobot for image url response
    try:
        url = 'http://inspirobot.me/api?generate=true'
        params = {'generate' : 'true'}
        response = requests.get(url, params, timeout=10)
        image = response.text
        await ctx.send(image)
        
    except RequestException:
        
        await ctx.send('Inspirobot is broken, there is no reason to live.')


@bot.command()
async def xmas(ctx):

    # sends GET request to Inspirobot for image url response
    try:
        url = 'http://inspirobot.me/api?generate=true&season=xmas'
        params = {'generate' : 'true'}
        response = requests.get(url, params, timeout=10)
        image = response.text
        await ctx.send(image)
        
    except RequestException:
        
        await ctx.send('Inspirobot is broken, there is no reason to live.')


@bot.command()
async def info(ctx):
    embed = discord.Embed(title='Reasons', description='Be inspired.',
                          color=0xeee657)
    
    # give info about you here
    embed.add_field(name='Author', value='<YOUR_NAME_HERE>')
    
    # Shows the number of servers the bot is member of.
    embed.add_field(name='Server count', value=f'{len(bot.guilds)}')

    # give users a link to invite this bot to their server
    embed.add_field(name='Invite', 
        value='https://discordapp.com/oauth2/authorize?client_id=' + 
              '<YOUR_BOT_CLIENT_ID_GOES_HERE>&scope=bot')

    await ctx.send(embed=embed)

bot.remove_command('help')


@bot.command()
async def help(ctx):
    embed = discord.Embed(title='Reasons', description='Be inspired.' + 
                          ' List of commands are:', color=0xeee657)
    embed.add_field(name='$inspire', value='Returns an AI generated' + 
                    ' macro from Inspirobot.me', inline=False)
    embed.add_field(name='$xmas', value='Returns an AI generated' + 
                    ' Christmas themed macro from Inspirobot.me', inline=False)
    embed.add_field(name='$info', value='Gives a little info about the bot',
                    inline=False)
    embed.add_field(name='$help', value='Gives this message', inline=False)

    await ctx.send(embed=embed)

bot.run('<YOUR_TOKEN_GOES_HERE>')
