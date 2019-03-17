from discord.ext import commands
import discord
import json
import asyncio
from utils import ApexStats

class Stats:
    def __init__(self,bot):
        self.bot = bot
    
    @commands.command(pass_context=True)
    async def stats(self,ctx):
        await ctx.message.delete()
        player = ctx.message.content.split("a.stats ",1)
        if(len(player) == 1):
            embed=discord.Embed(title=":warning: Please give me a player name to look up :warning:")
            m = await ctx.send(embed=embed)
            await asyncio.sleep(3)
            await m.delete()
            return
        embed = ApexStats.get_stats(player[1])
        ###
        
        ###
        await ctx.send(embed=embed)


def setup(bot):
   bot.add_cog(Stats(bot))
   print("Added Stats Cog from Cogs!")
