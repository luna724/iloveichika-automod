from discord import Embed, Message
from discord.ext import commands
import discord.utils
import random
import time


async def process(bot: commands.Bot, message: Message):
    text = message.content.strip()
    channel_id = message.channel.id
    welcome_channel_id = 1306100727709433867
    if channel_id == welcome_channel_id:
        trigger_messages = ["hi!", "!gimme verified"]
        if text.lower() in trigger_messages:
            guild = message.guild
            role_name = "Verified"
            member = message.author

            role = discord.utils.get(guild.roles, name=role_name)
            if not role:
                await message.reply(
                    f"[Discord.py]: {role_name} is not found.", mention_author=False
                )
                return

            if role in member.roles:
                await message.reply(
                    "もうモデレータじゃないのか? 強欲なやつだ", mention_author=True
                )
                return

            await member.add_roles(role)
            await message.reply(
                f"認証成功! もうここにはいられないよ、いってらっしゃい!",
                mention_author=True,
            )
            return
    if channel_id == 1287028656203632743:
        if text.strip().startswith("spamoyai"):
            count = text.replace("spamoyai", "").strip()
            if count.isdigit():
                count = int(count)
            else:
                count = 1
            for i in range(count):
                await message.reply(
                    ("🗿" * random.randrange(1, 150))
                    + ("🍷" * random.randrange(0, 500))
                )
                time.sleep(0.5)
        return
    return
