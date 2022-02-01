import discord
from discord.ext import commands

from Utils.classes import Command


class ModeratorCommands(commands.Cog):
    def __init__(self, client):
        self.client = client


def setup(client):
    client.add_cog(ModeratorCommands(client))
