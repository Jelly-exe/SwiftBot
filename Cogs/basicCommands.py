import discord
from discord.ext import commands

from Utils.classes import Command


class BasicCommands(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name='ping',
                      description='Gives the bot latency in milliseconds.',
                      usage='ping',
                      cls=Command,
                      access=0)
    async def ping(self, context):
        client = self.client

        embed = discord.Embed(
            description=f'🏓 Pong! Latency: `{round(client.latency * 1000)}ms`',
            colour=client.config['embed']['colour']
        )
        await context.send(embed=embed)


def setup(client):
    client.add_cog(BasicCommands(client))
