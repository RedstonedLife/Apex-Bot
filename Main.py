from discord.ext import commands
import discord,json,io
import psutil
# Cogs
from cogs import Info
from cogs import Stats
from cogs import Drop
from cogs import Legends
from cogs import Help
# Events

# # # # # #
with open('cpu\PROCFILE.json') as f:
    data = json.load(f)
########
bot = commands.Bot(command_prefix=data['prefix'],description="Apex Bot is a bot that can check stats for players, It also comes with some handy commands.")
########
    

@bot.event
async def on_guild_join(guild):
    owner_id = guild.owner_id
    member = guild.get_member(owner_id)
    embed = discord.Embed(title="Thanks for inviting me",description="\nYou can see my commands using `h!help`\nYou can see my info using `h!info`",color=0xff04ff)
    await member.send(embed=embed)


@bot.event
async def on_ready():
    bot.remove_command("help")
    await bot.wait_until_ready()
    Info.setup(bot,data)
    Stats.setup(bot)
    Drop.setup(bot)
    Legends.setup(bot)
    Help.setup(bot)
    #
    await bot.change_presence(game=discord.Game(name="a.help",url="https://twitch.tv/redstonedlife",type=2))
    #
    print("Bot is ready")

    
bot.run(data['token'])
