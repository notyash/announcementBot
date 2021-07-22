import discord
from discord.ext import commands
from discord.utils import get


class Functions(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.link = "<https://discord.com/api/oauth2/authorize?client_id=867820946571919442&permissions=8&scope=bot>"
        self.embed = discord.Embed(colour=discord.Color.from_rgb(30, 144, 255))

    @commands.command(name="send", aliases=["msg"])
    async def send_message(self, ctx, *, message):
        guild_names = []
        for guild in self.bot.guilds:
            channel = get(guild.channels, name="announcement")
            guild_names.append(guild.name)

            self.embed.description = message
            msg = await channel.send(embed=self.embed)
            await msg.add_reaction("✅")

        await ctx.send(f"Sent messages to **{', '.join(guild_names)}** servers.")

    @commands.command(name="invite", aliases=["join", "add"])
    async def invite_link(self, ctx):
        self.embed.description = f"Use this link to invite the bot to your server.\n{self.link}"
        msg = await ctx.send(embed=self.embed)
        await msg.add_reaction("✅")


def setup(bot):
    bot.add_cog(Functions(bot))
