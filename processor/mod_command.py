import discord
from discord.ext import commands
from discord import RawReactionActionEvent
from typing import Literal

def process(bot: commands.Bot):
    guild = discord.Object(id=1287028655754575976)

    @bot.tree.command(
        name="make_embed",
        description="make your message to embed",
        guild=guild
    )
    async def make_embed(interaction: discord.Interaction, title: str, message: str, color: Literal["red", "green", "blue", "aqua", "lime", "white", "yellow"] = "aqua"):
        color_dict = {
            "red": 0xff0000,
            "green": 0x00ff00,
            "blue": 0x0000ff,
            "aqua": 0x00ffff,
            "lime": 0x00ff00,
            "white": 0xffffff,
            "yellow": 0xffff00
        }

        await interaction.channel.send(
            embed=discord.Embed(
                title=title,
                description=message,
                color=color_dict[color]
            )
        )
