import asyncio
import json

import discord
from discord.ext import commands

from Utils.classes import Command


class Rules(commands.Cog):
    def __init__(self, client):
        self.client = client

        with open("roles.json", encoding='utf8') as file:
            self.roles = json.load(file)

    @commands.command(name='rules',
                      description='rules',
                      usage='rules',
                      cls=Command,
                      access=0)
    async def rules(self, context):
        client = self.client

        embed = discord.Embed(
            title='Rules',
            description=f'<Insert rules here>',
            colour=client.config['embed']['colour']
        )
        await context.send(embed=embed)
        await asyncio.sleep(0.05)
        await context.message.delete()


def setup(client):
    client.add_cog(Rules(client))
