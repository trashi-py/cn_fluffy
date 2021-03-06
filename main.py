import discord
import os
import time
from discord.ext import commands
from dotenv import load_dotenv
import sqlite3 as sl
from cogs.Debug import debug
from cogs.Moderation import Moderation
from cogs.Utility import Utility
from cogs.Social import Social
load_dotenv()
token = os.getenv('TOKEN')
intents = discord.Intents.all()
bot = commands.Bot(command_prefix = "..!", intents = intents)
bot.add_cog(Social(bot))
bot.add_cog(Utility(bot))
bot.add_cog(debug(bot))
bot.add_cog(Moderation(bot))
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")
    print(bot.cogs)
    conn = sl.connect("assets/data.sqlite3")
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS guild (guild_id PRIMARY KEY, mute_id, test);""")
    cur.execute("""CREATE TABLE IF NOT EXISTS user (userid PRIMARY KEY, curr INTEGER);""")
    conn.close()
async def on_command():
    try: conn.close()
    except err as error:
        print(err)
bot.run(token)