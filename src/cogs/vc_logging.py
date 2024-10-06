import discord
import datetime
from discord.ext import commands
from config.config_parser import config_load
from logger import logger

config = config_load()

class VCLogging(commands.Cog):
    def __init__(self, bot): 
        self.bot = bot

    @commands.Cog.listener()
    async def on_voice_state_update(self, member: discord.Member, before: discord.VoiceState, after:discord.VoiceState):
        if before.channel is not None:
            embedmsg = discord.Embed(
                description=f"<@{member.id}> has left the voice channel.",
                timestamp=datetime.datetime.now(),
                footer=discord.EmbedFooter(text=f"#{before.channel}"),
                color=discord.Colour.red()
                )
            embedmsg.set_author(name=member.name, icon_url=member.avatar)
            await before.channel.send(embed=embedmsg)
            logger.info(f"User {member.name} ({member.id}) has left the voice channel {before.channel} ({before.channel.id}).")

        if after.channel is not None:
            embedmsg = discord.Embed(
                description=f"<@{member.id}> has joined the voice channel.",
                timestamp=datetime.datetime.now(),
                footer=discord.EmbedFooter(text=f"#{after.channel}"),
                color=discord.Colour.green()
                )
            embedmsg.set_author(name=member.name, icon_url=member.avatar)
            await after.channel.send(embed=embedmsg)
            logger.info(f"User {member.name} ({member.id}) has joined the voice channel {after.channel} ({after.channel.id}).")

def setup(bot): 
    bot.add_cog(VCLogging(bot)) 