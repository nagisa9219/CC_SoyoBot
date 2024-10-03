import discord, datetime
from types import NoneType
from discord.ext import commands
from config.config_parser import config_load

config = config_load()

class VCLogging(commands.Cog):
    def __init__(self, bot): 
        self.bot = bot

    @commands.Cog.listener()
    async def on_voice_state_update(self, member: discord.Member, before: discord.VoiceState, after:discord.VoiceState):
        print(f"{member}, {before.channel}->{after.channel}")
        print(f"{before.channel is not None}, {after.channel is not None}")
        if before.channel is not None:
            print(f"{member} leaved {before.channel}.")
            embedmsg = discord.Embed(
                description=f"<@{member.id}> has left the voice chat.",
                timestamp=datetime.datetime.now(),
                footer=discord.EmbedFooter(text=f"#{before.channel}"),
                color=discord.Colour.red()
                )
            embedmsg.set_author(name=member.name, icon_url=member.avatar)
            await before.channel.send(embed=embedmsg)

        if after.channel is not None:
            print(f"{member} joined {after.channel}.")
            embedmsg = discord.Embed(
                description=f"<@{member.id}> has joined the voice chat.",
                timestamp=datetime.datetime.now(),
                footer=discord.EmbedFooter(text=f"#{after.channel}"),
                color=discord.Colour.green()
                )
            embedmsg.set_author(name=member.name, icon_url=member.avatar)
            await after.channel.send(embed=embedmsg)

def setup(bot): 
    bot.add_cog(VCLogging(bot)) 