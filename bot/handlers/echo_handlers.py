from aiogram import Router, F
from aiogram.types import Message


router = Router(name="echo_bot")


async def send_photo(message: Message):
    await message.reply_photo(message.photo[0].file_id)


async def send_sticker(message: Message):
    await message.reply(text='И я так могу...')
    await message.answer_sticker(message.sticker.file_id)


async def send_anima(message: Message):
    await message.reply(text='И у меня такая есть...')
    await message.answer_animation(message.animation.file_id)


async def send_echo(message: Message):
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.reply(text='Данный тип сообщения не поддерживается')


router.message.register(send_photo, F.photo)
router.message.register(send_sticker, F.sticker)
router.message.register(send_anima, F.animation)
router.message.register(send_echo)