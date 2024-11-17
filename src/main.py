import discord
from discord.ext import commands
import os
import dotenv
import json
from src.logger import logger
from config.config_parser import config_load, config_create

dotenv.load_dotenv()
intents = discord.Intents.all()
bot = commands.Bot(intents=intents)

src_path = os.getcwd()

if not os.path.isfile(f"{src_path}/config/config.json"):
    config_create(src_path)

config = config_load(src_path)

enabled_cogs = config["cogs"]["enabled_cogs"]
for cog in enabled_cogs:
    bot.load_extension(f"cogs.{cog}")
logger.info(f"Loaded cogs: {",".join(enabled_cogs)}" )


@bot.event
async def on_ready():
    logger.info(f"{bot.user} is ready and online!")

bot.run(os.getenv('TOKEN'))