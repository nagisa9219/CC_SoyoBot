import discord
from discord.ext import commands

class VCLogging(commands.Cog): # create a class for our cog that inherits from commands.Cog
    # this class is used to create a cog, which is a module that can be added to the bot

    def __init__(self, bot): # this is a special method that is called when the cog is loaded
        self.bot = bot

    @discord.slash_command() # creates a prefixed command
    async def hello(self, ctx): # all methods now must have both self and ctx parameters
        await ctx.respond('Hello!')

    @discord.slash_command() # we can also add application commands
    async def goodbye(self, ctx):
        await ctx.respond('Goodbye!')

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        print(f"Received {message.content}")

    @commands.Cog.listener()
    async def on_voice_channel_status_update(self, channel, before, after): # call when receive voice channel status updated.
        print(f"Received channel {channel} updated. ({before} -> {after})")
    
    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after): # call when received member voice state updated.
        print(f"Received member voice state updated: {member}. ({before} -> {after})")

def setup(bot): # this is called by Pycord to setup the cog
    bot.add_cog(VCLogging(bot)) # add the cog to the bot