from Bot import telegram
from aiohttp import web
import BotBase
import asyncio
import re

class Bot(BotBase.BotBase):
    def __init__(self, config, loop=None):
        super().__init__(config, loop=loop)
        self.config = config
        self._users_data = {}

    async def command_handler(self, user_id, update, start=False):
        if "/start" == self.api.get_payload(update):
            return self.main_user_loop(user_id)

    async def default_task(self, user_id):
        pass

    async def main_user_loop(self, user_id):
        await self.api.send_message(user_id, "AAAAAAAAAA")
