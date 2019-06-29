from discord.ext import commands
from config import token

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(bot.user.name + " initialized!")

bot.run(token)
