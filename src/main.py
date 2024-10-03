import discord
from discord.ext import commands
import os, dotenv, json

dotenv.load_dotenv()
intents = discord.Intents.all()
intents.message_content = True 
intents.members = True
bot = commands.Bot(intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")

with open(f"{os.getcwd()}/src/config/config.json") as rconfig:
    config = json.load(rconfig)
enabled_cogs = config["cogs"]["enabled_cogs"]
for cog in enabled_cogs:
    bot.load_extension(f"cmds.{cog}")

bot.run(os.getenv('TOKEN')) 