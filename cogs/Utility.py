import requests
from requests.exceptions import HTTPError
import discord
import random
from discord.ext import commands

class Utility(commands.Cog, name='Utility'):
    def __init__(self, bot):
        self.bot = bot
    
    def setup(bot):
        bot.add_cog(Utility(bot))

    async def ping(self, ctx: commands.Context):
        """Get the commands's current websocket latency."""
        await ctx.send(f"Pong! {round(self.commands.latency * 1000)}ms")
    @commands.command(help="Rolls a dice")
    async def dice(self, ctx, arg):
        embedDice = discord.Embed(title="Dice", color =discord.Color.from_rgb(100, 255, 20))
        embedDice.add_field(name="You have rolled:", value=str(random.randint(1,int(arg))))
        await ctx.send(embed=embedDice)
