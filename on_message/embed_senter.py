from discord import Embed, Message
from discord.ext import commands

async def process(bot: commands.Bot, message: Message):
    text = message.content

    if "?SENT=" in text:
        text = text.replace("?SENT=", "")

        if "server-rules" in text:
            output = " 賢いなら守って\n### - [DiscordTOS](https://discord.com/terms)を破る\n### - [User]を除くiloveichikaの使用"
            await message.channel.send(
                embed=Embed(
                    title="Server Rules (禁止行為)",
                    description=output, color=0xFF0000
                ))
            return

