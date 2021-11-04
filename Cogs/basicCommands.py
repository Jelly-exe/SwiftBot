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

    @commands.command(name='nick',
                      description='Set nick',
                      usage='nick [user] [nick]')
    async def nick(self, context, user: discord.Member, *, nick):
        client = self.client

        if user.id == context.author.id:
            embed = discord.Embed(
                description='Cannot change your own nickname.',
                colour=client.config['embed']['colour']
            )

            await context.send(embed=embed)
            return

        try:
            await user.edit(nick=nick)
            embed = discord.Embed(
                description='Nickname changed.',
                colour=client.config['embed']['colour']
            )
            embed.set_footer(text=client.config['embed']['footer']['text'], icon_url=client.config['embed']['footer']['url'])

        except:
            embed = discord.Embed(
                description='Failed to change nickname.',
                colour=client.config['embed']['colour']
            )

        await context.send(embed=embed)


def setup(client):
    client.add_cog(BasicCommands(client))
