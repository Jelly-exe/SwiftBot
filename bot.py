import json
import os

import yaml

import discord
from discord import app_commands
from discord.ext import commands

import Utils.classes
from Utils import colours
from datetime import datetime

from Utils.classes import NoPermission


class SwiftBot(commands.Bot):
    def __init__(self):
        self.step = 0
        self.initial_extensions = []
        self.testingGuild = discord.Object(id=887781128046538812)

        with open("roles.json", encoding='utf8') as file:
            self.roles = json.load(file)

        print(f'{colours.OKGREEN}{self._displayStep()}. Setting allowed_mentions')
        allowed_mentions = discord.AllowedMentions(roles=False, everyone=False, users=True)

        print(f'{colours.OKGREEN}{self._displayStep()}. Setting activity')
        activity = discord.Activity(name='with the devs!', type=discord.ActivityType.playing)

        print(f'{colours.OKGREEN}{self._displayStep()}. Setting description')
        description = 'Bot made for the Chimneyswift11 Offical Discord'

        print(f'{colours.OKGREEN}{self._displayStep()}. Setting up intents')
        intents = discord.Intents.default()
        intents.members = True
        intents.guilds = True
        intents.presences = True
        intents.message_content = True

        print(f'{colours.OKGREEN}{self._displayStep()}. Reading configs\'s')
        self.bot = yaml.load(open("bot.yml", "r"), Loader=yaml.FullLoader)
        self.config = yaml.load(open("config.yml", "r"), Loader=yaml.FullLoader)

        print(f'{colours.OKGREEN}{self._displayStep()}. Initializing the bot')
        super().__init__(command_prefix=self._getPrefix,
                         help_command=None,
                         owner_id=278548721778688010,
                         activity=activity,
                         intents=intents,
                         allowed_mentions=allowed_mentions,
                         description=description,
                         case_insensitive=True)

        self.persistent_views_added = False

        print(f'{colours.OKGREEN}{self._displayStep()}. Setting the boot time')
        self.boot = datetime.now()

        print(f'{colours.OKGREEN}{self._displayStep()}. Setting the token')
        self.token = self.bot["token"] if not self.bot['dev'] else self.bot["dev_token"]

    async def setup_hook(self):
        await self._getCogs()
        for ext in self.initial_extensions:
            try:
                await self.load_extension(ext)
                print(f'{colours.OKGREEN}{self._displayStep()}. Loading {ext}')
            except Exception as error:
                print(f'{colours.FAIL}{self._displayStep()}. {ext} cannot be loaded. [{error}]')

    def _getPrefix(self, client, message):
        if self.bot["dev"]:
            return self.config["prefix"] * 2

        return self.config["prefix"]

    async def _getCogs(self):
        for i in os.listdir('Cogs'):
            if i.endswith('.py'):
                self.initial_extensions.append(f'Cogs.{i[:-3]}')

    def getToken(self):
        return self.token

    def _displayStep(self):
        self.step += 1
        return self.step

    async def on_ready(self):
        if not self.persistent_views_added:
            for key in self.roles["reaction"]:
                self.add_view(Utils.classes.RoleButtonsView(key))
            self.persistent_views_added = True

        await self.tree.sync(guild=self.testingGuild)

        print(f'{colours.OKCYAN}~~~~~~~~~~~~~')
        print(f'{colours.OKCYAN}Logged in as - ')
        print(f'{colours.OKCYAN}Name: {self.user.name}')
        print(f'{colours.OKCYAN}Id: {self.user.id}')
        print(f'{colours.OKCYAN}Time: {self.boot}')
        print(f'{colours.OKCYAN}~~~~~~~~~~~~~')
        print(f'{colours.OKCYAN}\n(Pterodactyl Bot Online)')

        if self.bot["dev"]:
            print(f'{colours.WARNING}\nDEV MODE')

    async def on_command_error(self, context, error):
        if isinstance(error, commands.CommandNotFound):
            return

        elif isinstance(error, commands.CommandOnCooldown):
            print(colours.FAIL + 'Error: Command on Cooldown')
            embed = discord.Embed(
                description=f'Currently on cooldown. Please wait {int(error.retry_after)} seconds before running again.',
                colour=self.config['embed']['colour']
            )
            await context.send(embed=embed)
            return

        elif isinstance(error, commands.BadArgument) or isinstance(error, commands.MissingRequiredArgument):
            print(colours.FAIL + 'Error: Missing Required Arguments')
            embed = discord.Embed(
                description=f'Invalid arguments passed. `{self.config["prefix"]}{context.command.usage}`',
                colour=self.config['embed']['colour']
            )
            await context.send(embed=embed)
            return

        elif isinstance(error, NoPermission):
            embed = discord.Embed(
                description=error.args[0],
                colour=self.config['embed']['colour'])
            await context.send(embed=embed)

        elif isinstance(error, commands.CheckFailure) or isinstance(error, RuntimeError):
            return

        else:
            embed = discord.Embed(
                description=f'{error.args[0]}\n\nPlease alert Jelly#6161 of this error.',
                colour=self.config['embed']['colour'])
            await context.send(embed=embed)
            raise error
