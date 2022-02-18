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
    @commands.command(name='rules',
                      description='rules',
                      usage='rules',
                      cls=Command,
                      access=0)
    async def rules(self, context):
        client = self.client

        embed = discord.Embed(
            title='Rules',
            description=f'''1. Avoid Spam at all cost. (This includes)\n    • All forms of Zalgo, Emoticon or One Line spam.\n    • Image/File/Link spam.\n    • Voice spam (On Voice channels)\n    • DMs with other users of the server.
                        
                        2. Post containing self harm, violence or pornographic material is not allowed under any circumstances. This includes mild or suggestive content.
                        
                        3. Respect others in both DMs or chat within the server. Attacking other members of chat for their ethnicity/religion/beliefs is not welcomed here.
                        
                        4. Avoid pestering mods with messages, mods will get back to you as soon as possible and review any proof of attacks. (We have logs)
                        
                        5. Hate speech is not tolerable and will lead to a ban no matter the context.
                        
                        6. Respect Chim's privacy.
                        
                        7. Do not use this server in order to promote your or other's streams or content. Sharing yours or others videos is ok, but avoid overdoing it. (Music/Meme/Trending video sharing is ok)
                        
                        8. Avoid posting of any topic related to illegal substances (e.g. Weed, Cocaine, Tobacco, etc.). Beer is allowed as long as you don't encourage others to do it, some members are under 18/21 and drinking might not be allowed in their regions.
                        
                        9. Do not post content of controversial/political topic in any way shape or form. This is a free speech server but we want to avoid any confrontation between users.
                        
                        10. You must be 13 or older in order to be a part of this community.
                        
                        
                        **Failing to follow these rules may result on a warning, penalty or ban.**''',
            colour=client.config['embed']['colour']
        )
        embed.set_footer(text=client.config['embed']['footer']['text'], icon_url=client.config['embed']['footer']['url'])
        embed2 = discord.Embed(
            title="Information",
            description='''
                        To unlock access to my Patreon Vanilla Minecraft server you must sign up at the Pro Tier or above on my Patreon Page.
                        
                        For access to the Attack of the B-Team Patreon Server you'll need to sign up at the Pro+ Tier or above.
            
                        ---------------------
                        
                        Links:
                        • [Patreon](http://www.patreon.com/ChimneySwift11)
                        • [YouTube](http://www.youtube.com/ChimneySwift11)
                        • [Twitter](http://www.twitter.com/ChimneySwift11)
                        • [Facebook](http://www.facebook.com/ChimneySwift11)
                        • [Instagram](http://www.instagram.com/PleaseStandByPhotography)''',
            colour=client.config['embed']['colour']
        )
        embed2.set_footer(text=client.config['embed']['footer']['text'], icon_url=client.config['embed']['footer']['url'])
        await context.send(embed=embed)
        await context.send(embed=embed2)
        await asyncio.sleep(0.05)
        await context.message.delete()


def setup(client):
    client.add_cog(Rules(client))
