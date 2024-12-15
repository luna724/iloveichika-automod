import importlib
import os
import discord
from discord.ext import commands
from typing import *

class BOT:
    def __init__(self):
        intents = discord.Intents.default()
        intents.members = True
        intents.presences = True
        intents.message_content = True
        intents.reactions = True
        intents.guilds = True
        intents.guild_messages = True
        intents.guild_reactions = True
        intents.guild_scheduled_events = True
        intents.typing = True
        intents.voice_states = True
        intents.webhooks = True
        intents.integrations = True
        intents.invites = True
        intents.messages = True
        self.bot = commands.Bot(command_prefix='!', intents=intents)
        self.bot.remove_command('help')

        self.init()
        self.on_message_functions = self.listup_processes(folder_path="on_message")
        slash_command_functions = self.listup_processes(folder_path="processor")
        for s in slash_command_functions:
            s(self.bot)
        self.launch_bot()

    @staticmethod
    def listup_processes(folder_path) -> List[Callable]:
        processes = []
        # ディレクトリ内のすべての .py ファイルを取得
        for filename in os.listdir(os.path.join(os.getcwd(), folder_path)):
            if filename.endswith(".py") and not filename.startswith("__"):  # __init__.py は除外
                module_name = f"{folder_path.replace('/', '.')}.{filename[:-3]}"  # モジュール名に変換
                try:
                    # モジュールの動的インポート
                    module = importlib.import_module(module_name)

                    # モジュール内に process 関数が存在するか確認
                    if hasattr(module, "process"):
                        if callable(module.process):
                            # process(message) を呼び出す
                            processes.append(module.process)
                    else:
                        print(f"{module_name} には 'process' 関数が定義されていません")
                except Exception as e:
                    print(f"{module_name} の読み込み中にエラーが発生しました: {e}")
        return processes

    def init(self):
        bot = self.bot
        @bot.event
        async def on_ready():
            print(f'Logged as {bot.user}')

        @bot.event
        async def on_message(message: discord.Message):
            if message.author == bot.user:
                return
            if message.guild.id != 1287028655754575976:
                return

            await self.process_message(message)
            await bot.process_commands(message)

    async def process_message(self, message):
        for f in self.on_message_functions:
            await f(self.bot, message)

    def launch_bot(self):
        self.bot.run(os.environ['iloveichikaTOKEN'])

if __name__ == "__main__":
    BOT()