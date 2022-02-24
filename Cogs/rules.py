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

    @commands.is_owner()
    @commands.command(name='rulesbanner',
                      description='rulesbanner',
                      usage='rulesbanner',
                      cls=Command,
                      access=0)
    async def rulesbanner(self, context):
        client = self.client

        file = discord.File(fp=f'Assets/Rules.png')
        await context.send(file=file)
        await asyncio.sleep(0.05)
        await context.message.delete()
    @commands.is_owner()
    @commands.command(name='infobanner',
                      description='infobanner',
                      usage='infobanner',
                      cls=Command,
                      access=0)
    async def infobanner(self, context):
        client = self.client

        file = discord.File(fp=f'Assets/Information.png')
        await context.send(file=file)
        await asyncio.sleep(0.05)
        await context.message.delete()

    @commands.is_owner()
    @commands.command(name='rules',
                      description='rules',
                      usage='rules',
                      cls=Command,
                      access=0)
    async def rules(self, context):
        client = self.client

        embed = discord.Embed(
            title='Rules',
            description=f'''
<:_1:946199264353189919> Avoid Spam at all cost. This includes:
​ ​ ​ ​ ​ ​ ​ ​ ​ ​ ​• All forms of Zalgo, Emoticon, or One Line spam
​ ​ ​ ​ ​ ​ ​ ​ ​ ​ ​• Image/File/Link spam
​ ​ ​ ​ ​ ​ ​ ​ ​ ​ ​• Voice spam (On Voice channels)
​ ​ ​ ​ ​ ​ ​ ​ ​ ​ ​• DMs with other users of the server

<:_2:946199264323833896> Posts containing self harm, violence, or pornographic material are not allowed under any circumstances. This includes mild or suggestive content of this nature.

<:_3:946199264344830052> Respect each other in DMs and chat within the server. Attacking other members of this Discord for their ethnicity, religion, or beliefs is not welcome here.

<:_4:946199264273502208> Avoid pestering Moderators with messages. Mods will get back to you as soon as possible, and will review any proof of attacks. (We have logs.)

<:_5:946199264231563284> Hate speech is not tolerated and will lead to a ban, no matter the context.

<:_6:946199264202211388> Respect Chim's privacy.

<:_7:946199264252538980> Do not use this server in order to promote your or other's streams or content. Sharing your or other's videos is ok, but please avoid doing this in excess. (Music/Meme/Trending video sharing is ok.)

<:_8:946199264256720916> Avoid making posts related to illegal or restricted substances. Discussions regarding alcohol are allowed as long as you don't encourage others to consume it. Some members are under the legal drinking age.

<:_9:946199264252547173> Refrain from posting about controversial or political topics. This is a free speech server, but this is in place to avoid arguments between users.

<:_10:946199264252547172> You must be 13 years or older to be a part of this Discord community.
                        
**Failing to follow these rules may result in a warning, penalty, or ban.**''',
            colour=client.config['embed']['colour']
        )
        embed.set_footer(text=client.config['embed']['footer']['text'], icon_url=client.config['embed']['footer']['url'])
        await context.send(embed=embed)
        await asyncio.sleep(0.05)
        await context.message.delete()

    @commands.is_owner()
    @commands.command(name='info',
                      description='info',
                      usage='info',
                      cls=Command,
                      access=0)
    async def info(self, context):
        client = self.client
        embed = discord.Embed(
            title="Information",
            description='''
To unlock access to my Patreon Vanilla Minecraft server, you must sign up at the Pro Tier or above on my Patreon Page.

For access to the Attack of the B-Team Patreon Server you'll need to sign up at the Pro+ Tier or above.

---------------------

Links:
• [Patreon](http://www.patreon.com/ChimneySwift11)
• [Twitch](https://www.twitch.tv/ChimneySwift11)
• [YouTube](http://www.youtube.com/ChimneySwift11)
• [Twitter](http://www.twitter.com/ChimneySwift11)
• [Facebook](http://www.facebook.com/ChimneySwift11)
• [Instagram](http://www.instagram.com/PleaseStandByPhotography)
• [Oooh](https://unlock.oooh.tv/154)''',
            colour=client.config['embed']['colour']
        )
        embed.set_footer(text=client.config['embed']['footer']['text'], icon_url=client.config['embed']['footer']['url'])
        await context.send(embed=embed)
        await asyncio.sleep(0.05)
        await context.message.delete()

    @commands.is_owner()
    @commands.command(name='rules2',
                      description='rules2',
                      usage='rules2',
                      cls=Command,
                      access=0)
    async def rules2(self, context):
        client = self.client
        embed = discord.Embed(
            title='Rules',
            colour=client.config['embed']['colour']
        )
        embed.add_field(name='<:_1:945812659092197407>', value='Avoid Spam at all cost. This includes:\n ​ ​ ​ ​ ​ ​ ​ ​ ​ ​ ​• All forms of Zalgo, Emoticon, or One Line spam\n ​ ​ ​ ​ ​ ​ ​ ​ ​ ​ ​• Image/File/Link spam\n ​ ​ ​ ​ ​ ​ ​ ​ ​ ​ ​• Voice spam (On Voice channels)\n ​ ​ ​ ​ ​ ​ ​ ​ ​ ​ ​• DMs with other users of the server\n\n** **', inline=False)
        embed.add_field(name='<:_2:945812659306115072>',
                        value='Respect each other in DMs and chat within the server. Attacking other members of this Discord for their ethnicity, religion, or beliefs is not welcome here.\n\n** **',
                        inline=False)
        embed.add_field(name='<:_3:945812659343859723>', value='Respect each other in DMs and chat within the server. Attacking other members of this Discord for their ethnicity, religion, or beliefs is not welcome here.\n\n** **', inline=False)
        embed.add_field(name='<:_4:945812659113185291>', value='Avoid pestering Moderators with messages. Mods will get back to you as soon as possible, and will review any proof of attacks. (We have logs.)\n\n** **', inline=False)
        embed.add_field(name='<:_5:945812659486486568>', value='Hate speech is not tolerated and will lead to a ban, no matter the context.\n\n** **', inline=False)
        embed.add_field(name='<:_6:945812659914276965>', value='Respect Chim\'s privacy.\n\n** **', inline=False)
        embed.add_field(name='<:_7:945812659457118238>', value='Do not use this server in order to promote your or other\'s streams or content. Sharing your or other\'s videos is ok, but please avoid doing this in excess. (Music/Meme/Trending video sharing is ok.)\n\n** **', inline=False)
        embed.add_field(name='<:_8:945812659570352138>', value='Avoid making posts related to illegal or restricted substances. Discussions regarding alcohol are allowed as long as you don\'t encourage others to consume it. Some members are under the legal drinking age.\n\n** **', inline=False)
        embed.add_field(name='<:_9:945812659775885343>', value='Refrain from posting about controversial or political topics. This is a free speech server, but this is in place to avoid arguments between users.\n\n** **', inline=False)
        embed.add_field(name='<:_10_1_2:945816782160150578><:_10_2_2:945816782348910623>', value='You must be 13 years or older to be a part of this Discord community.\n\n** **', inline=False)

        embed.set_footer(text=client.config['embed']['footer']['text'], icon_url=client.config['embed']['footer']['url'])
        await context.send(embed=embed)
        await asyncio.sleep(0.05)
        await context.message.delete()

def setup(client):
    client.add_cog(Rules(client))
