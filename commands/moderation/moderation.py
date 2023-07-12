from discord.ext import commands
import discord


class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def restrict(self, ctx, member: discord.Member):
        """Restrict a member from sending messages temporarily"""
        # Get the restricted role for your server
        restricted_role = discord.utils.get(ctx.guild.roles, name="Restricted")

        if restricted_role is None:
            # If the role doesn't exist, create it
            restricted_role = await ctx.guild.create_role(name="Restricted", reason="Used for restricting members")

            # Set the channel permissions for the role
            overwrite = discord.PermissionOverwrite(send_messages=False)
            for channel in ctx.guild.text_channels:
                await channel.set_permissions(restricted_role, overwrite=overwrite)

        # Add the restricted role to the member
        await member.add_roles(restricted_role)

        await ctx.send(
            f"DarkVa'bot fait usage de la force sur le pauvre '{member.mention} qui est bien incapable de parler pour le moment...")

    @commands.command()
    async def unrestrict(self, ctx, member: discord.Member):
        """Remove message restriction from a member"""
        # Get the restricted role for your server
        restricted_role = discord.utils.get(ctx.guild.roles, name="Restricted")

        if restricted_role is not None and restricted_role in member.roles:
            # Remove the restricted role from the member
            await member.remove_roles(restricted_role)
            await ctx.send(
                f"DarkVa'bot dans sa grande bonté, relache son emprise sur {member.mention}. Espérons qu'il ai compris la leçon")
        else:
            await ctx.send(f"{member.mention} is not currently restricted.")


async def setup(bot):
    await bot.add_cog(Moderation(bot))
