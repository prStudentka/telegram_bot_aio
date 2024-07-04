from unittest.mock import AsyncMock
import pytest
from bot.handlers.command_handler import start_bot


@pytest.mark.asyncio
async def test_start_command():
    message_mock = AsyncMock()
    name = message_mock.from_user.full_name
    await start_bot(message_mock)

    message_mock.answer.assert_called_with(f'Привет!\nНапиши мне что-нибудь {name}')