from argparse import ArgumentParser
import asyncio
from setup import dp, bot
from app.structure.models import Proxy
from loguru import logger
from typing import Callable

parser = ArgumentParser()


async def _background_func(name):
    c = 0
    while True:
        c += 1
        print(f"Hello {name}, {c} times")
        await asyncio.sleep(1)


def _pars_args() -> ArgumentParser:
    parser.add_argument("-c", "--create_proxy", action="store_true")
    parser.add_argument("-np", "--notify_problems", action="store_true")
    return parser.parse_args()


def _create_first_proxy(args: ArgumentParser):
    if args.create_proxy:
        logger.info("Test proxy created")
        if Proxy.select().where(Proxy.name == "triolan"):
            return
        Proxy.create(
            name="triolan",
            address="185.112.12.134",
            port=2831,
            login="36547",
            password="gyy5wFZD",
        )


async def _run_with_background_func(
    parser: ArgumentParser, func: Callable, *args, **kwargs
):
    # TODO update flags
    if parser.notify_problems:
        logger.info("Run bot with notification")

        async with asyncio.TaskGroup() as tg:
            # tg.create_task(testing_sites(1))
            tg.create_task(func(*args, **kwargs))
            tg.create_task(dp.start_polling(bot))

    else:
        logger.info("Run bot only")
        await dp.start_polling(bot)


async def run_with_flags():
    parser = _pars_args()
    _create_first_proxy(parser)
    await _run_with_background_func(parser, _background_func, "King")
