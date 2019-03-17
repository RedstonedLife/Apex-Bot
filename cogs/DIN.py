from discord.ext import commands
import discord
import json
import asyncio
from utils import ApexStats

class Stats:
    def __init__(self,bot):
        self.bot = bot
    
    @commands.command(pass_context=True)
    async def discord(self,ctx):
        await ctx.message.delete()
        embed = discord.Embed(title="Invite Apex Bot to your server!",description="[Click Here To Invite Apex Bot To Your Server!](https://discordapp.com/api/oauth2/authorize?client_id=554047154902138889&permissions=18432&scope=bot)",color=0x2244ff)
        await ctx.send(embed=embed)


def setup(bot):
   bot.add_cog(Stats(bot))
   print("Added DIN Cog from Cogs!")
