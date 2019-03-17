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
#purge = await ctx.message.channel.purge(limit=amt)
with open('cpu\PROCFILE.json') as f:
    data = json.load(f)
########
bot = commands.Bot(command_prefix=data['prefix'],description="Apex Bot is a bot that can check stats for players, It also comes with some handy commands.")
########

@bot.command(pass_context=True)
async def purge(ctx, amt : int = 5):
    
    purge = await ctx.message.channel.purge(limit=amt)
    data = json.dumps({})
    f = io.StringIO()
    for m in purge:
            mc = str(str(m.clean_content).encode('utf8')).split("b'",1)[1]
            f.write("MSG ID: " + str(m.id) + " | Author Name and Hash: " + str(m.author.name) + "#" + str(m.author.discriminator) + " |  Timestamp: " +str(m.created_at)+" | Message Content: " + str(mc) +" |\n")
    print(f.getvalue())
    await ctx.send(file=discord.File(fp=io.BytesIO(str(f.getvalue()),filename="purge.txt")))
    f.close()
    

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
