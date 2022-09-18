import asyncio
import json

import discord
from discord.ext import commands

from Utils.classes import Command, RoleButtonsView


class Roles(commands.Cog):
    def __init__(self, client):
        self.client = client

        with open("roles.json", encoding='utf8') as file:
            self.roles = json.load(file)

    @commands.is_owner()
    @commands.command(name='rolesbanner',
                      description='rolesbanner',
                      usage='rolesbanner',
                      cls=Command,
                      access=0)
    async def rolesbanner(self, context):
        client = self.client

        file = discord.File(fp=f'Assets/Choose_Your_Roles.png')
        await context.send(file=file)
        await asyncio.sleep(0.05)
        await context.message.delete()

    @commands.command(name='rolecount',
                      description='rolecount',
                      usage='rolecount',
                      cls=Command,
                      access=0)
    async def rolecount(self, context):
        client = self.client

        string = ""
        for key in self.roles["reaction"]:
            for role in self.roles["reaction"][key]:
                activeRole = discord.utils.get(context.guild.roles, id=int(self.roles["reaction"][key][role]["role"]))
                string += f'{self.roles["reaction"][key][role]["name"]} - {len(activeRole.members)}\n'

        embed = discord.Embed(
            title="Reaction Role Member Counts",
            description=string,
            colour=client.config['embed']['colour']
        )

        embed.set_footer(text=client.config['embed']['footer']['text'], icon_url=client.config['embed']['footer']['url'])
        await context.send(embed=embed)

    @commands.is_owner()
    @commands.command(name='roles',
                      description='roles',
                      usage='roles',
                      cls=Command,
                      access=0)
    async def roles(self, context):
        client = self.client

        for key in self.roles["reaction"]:
            string = ""
            for role in self.roles["reaction"][key]:
                if "display" in self.roles["reaction"][key][role]:
                    string += f'\n• {self.roles["reaction"][key][role]["display"]}'
                else:
                    string += f'\n• **{self.roles["reaction"][key][role]["name"]}**'

            embed = discord.Embed(
                title=self.roles["reactionContent"][key]["title"],
                description=self.roles["reactionContent"][key]["content"].replace("<roles>", string),
                colour=client.config['embed']['colour']
            )
            embed.set_footer(text=client.config['embed']['footer']['text'], icon_url=client.config['embed']['footer']['url'])
            # embed.set_image(url=self.roles["reactionContent"][key]["image"])
            await context.send(embed=embed, view=RoleButtonsView(key))

        await asyncio.sleep(0.05)
        await context.message.delete()

    @commands.Cog.listener()
    async def on_member_join(self, member):
        client = self.client

        # channel = discord.utils.get(member.guild.channels, id=client.bot["channels"]["welcome"])
        # embed = discord.Embed(
        #     title=f'Welcome to the server {member.name}!',
        #     description=f'Please make sure to read <#{client.bot["channels"]["rules"]}>!',
        #     colour=client.config['embed']['colour']
        # )
        # embed.set_footer(text=client.config['embed']['footer']['text'], icon_url=client.config['embed']['footer']['url'])
        #
        # embed.set_thumbnail(url=member.avatar.url)
        # await channel.send(member.mention, embed=embed)

        role = discord.utils.get(member.guild.roles, id=self.roles["swifter"])
        await asyncio.sleep(60 * 10)
        await member.add_roles(role)


async def setup(client):
    await client.add_cog(Roles(client))
