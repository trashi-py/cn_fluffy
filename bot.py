import discord
import os
import discord.ext.commands
from dotenv import load_dotenv 
import json
import sqlite3 as sl
import random
## TRY TO FIX SQLITE OR FIND AN ALTERNATIVE
## E.G.: PARSING INTO .TXT
################## INITIATE ################################
f = open("data.db","w")
f.close
conn = sl.connect("data.db")
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS test (guild_id INTEGER);""")
cur.close()
conn.close()
load_dotenv()
bot = discord.ext.commands.Bot(command_prefix="..!")

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
    await bot.change_presence(activity=discord.Game(name="Test mode initiated"))

############################################################

## COMMAND:
# @bot.command()
# async def <COMMAND NAME>(ctx, <insert args>):
@bot.command()
async def reg1(ctx, arg):
    cur.execute()
@bot.command()
async def test(ctx, arg):
    await ctx.send(arg)
@bot.command()
async def con(ctx):
    print("success")
@bot.command()
async def hug(ctx, arg):
    await ctx.send("<@"+str(ctx.author.id)+">" + " hugs " + arg)
@bot.command()
async def dice(ctx, arg):
    embedDice = discord.Embed(title="Dice", color =discord.Color.from_rgb(100, 255, 20))
    embedDice.add_field(name="You have rolled:", value=str(random.randint(1,int(arg))))
    await ctx.send(embed=embedDice)
@bot.command()
async def goatfact(ctx):
    goatfacts = [
        "Goat revolution is near.", 
        "Goats exist.",
        "Goat goes 'baaaa'.", 
        "Scientists changed genomes of a goat to produce bulletproof vests from their milk.", 
        "Goats were one of the first animals to be tamed by humans and were being herded 9,000 years ago.",
        "Goat meat is the most consumed meat per capita worldwide."
        ]
    await ctx.send(random.choice(goatfacts))

###

@bot.command()
async def embed(ctx, arg1, arg2, cr, cb, cg):
    embedVar = discord.Embed(title=arg1, description=arg2, color=discord.Color.from_rgb(int(cr), int(cb), int(cg)))
    await ctx.send(embed=embedVar)

# help command, update regularly

@bot.command()
async def cmds(ctx):
    embedHelp = discord.Embed(title="Commands:", desc="Prefix = ..!", color =discord.Color.from_rgb(200, 255, 20))
    embedHelp.add_field(name="hug", value="Hugs a user \n Usage: `..!hug <target>`")
    embedHelp.add_field(name="embed", value="Sends an embed. \n Usage: `..!embed <title> <desc> <red> <blue> <green>`")
    embedHelp.add_field(name="goatfact", value="Facts about goats!")
    await ctx.send(embed=embedHelp)

bot.run(os.getenv('TOKEN'))