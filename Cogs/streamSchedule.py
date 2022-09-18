from typing import Literal

import discord
from discord import app_commands
from discord.ext import commands

from Utils.classes import Command


class StreamSchedule(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.schedule = {
            'Monday': {
                'game': 'Sea of Thieves',
                'time': 1647874800
            },
            'Tuesday': None,
            'Wednesday': None,
            'Thursday': None,
            'Friday': {
                'game': 'Minecraft',
                'time': 1647608400,
                'every': '2'
            },
            'Saturday': {
                'game': 'Sea of Thieves',
                'time': 1647702000
            },
            'Sunday': None
        }
        self.message = None

    def makeMessage(self):
        string = ''
        lowest = None

        for i in self.schedule:
            if self.schedule[i]:
                time = self.schedule[i]["time"]
                string += f'{i}: <t:{time}:t> - {self.schedule[i]["game"]}\n'
                if not lowest or time < self.schedule[lowest]["time"]:
                    lowest = i

        return [string, lowest]

    @commands.is_owner()
    @commands.command(name='ss',
                      description='Stream Schedule.',
                      usage='ss',
                      cls=Command,
                      access=0)
    async def ss(self, context):
        client = self.client
        stuff = self.makeMessage()
        embed = discord.Embed(
            title='Current Stream Schedule',
            description=stuff[0],
            colour=client.config['embed']['colour']
        )
        embed.add_field(name='Next Stream', value=f'The next stream will be **<t:{self.schedule[stuff[1]]["time"]}:R>**. Chim will be streaming **{self.schedule[stuff[1]]["game"]}**.')
        self.message = await context.send(embed=embed)

    @commands.is_owner()
    @commands.command(name='ss',
                      description='Stream Schedule.',
                      usage='ss',
                      cls=Command,
                      access=0)
    async def ss(self, context):
        client = self.client
        stuff = self.makeMessage()
        embed = discord.Embed(
            title='Current Stream Schedule',
            description=stuff[0],
            colour=client.config['embed']['colour']
        )
        embed.add_field(name='Next Stream', value=f'The next stream will be **<t:{self.schedule[stuff[1]]["time"]}:R>**. Chim will be streaming **{self.schedule[stuff[1]]["game"]}**.')
        self.message = await context.send(embed=embed)

    @app_commands.command(description='Set the stream schedule time and game on a specified day')
    @app_commands.guilds(discord.Object(id=887781128046538812))
    @app_commands.describe(day='Day')
    @app_commands.describe(time='Time - Leave both Time and Game blank for no stream')
    @app_commands.describe(game='Game - Leave both Time and Game blank for no stream')
    async def set(self, interaction: discord.Interaction, day: Literal['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'], time: str = None, game: str = None):
        await interaction.response.send_message(f'{day} {time} {game}')

    @app_commands.command(description='Override the stream schedule for a specific date')
    @app_commands.guilds(discord.Object(id=887781128046538812))
    @app_commands.describe(date='Date - DD/MM/YYYY')
    @app_commands.describe(time='Time - Leave both Time** and Game blank for no stream')
    @app_commands.describe(game='Game - Leave both Time** and Game blank for no stream')
    async def override(self, interaction: discord.Interaction, date: str, time: str = None, game: str = None):
        await interaction.response.send_message(f'{date} {time} {game}')


async def setup(client):
    await client.add_cog(StreamSchedule(client))
