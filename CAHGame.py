from discord.ext import commands, tasks
import discord
import asyncio

class CAH(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

def setup(bot):
	bot.add_cog(CAH(bot))