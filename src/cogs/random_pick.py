import discord
import random
from discord.ext import commands
from logger import logger

class RandomPick(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    randompick = discord.SlashCommandGroup("pick", "Random pick related commands")

    @randompick.command()
    @discord.option("sequence", str, description="Provide sequence to be picked.")
    @discord.option("amount", int, description="The amount to be picked. Default value is 1", default = 1)
    @discord.option("separator", str , description="The separator of the sequence. Leave empty for space.", default=" ")
    async def list(self, ctx: discord.ApplicationContext, sequence: str, amount: int = 1, separator: str = " "):
        """
        Pick one or more objects ramdomly from the given sequence.
        """
        if separator not in sequence:
            await ctx.respond(f"The separator (`{separator}`) is not in the given sequence. Please give the separator corresponding to the sequence.")
            return
        else:
            seq_list = sequence.split(sep=separator)
            if len(seq_list) < amount:
                await ctx.respond(f"The amount to be picked (`{amount}`) must be less than the given sequence.")
                return
            logger.info(f"User {ctx.author} used command: \"{ctx.command} {sequence} {amount} {separator}\" in channel {ctx.channel} ({ctx.channel_id}).")
            n = 0
            response = []
            while n < amount:
                picked = seq_list[random.randint(0,len(seq_list)-1)]
                response.append(picked)
                seq_list.remove(picked)
                n += 1
            await ctx.respond(f"{separator}".join(response))
    
    @randompick.command()
    @discord.option("start", int, description="The start value of the number range.")
    @discord.option("stop", int, description="The stop value of the number range.")
    @discord.option("step", int, description="The step of the number range. Default value is 1.", default=1)
    @discord.option("amount", int, description="The amount to be picked. Default value is 1.", default=1)
    async def range(self, ctx: discord.ApplicationContext, start: int, stop: int, step: int = 1, amount: int = 1):
        """
        Pick one or more numbers ramdomly from the given range.
        """
        seq_list = [i for i in range(start, stop, step)]
        if len(seq_list) < amount:
            await ctx.respond(f"The amount to be picked (`{amount}`) must be less than the given sequence.")
            return
        logger.info(f"User {ctx.author} used command: \"{ctx.command} {start} {stop} {step} {amount}\" in channel {ctx.channel} ({ctx.channel_id}).")
        n = 0
        response = []
        while n < amount:
            picked = seq_list[random.randint(0,len(seq_list)-1)]
            response.append(str(picked))
            seq_list.remove(picked)
            n += 1
        await ctx.respond(f", ".join(response))

def setup(bot):
    bot.add_cog(RandomPick(bot))