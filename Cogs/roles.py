import json

import discord
from discord.ext import commands

from Utils.classes import Command, PersistentView, PersistentView2


class Roles(commands.Cog):
    def __init__(self, client):
        self.client = client

        with open("roles.json", encoding='utf8') as file:
            self.roles = json.load(file)

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        client = self.client

        if payload.message_id == client.bot['messages']['roles']['message']:
            channel = client.get_channel(client.bot['messages']['roles']['channel'])
            user = payload.member

            if payload.emoji.name in self.roles:
                role = discord.utils.get(channel.guild.roles, id=self.roles[payload.emoji.name])
                await user.add_roles(role)

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        client = self.client

        if payload.message_id == client.bot['messages']['roles']['message']:
            channel = client.get_channel(client.bot['messages']['roles']['channel'])
            user = discord.utils.get(channel.guild.members, id=payload.user_id)

            if payload.emoji.name in self.roles:
                role = discord.utils.get(channel.guild.roles, id=self.roles[payload.emoji.name])
                await user.remove_roles(role)

    @commands.command(name='roles',
                      description='roles',
                      usage='roles',
                      cls=Command,
                      access=0)
    async def roles(self, context):
        client = self.client

        embed = discord.Embed(
            title='Roles',
            description=f'React to toggle notifications for the following:\n\n🦜 - Sea of Thieves\n☠ - Elder Scrolls Online',
            colour=client.config['embed']['colour']
        )
        message = await context.send(embed=embed)

        await message.add_reaction("🦜")
        await message.add_reaction("☠")

    @commands.command(name='roles2',
                      description='roles2',
                      usage='roles2',
                      cls=Command,
                      access=0)
    async def roles2(self, context):
        client = self.client

        embed = discord.Embed(
            title='Roles',
            description=f'Press the below buttons to toggle notifications for the following:\n\n- Sea of Thieves\n- Elder Scrolls Online',
            colour=client.config['embed']['colour']
        )
        await context.send(embed=embed, view=PersistentView())

    @commands.command(name='roles3',
                      description='roles3',
                      usage='roles3',
                      cls=Command,
                      access=0)
    async def roles3(self, context):
        client = self.client

        embed = discord.Embed(
            title='Roles',
            description=f'Select the options from the dropdown to toggle notifications for the following:\n\n- Sea of Thieves\n- Elder Scrolls Online',
            colour=client.config['embed']['colour']
        )
        await context.send(embed=embed, view=PersistentView2())


def setup(client):
    client.add_cog(Roles(client))
