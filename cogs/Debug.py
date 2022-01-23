import discord
import requests
from requests import HTTPError
from discord.ext import commands
import sqlite3 as sl
conn = sl.connect("assets/data.sqlite3")
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS guild (guild_id PRIMARY KEY, mute_id, test);""")
cur.execute("""CREATE TABLE IF NOT EXISTS user (userid PRIMARY KEY, curr INTEGER);""")
class Debug(commands.Cog, name='Debug'):
    def __init__(self, bot):
        self.bot = bot
    def setup(self, bot):
        bot.add_cog(Debug(bot))
    @commands.command(help="//DEBUG//")
    async def join(self, context):
            if (context.author.voice):
                channel = context.author.voice.channel
                voice = await channel.connect()
                player = voice.play(discord.FFmpegPCMAudio(executable="C:/ffmpeg/bin/ffmpeg.exe", source="testaud.mp3"))
            else:
                context.send("You must be in a voice channel")
    # Leave command, leaves the voice channel
    @commands.command(help="//DEBUG//")
    async def leave(self, context):
            await context.voice_client.disconnect()
    @commands.command(help="//DEBUG//")
    async def user(self, ctx, arg):
        cur.execute("select * from user where userid =" + str(ctx.author.id))
        res = cur.fetchone()
        try: (uid,cr) = res
        except:
            cur.execute("INSERT INTO user (userid) VALUES (?, ?)",(ctx.author.id, arg))
            conn.commit()
        finally:
            cur.execute("UPDATE user SET curr = ? WHERE userid = ?",(arg, ctx.author.id))
            cur.fetchone()
            conn.commit()
            (uid,cr) = res
            await ctx.send(str(cr)+"--->"+str(arg))
    @commands.command(help="//DEBUG//")
    async def guild_reg(self, ctx, arg):
        cur.execute("CREATE TABLE IF NOT EXISTS guild" + str(ctx.guild.id) + " (uid,curr)")
        cur.execute("SELECT * FROM guild"+str(ctx.guild.id)+" WHERE uid = "+str(ctx.author.id))
        res = cur.fetchone()
        try: (uid, cr) = res
        except:
            cur.execute("INSERT INTO guild"+str(ctx.guild.id)+" (uid,curr) VALUES (?, ?)",(ctx.author.id,arg))
            conn.commit()
        finally:
            cur.execute("UPDATE guild"+str(ctx.guild.id)+" SET curr = ? WHERE uid = ?",(arg, ctx.author.id))
            conn.commit()
    @commands.command(help="//DEBUG//")
    async def start(self, ctx): 
        cur.execute("INSERT INTO guild (guild_id) VALUES ("+str(ctx.guild.id)+")")
        conn.commit()
    @commands.command()
    async def con(self, ctx):
        print("success")
    ###text format test###
    @commands.command(help="//DEBUG//")
    async def format(self, ctx,user: discord.User):
        await ctx.send("`{0} test ".format(ctx.author)+user.name+ "`")
    @commands.command(help="//DEBUG//")
    async def embed(self, ctx, arg1, arg2, cr, cb, cg):
        embedVar = discord.Embed(title=arg1, description=arg2, color=discord.Color.from_rgb(int(cr), int(cb), int(cg)))
        await ctx.send(embed=embedVar)