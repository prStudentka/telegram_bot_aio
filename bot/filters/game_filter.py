from aiogram.filters import BaseFilter
from aiogram.types import Message
from ..games.config_game import FIRST_NUMBER,  LAST_NUMBER


class NumberInMessage(BaseFilter):
    async def __call__(self, message: Message):
        return message.text and \
               message.text.isdigit() and \
               FIRST_NUMBER <= int(message.text) <= LAST_NUMBER