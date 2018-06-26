import discord, asyncio
from discord.ext import commands
from key import token
import random


bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    await bot.send_message(bot.get_channel('417770680369676292'), 'Wbijam do kanau (:')


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
        await bot.say('Jestem gupi i nic nie rozumiem')



@bot.command(pass_context = True)
async def hlep(ctx):
    await bot.delete_message(ctx.message)
    msg = "```css\n!hlep - wyswietla liste komend\n!clear all - usuwa wszystko \n!clear liczba - usuwa liczba wiadomosci\n!jestem botem - nadaje range ''bot peaceful'' uzytkownikowi\n!promote username/id ''rank name'' \n\n!add liczba liczba```"
    await bot.say(msg)

	
@bot.command(pass_context = True)
async def jestem(ctx):
	if (ctx.message.content=='!jestem botem'):
		await bot.delete_message(ctx.message)
		user = ctx.message.author.mention
		role = discord.utils.get(ctx.message.server.roles, name='BOTY')
		await bot.add_roles(ctx.message.author, role)
		await bot.say('Brawo {} od dziś należysz do zacnego grona {}'.format(user, role))

        
@bot.command(pass_context = True)
async def promote(ctx, user, rank):
    await bot.delete_message(ctx.message)
    if (user.isdigit()):
        username = discord.utils.get(ctx.message.server.members, id=user)
    elif(user == ((discord.utils.get(ctx.message.server.members, name=user).name))):
        username = discord.utils.get(ctx.message.server.members, name=user)
    else:
        await bot.say('Error')
    role = discord.utils.get(ctx.message.server.roles, name=rank)
    await bot.add_roles(username, role)
    await bot.say('Brawo {} od dziś należysz do zacnego grona {}'.format(username.mention, role))
	
	
bot.run(token)