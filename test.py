import discord, asyncio, time
from discord.ext import commands
from key import token
import random


bot = commands.Bot(command_prefix='!')



@bot.command(pass_context = True)
async def e(ctx): #event #(time,ctx) makes delete_message dunt find it 
    await bot.delete_message(ctx.message)
    quote = '```'
    msg = ctx.message.content
    msg = msg.split(None,1)[1]
    global msgtest
    msgtest = await bot.say(quote+msg+quote)
    
    global queue
    queue = []
   
    global test
    for i in range(1,5): #timer here !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        test = await bot.wait_for_reaction(message=msgtest)
    
   
@bot.command(pass_context = True)
async def t(ctx): #test
    await bot.say(test[0].emoji)
    await bot.say(test[1])

@bot.command(pass_context = True)
async def j(ctx): #join
    user = ctx.message.author
    if user not in queue:
        queue.append(user);
    else:
        await bot.say("You are already in quqe")
        
   

@bot.command(pass_context = True)
async def q(ctx): #queue
    for i in (queue):
        await bot.say(i)

        
@bot.command(pass_context = True)
async def r(ctx): 
    await bot.say(msgtest.author)
    await bot.say(msgtest.id)
    await bot.say(msgtest.reactions)
    
'''    
@bot.event #make 2 for both reactions or 2 x if
async def wait_for_reaction(emoji, user, message=msgtest):
    await bot.send_message(bot.get_channel('417770680369676292'), '{}\n{}'.format(emoji.name,user))
    
    #tez moze byc
   #await bot.wait_for_reaction() O.o
'''


'''
@bot.event
async def on_reaction_add(reaction, user):          #get channel id by reaction.channel or sumthing
    if reaction.message.id == msgtest.id:
        if user not in queue:
            queue.append(user)
        else:
            await bot.send_message(bot.get_channel('417770680369676292'), 'You are already in queue')
        
    await bot.send_message(bot.get_channel('417770680369676292'), '{}\n{}'.format(reaction.emoji.name,user))
   
    #To get the message being reacted, access it via Reaction.message.
'''

bot.run(token)
