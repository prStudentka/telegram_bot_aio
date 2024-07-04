#!/usr/bin/env python3
from bot import game_bot
from bot.handlers import (
                           echo_handlers,
                           command_handler
                          )
from bot import loader


def main():
    loader.dp.include_routers(
                       command_handler.router,
                       game_bot.router_game,
                       echo_handlers.router,
                       )
    loader.dp.run_polling(loader.mybot)


if __name__ == '__main__':
    main()