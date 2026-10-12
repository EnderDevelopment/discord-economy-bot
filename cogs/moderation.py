import discord
from discord.ext import commands
from discord import app_commands

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="ban", description="Ban a user from the server")
    async def ban(self, interaction: discord.Interaction, user: discord.User, delete_days: int = 0, reason: str = None):
        await interaction.guild.ban(user, delete_message_days=delete_days, reason=reason)
        await interaction.response.send_message(f"Banned {user.mention}", ephemeral=True)

    @app_commands.command(name="unban", description="Unban a user from the server")
    async def unban(self, interaction: discord.Interaction, user: discord.User):
        await interaction.guild.unban(user)
        await interaction.response.send_message(f"Unbanned {user.mention}", ephemeral=True)

    @app_commands.command(name="kick", description="Kick a user from the server")
    async def kick(self, interaction: discord.Interaction, user: discord.User, reason: str = None):
        await interaction.guild.kick(user, reason=reason)
        await interaction.response.send_message(f"Kicked {user.mention}", ephemeral=True)

    @app_commands.command(name="warn", description="Warn a user")
    async def warn(self, interaction: discord.Interaction, user: discord.User, reason: str = None):
        await interaction.response.send_message(f"Warned {user.mention}", ephemeral=True)

    @app_commands.command(name="clear_warn", description="Clear a warning for a user")
    async def clear_warn(self, interaction: discord.Interaction, user: discord.User):
        await interaction.response.send_message(f"Cleared warnings for {user.mention}", ephemeral=True)

    @app_commands.command(name="timeout", description="Timeout a user")
    async def timeout(self, interaction: discord.Interaction, user: discord.User, duration: str, reason: str):
        await interaction.response.send_message(f"Timed out {user.mention} for {duration}", ephemeral=True)

    @app_commands.command(name="untimeout", description="Remove timeout from a user")
    async def untimeout(self, interaction: discord.Interaction, user: discord.User):
        await interaction.response.send_message(f"Removed timeout from {user.mention}", ephemeral=True)

    @app_commands.command(name="say", description="Make the bot say something")
    async def say(self, interaction: discord.Interaction, message: str):
        await interaction.response.send_message(message)

    @app_commands.command(name="purge", description="Purge messages from the channel")
    async def purge(self, interaction: discord.Interaction, amount: int):
        await interaction.channel.purge(limit=amount)
        await interaction.response.send_message(f"Purged {amount} messages", ephemeral=True)

    @app_commands.command(name="dm", description="Send a DM to a user")
    async def dm(self, interaction: discord.Interaction, user: discord.User, message: str):
        await user.send(message)
        await interaction.response.send_message(f"Sent DM to {user.mention}", ephemeral=True)

    @app_commands.command(name="cases", description="View moderation cases for a user")
    async def cases(self, interaction: discord.Interaction, user: discord.User):
        await interaction.response.send_message(f"Moderation cases for {user.mention}", ephemeral=True)

    @app_commands.command(name="usernotes_add", description="Add a user note")
    async def usernotes_add(self, interaction: discord.Interaction, user: discord.User, note_type: str):
        await interaction.response.send_message(f"Added {note_type} note for {user.mention}", ephemeral=True)

    @app_commands.command(name="usernotes_clear", description="Clear user notes")
    async def usernotes_clear(self, interaction: discord.Interaction, user: discord.User):
        await interaction.response.send_message(f"Cleared notes for {user.mention}", ephemeral=True)

    @app_commands.command(name="usernotes_view", description="View user notes")
    async def usernotes_view(self, interaction: discord.Interaction, user: discord.User):
        await interaction.response.send_message(f"Notes for {user.mention}", ephemeral=True)

    @app_commands.command(name="mass", description="Mass actions on users")
    async def mass(self, interaction: discord.Interaction, action: str, users: str, reason: str = None):
        await interaction.response.send_message(f"Performed {action} on users: {users}", ephemeral=True)

    @app_commands.command(name="lock", description="Lock a channel")
    async def lock(self, interaction: discord.Interaction, channel: discord.TextChannel, reason: str = None):
        await interaction.response.send_message(f"Locked {channel.mention}", ephemeral=True)

    @app_commands.command(name="unlock", description="Unlock a channel")
    async def unlock(self, interaction: discord.Interaction, channel: discord.TextChannel):
        await interaction.response.send_message(f"Unlocked {channel.mention}", ephemeral=True)

def setup(bot):
    bot.add_cog(Moderation(bot))