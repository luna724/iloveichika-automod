import discord
from discord.ext import commands
from discord import RawReactionActionEvent

def process(bot: commands.Bot):
    verify_role = "Verified"

    @bot.event
    async def on_raw_reaction_add(payload: RawReactionActionEvent):
        # Botが指定するチャンネル/メッセージのみを監視
        guild = bot.get_guild(payload.guild_id)
        if payload.message_id == 1317878176369606676:
            # 認証の Embed のテキストIDで認証を監視
            role = discord.utils.get(guild.roles, name=verify_role)
            if role:
                member = guild.get_member(payload.user_id)
                if member:
                    print(f"[Discord.py]: {verify_role} role added to user {member.display_name}.")
                    await member.add_roles(role)
                else:
                    print(f"[Discord.py]: {payload.user_id} is not found.")
            else:
                print(f"[Discord.py]: {verify_role} is not found.")
            return

        if payload.message_id == 1317881025417711677:
            # ロール取得メッセージ
            roles = {
                "🇱": "LunaClient",
                "⭐": "SD-PEM",
                "🇸": "Stable-Diffusion",
                "🔴": "つべ",
                "🗿": "監視者",
                "<:sakisaki:1075136121119445092>": "!sakisaki"
            }

            print("[DEV]: payload.emoji: ", str(payload.emoji))
            print("[DEV]: payload.emoji.name: ", payload.emoji.name)
            if payload.emoji.name == "<:sakisaki:1075136121119445092>":
                print("[DEV]: sakisaki")
            elif payload.emoji.name == "\n{REGIONAL INDICATOR L}":
                print("[DEV]: L INDICATOR")

            role_name = roles.get(payload.emoji.name.strip(), None)
            if not role_name:
                # 外部サーバーの絵文字
                role_name = roles.get(str(payload.emoji), None)
                if not role_name:
                    print(f"[Discord.py]: {payload.emoji.name} aren't registered Verify role.")
                    return

            # ロール付与処理
            role = discord.utils.get(guild.roles, name=role_name)
            if role:
                member = guild.get_member(payload.user_id)
                if member:
                    print(f"[Discord.py]: {role_name} role added to user {member.display_name}.")
                    await member.add_roles(role)
                else:
                    print(f"[Discord.py]: {payload.user_id} is not found.")

            elif role_name == "!sakisaki":
                role_names = ["LunaClient", "SD-PEM", "Stable-Diffusion", "つべ", "監視者", "配死ん", "先駆者"]
                for role_name in role_names:
                    role = discord.utils.get(guild.roles, name=role_name)
                    if role:
                        member = guild.get_member(payload.user_id)
                        if member:
                            print(f"[Discord.py]: {role_name} role added to user {member.display_name}.")
                            await member.add_roles(role)

            else:
                print(f"[Discord.py]: {verify_role} is not found.")
            return

        return