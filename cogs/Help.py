from discord.ext import commands
import discord
import json
import asyncio
from utils import ApexStats

class Stats:
    def __init__(self,bot):
        self.bot = bot
    
    @commands.command(pass_context=True)
    async def help(self,ctx):
        await ctx.message.delete()
        #
        embed = discord.Embed(title="Apex Bot Commands List",description="Commands list for `Apex Bot`",color=0x22ff44)
        #
        embed.add_field(name="Help",value="Displays this message!\nUsage: a.help",inline=False)
        embed.add_field(name="Drop",value="Gives a random drop location for next game!\nUsage: a.drop",inline=False)
        embed.add_field(name="Legend",value="Picks a legend for next game!\nUsage: a.legend",inline=False)
        embed.add_field(name="Legends",value="Pick legends for your team for next match!\nUsage: a.legends",inline=False)
        embed.add_field(name="Stats",value="Displays stats for a given user!\nUsage: a.stats <IGN>\nExample: a.stats RedstonedLife",inline=False)
        embed.add_field(name="Info",value="Displays bot info!\nUsage: a.info",inline=False)
        embed.add_field(name="Discord",value="Gives a invite link so people can invite the bot!\nUsage: a.discord",inline=False)
        #
        await ctx.send(embed=embed)


def setup(bot):
   bot.add_cog(Stats(bot))
   print("Added Stats Cog from Cogs!")
