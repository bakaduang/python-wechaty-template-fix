"""template of your bot"""
from __future__ import annotations
import asyncio
import os
from wechaty_puppet_itchat import PuppetItChat
from wechaty_puppet import PuppetOptions
from wechaty import Wechaty, WechatyOptions

from wechaty_plugin_contrib.contrib.info_logger import InfoLoggerPlugin
from src.plugins.ding_dong import DingDongPlugin
from src.plugins.repeater import RepeaterPlugin
from src.plugins.counter import CounterPlugin, UICounterPlugin


if __name__ == "__main__":
    options = WechatyOptions(
        puppet=PuppetItChat(PuppetOptions())
    )
    bot = Wechaty(options)
    bot.use([
        DingDongPlugin(),
        RepeaterPlugin(),
        InfoLoggerPlugin(),
        CounterPlugin(),
        UICounterPlugin(),
    ])
    asyncio.run(bot.start())
