from aiogram import Router, F
from aiogram.filters import Command, StateFilter, CommandStart
from aiogram.types import Message
from aiogram.fsm.state import default_state
from aiogram.fsm.context import FSMContext
from bot import game_bot


router = Router(name='commands')


@router.message(CommandStart(), StateFilter(default_state))
async def start_bot(message: Message):
    name = message.from_user.full_name
    await message.answer(f'Привет!\nНапиши мне что-нибудь {name}')


@router.message(Command('help'))
async def help_bot(message: Message):
    await message.answer('Напиши мне что-нибудь.\n'
                         'Хочешь со мной поиграть напиши команду /game')


@router.message(Command('game'))
async def get_game(message: Message, state: FSMContext):
    await game_bot.invite_game(message, state)

