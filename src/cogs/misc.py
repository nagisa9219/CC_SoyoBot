import discord
from discord.ext import commands
from src.logger import logger

class MiscCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    misc = discord.SlashCommandGroup("misc", "test")

    @misc.command()
    @discord.option("text", str, description="text")
    async def say(self, ctx: discord.ApplicationContext, text: str):
        """
        say
        """
        await ctx.send_response(content="ok", ephemeral=True)
        await ctx.channel.send(text)

def setup(bot):
    bot.add_cog(MiscCommand(bot))