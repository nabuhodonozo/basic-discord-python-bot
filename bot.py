from discord.ext import commands
from config import token

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(bot.user.name + " initialized!")

@bot.command(pass_context=True)
async def purge(ctx, limit: int):
    deleted = await ctx.message.channel.purge(limit=limit+1)
    print('Deleted {} message(s), by {}'.format(len(deleted), ctx.message.author))

bot.run(token)
