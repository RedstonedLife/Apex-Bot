import discord, random
from apex_legends import ApexLegends
from apex_legends import exceptions

apex = ApexLegends("69709b3b-09a7-4b3b-8f55-fdaaae5ab04f")

platform = {
    '1':'XBOX',
    '2':'PSN',
    '5':'PC'
}

def get_stats(player):
    try:
        p = apex.player(player)
    except exceptions.UnknownPlayerError:
        embed = discord.Embed(title=":warning: Couldn't find a player with the name " + player + " :warning:")
        return embed
    thumbs = []
    for legend in p.legends:
        thumbs.append(legend.icon)
        
    embed = discord.Embed(title=player,description="Showing stats for " + player,color=0xff00ff)
    # Add Fields
    embed.add_field(name="Platform",value=platform[str(p.platform)],inline=True)
    embed.add_field(name="Level",value=p.level,inline=True)
    embed.add_field(name="Total Kills",value=p.kills,inline=True)
    embed.add_field(name="Total Damage",value=p.damage,inline=True)
    # Thumbnail
    embed.set_thumbnail(url=random.choice(thumbs))
    # Legends
    for legend in p.legends:
        embed.add_field(name=legend.legend_name + " Kills",value=legend.kills,inline=True)
    return embed
    
