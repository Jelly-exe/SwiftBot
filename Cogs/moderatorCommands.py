import discord
from discord.ext import commands

from Utils.classes import Command


class ModeratorCommands(commands.Cog):
    def __init__(self, client):
        self.client = client


async def setup(client):
    await client.add_cog(ModeratorCommands(client))
