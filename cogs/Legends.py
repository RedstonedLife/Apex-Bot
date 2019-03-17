from discord.ext import commands
import discord, random
import json
import asyncio

class Legends:
    def __init__(self,bot):
        self.bot = bot
    
    @commands.command(pass_context=True)
    async def legend(self,ctx):
        await ctx.message.delete()
        legends = ["Bangalore","Bloodhound","Lifeline","Pathfinder","Gibraltar","Wraith","Caustic","Mirage"]
        await ctx.send(ctx.message.author.mention + " Next game choose `" + random.choice(legends) + "`")

    @commands.command(pass_context=True)
    async def legends(self,ctx):
        await ctx.message.delete()
        legends = ["Bangalore","Bloodhound","Lifeline","Pathfinder","Gibraltar","Wraith","Caustic","Mirage"]
        await ctx.send(ctx.message.author.mention + " Next your team will be `" + random.choice(legends) + "," + random.choice(legends) + "," + random.choice(legends) + "`")


def setup(bot):
   bot.add_cog(Legends(bot))
   print("Added Legends Cog from Cogs!")
