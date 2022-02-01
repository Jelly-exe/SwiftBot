import json

import discord
from discord.ext import commands


class Command(commands.Command):
    def __init__(self, *args, **kwargs):
        self.access = kwargs.pop('access')
        super().__init__(*args, **kwargs)


class Group(commands.Group):
    def __init__(self, *args, **kwargs):
        self.access = kwargs.pop('access')
        super().__init__(*args, **kwargs)


class NoPermission(commands.CheckFailure):
    pass


class RoleButton(discord.ui.Button):
    def __init__(self, label: str, key: str):
        super().__init__(style=discord.ButtonStyle.primary, label=label, custom_id=key)

        with open("roles.json", encoding='utf8') as file:
            self.roles = json.load(file)

        self.key = key

    async def callback(self, interaction: discord.Interaction):
        role = discord.utils.get(interaction.guild.roles, id=int(self.roles["reaction"][self.key]["role"]))
        user = discord.utils.get(interaction.guild.members, id=interaction.user.id)
        thing = None
        if role in user.roles:
            await user.remove_roles(role)
            thing = '<:red_minus:938174266896187474> Removed role'
        else:
            await user.add_roles(role)
            thing = '<:green_plus:938174266959102013> Added role'

        await interaction.response.send_message(f'{thing} <@&{role.id}>', ephemeral=True)


class RoleButtonsView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

        with open("roles.json", encoding='utf8') as file:
            self.roles = json.load(file)

        for role in self.roles["reaction"]:
            self.add_item(RoleButton(self.roles["reaction"][role]["name"], role))
