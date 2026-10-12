import discord
from discord.ext import commands
from discord import app_commands

class Earning(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="daily", description="Claim your daily reward")
    async def daily(self, interaction: discord.Interaction):
        await interaction.response.send_message("Claimed daily reward")

    @app_commands.command(name="weekly", description="Claim your weekly reward")
    async def weekly(self, interaction: discord.Interaction):
        await interaction.response.send_message("Claimed weekly reward")

    @app_commands.command(name="work", description="Work for money")
    async def work(self, interaction: discord.Interaction):
        await interaction.response.send_message("Worked and earned money")

    @app_commands.command(name="beg", description="Beg for money")
    async def beg(self, interaction: discord.Interaction):
        await interaction.response.send_message("Begged and earned money")

    @app_commands.command(name="fish", description="Go fishing")
    async def fish(self, interaction: discord.Interaction):
        await interaction.response.send_message("Went fishing")

    @app_commands.command(name="mine", description="Go mining")
    async def mine(self, interaction: discord.Interaction):
        await interaction.response.send_message("Went mining")

    @app_commands.command(name="groom", description="Groom animals")
    async def groom(self, interaction: discord.Interaction):
        await interaction.response.send_message("Groomed animals")

    @app_commands.command(name="trivia", description="Play trivia")
    async def trivia(self, interaction: discord.Interaction):
        await interaction.response.send_message("Played trivia")

    @app_commands.command(name="rob", description="Rob another user")
    async def rob(self, interaction: discord.Interaction, user: discord.User):
        await interaction.response.send_message(f"Robbed {user.mention}")

def setup(bot):
    bot.add_cog(Earning(bot))