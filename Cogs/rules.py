import json

import discord
from discord.ext import commands

from Utils.classes import Command, PersistentView, PersistentView2, PersistentView3


class Rules(commands.Cog):
    def __init__(self, client):
        self.client = client

        with open("roles.json", encoding='utf8') as file:
            self.roles = json.load(file)

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        client = self.client

        if payload.message_id == client.bot['messages']['rules']['message']:
            channel = client.get_channel(client.bot['messages']['rules']['channel'])
            user = payload.member

            if payload.emoji.name in self.roles:
                role = discord.utils.get(channel.guild.roles, id=self.roles[payload.emoji.name])
                await user.add_roles(role)

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        client = self.client

        if payload.message_id == client.bot['messages']['rules']['message']:
            channel = client.get_channel(client.bot['messages']['rules']['channel'])
            user = discord.utils.get(channel.guild.members, id=payload.user_id)

            if payload.emoji.name in self.roles:
                role = discord.utils.get(channel.guild.roles, id=self.roles[payload.emoji.name])
                await user.remove_roles(role)

    @commands.command(name='rules',
                      description='rules',
                      usage='rules',
                      cls=Command,
                      access=0)
    async def rules(self, context):
        client = self.client

        embed = discord.Embed(
            title='Rules',
            description=f'<Insert rules here>\n\nPlease react below to accept the rules and get the @Swifter role',
            colour=client.config['embed']['colour']
        )
        message = await context.send(embed=embed)

        await message.add_reaction("☑️")

    @commands.command(name='rules2',
                      description='rules2',
                      usage='rules2',
                      cls=Command,
                      access=0)
    async def rules2(self, context):
        client = self.client

        embed = discord.Embed(
            title='Rules',
            description=f'<Insert rules here>\n\nPlease press the button below to accept the rules and get the @Swifter role',
            colour=client.config['embed']['colour']
        )
        await context.send(embed=embed, view=PersistentView3())


def setup(client):
    client.add_cog(Rules(client))
