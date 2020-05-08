import discord
from discord.ext import commands
from utils import permissions, default

class Mod(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.guild_only()
    @permissions.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason: str = None):
        """ Kicks a user from the current server. """
        if await permissions.check_priv(ctx, member):
            return
        try:
            await member.kick(reason=default.responsible(ctx.author, reason))
            await ctx.send(default.actionmessage("kicked"))
        except Exception as e:
            await ctx.send("ofc!\n```", e, "```")

    @commands.command()
    @commands.guild_only()
    @permissions.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason: str = None):
        """ Bans user from the server """
        if await permissions.check_priv(ctx, member):
            return
        try:
            await member.ban(reason=default.responsible(ctx.author, reason))
            await ctx.send(default.responsible("banned"))
        except Exception as e:
            await ctx.send("uh oh\n```", e, "```")

    @commands.command()
    @commands.guild_only()
    @permissions.has_permissions(manage_messages=True)
    async def purge(self, ctx, amount: int, member):
        """ 
        Delete a specific amount of messages. Fails if you don't have perms. 
        """
        if await permissions.check_priv(ctx, member):
            return
        try:
            await ctx.channel.purge(limit=amount + 1)
        except discord.Forbidden:
            await ctx.send("i don\'t have permissions to manage messages.")


def setup(bot):
    bot.add_cog(Mod(bot))