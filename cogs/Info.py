from discord.ext import commands
import discord
import json
from utils import SystemUsage 

class Info:
    def __init__(self,bot,data):
        self.bot = bot
        self.data = data
    
    @commands.command(pass_context=True)
    async def info(self,ctx):
        await ctx.message.delete()
        embed = discord.Embed(title="Apex Bot",description="Apex Bot is a bot that can check stats for players, It also comes with some handy commands.",color=0xff04ff)
        embed.set_thumbnail(url=self.bot.user.avatar_url)
        embed.add_field(name="Creator",value=self.data["authors"][0],inline=True)
        embed.add_field(name="Version",value=self.data["version"],inline=True)
        embed.add_field(name="Prefix",value=self.data["prefix"],inline=True)
        a=0
        for guild in self.bot.guilds:
            a += 1
        embed.add_field(name="Servers",value=a,inline=True)
        embed.add_field(name="RAM Usage (%)",value=str(SystemUsage.memory_usage_psutil()) + "%/100%",inline=True)
        embed.add_field(name="CPU USage (%)",value=str(SystemUsage.cpu_usage_psutil()) + "%/100%",inline=True)

        await ctx.send(embed=embed)


def setup(bot,data):
   bot.add_cog(Info(bot,data))
   print("Added Info Cog from Cogs!")
