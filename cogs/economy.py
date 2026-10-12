import discord
from discord.ext import commands
from discord import app_commands

class Economy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="balance", description="Check your balance")
    async def balance(self, interaction: discord.Interaction):
        await interaction.response.send_message(f"Your balance is 100 meowency")

    @app_commands.command(name="deposit", description="Deposit money into your bank")
    async def deposit(self, interaction: discord.Interaction, amount: str):
        await interaction.response.send_message(f"Deposited {amount} meowency")

    @app_commands.command(name="withdraw", description="Withdraw money from your bank")
    async def withdraw(self, interaction: discord.Interaction, amount: str):
        await interaction.response.send_message(f"Withdrew {amount} meowency")

    @app_commands.command(name="pay", description="Pay another user")
    async def pay(self, interaction: discord.Interaction, user: discord.User, amount: str):
        await interaction.response.send_message(f"Paid {amount} meowency to {user.mention}")

    @app_commands.command(name="leaderboard", description="View the leaderboard")
    async def leaderboard(self, interaction: discord.Interaction):
        await interaction.response.send_message("Leaderboard")

    @app_commands.command(name="inventory", description="View your inventory")
    async def inventory(self, interaction: discord.Interaction):
        await interaction.response.send_message("Your inventory")

def setup(bot):
    bot.add_cog(Economy(bot))