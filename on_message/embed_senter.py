from discord import Embed, Message
from discord.ext import commands

async def process(bot: commands.Bot, message: Message):
    text = message.content

    if "?SENT=" in text and message.author.id == 1123616332349452288: # iloveichika2のみ
        text = text.replace("?SENT=", "")

        if "server-rules" in text:
            output = " 賢いなら守って\n### - [DiscordTOS](https://discord.com/terms)を破る\n### - [User]を除くiloveichikaの使用\n- このメッセージに何かしらの絵文字を付けると認証"
            await message.channel.send(
                embed=Embed(
                    title="Server Rules (禁止行為)",
                    description=output, color=0xFF0000
                ))

        if "project-sdpem-disclaimer" in text:
            output = "### SD-PEMに対する機能リクエスト、バグ報告などは[Githubから](https://github.com/luna724/SDPEM)\n"
            await message.channel.send(
                embed=Embed(
                    title=" Disclaimer",
                    description=output, color=0x00FFFF
                )
            )

        if "project-lunaclient-disclaimer" in text:
            output = ("#### 注意事項 - LunaClient v1.1.4はサポートされません。\n"
                      "### LunaClientに対する機能リクエスト、バグ方向などは[GitHubから](https://github.com/luna724/LunaClient)\n"
                      "- v1.1.4の問題、機能リクエストはサポートされません。\n"
                      "- v2のバグ報告は現在「クラッシュ」のみ受け付けています(β版のため)")
            await message.channel.send(
                embed=Embed(
                    title=" Disclaimer",
                    description=output, color=0x00FFFF
                )
            )

        if "role-giver" in text:
            output = "- ほしいロールに対応する絵文字を付けて取得\n- LunaClient: :regional_indicator_l: \n- SD-PEM: :star: \n- Stable-Diffusion: :regional_indicator_s: \n- Youtube: :red_circle: \n- 監視者(ログ閲覧権限): :moai:"
            await message.channel.send(
                embed=Embed(
                    title="ロール取得",
                    description=output, color=0x00FFFF
                )
            )

        if "role-giver-react" in text:
            # roles: チャンネルID
            channel_id = 1317110165035548672
            target_msg_id = 1317881025417711677

            channel = bot.get_channel(channel_id)
            if not channel:
                print("[DEV]: channel is not found.")
                return
            try:
                target_msg = await channel.fetch_message(target_msg_id)
            except Exception as e:
                print(f"[DEV]: target_msg is not found. ({e})")
                return

            reactions = ["🇱", "⭐", "🇸", "🔴", "🗿"]
            for reaction in reactions:
                await target_msg.add_reaction(reaction)
