import discord, asyncio
from discord.ext import commands
import random


bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    await bot.send_message(bot.get_channel('366519745790345217'), 'Wbijam do kanau (:')


@bot.command()
async def add(nr_one : int, nr_two : int):
    await bot.say(nr_one + nr_two)


@bot.command(pass_context = True)
async def clear(ctx, num):
    if num == 'all':
        await bot.purge_from(ctx.message.channel)
    elif num.isdigit():
        num = int(num)
        mgs = []
        async for i in bot.logs_from(ctx.message.channel, limit = num + 1):
            mgs.append(i)
        await bot.delete_messages(mgs)
    else:
	#add !clear "nickname" czysci wszystkie wiad danego uzytkownika
        await bot.say('Jestem jebanym debilem i nic nie rozumiem')

@bot.command(pass_context = True)
async def hlep(ctx):
    await bot.delete_message(ctx.message)
    msg = "```css\n!hlep - wyswietla liste komend\n!clear all - usuwa wszystko \n!clear liczba - usuwa liczba wiadomosci \n\n!add liczba liczba```"
    await bot.say(msg)
	
	
	
# ******************************************
#                Queue bot
# ******************************************
@bot.command(pass_context = True)
async def event(ctx):
	await bot.delete_message(ctx.message)
	global queue
	global counter
	queue = []
	
@bot.command(pass_context = True)
async def join(ctx):
    await bot.delete_message(ctx.message)
    user = ctx.message.author
    if user in queue:
        await bot.say('You are already in queue')
    else:
        queue.append(user)
        await bot.say(queue)
bot.run('')
