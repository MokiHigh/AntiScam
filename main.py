from discord.ext import commands
from AntiScam import AntiScam

whitelist = [400691183606693888, 420764023123083265, 328284269245890571, 753650148407640205, 826858091869896724] # Here you can add the IDs of the users allowed to bypass the AntiScam system.
logs_channel = None # Here you can add the ID of the channel where the logs will be sent.

bot = commands.Bot(command_prefix='>')
bot.remove_command('help') # Remove this line if you want to use the help command.

@bot.listen()
async def on_message(message):
    await AntiScam(message, bot = bot, whitelist  = whitelist, muted_role='Muted', verified_role='Gente relajada💎', logs_channel=920114673993515058) # Here you can change the names of the roles.

bot.run('OTIwMTE3NDI5OTk5Mzk4OTQ0.YbfsIg.CWgASOl_lKYI2BXmS9Fc_1nqnk4')
