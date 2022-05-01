#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import asyncio
import base64
import json
import os.path
import shutil

import qqbot
import requests
from qqbot.core.util.yaml_util import YamlUtil

from image_util import stitch_image
from onmyoji import summon, summon_one, summon_ten
from service.english import daily
from service.image import search

config = YamlUtil.read(os.path.join(os.path.dirname(__file__), "config.yaml"))
token = qqbot.Token(config["token"]["appid"], config["token"]["token"])


async def message_handler(event, message: qqbot.Message):
    """
    频道消息处理
    :param event: 事件类型
    :param message: 事件对象（如监听消息是Message对象）
    :return:
    """
    pass


async def at_message_handler(event, message: qqbot.Message):
    """
    频道被@消息处理
    :param event: 事件类型
    :param message: 事件对象（如监听消息是Message对象）
    """
    msg_api = qqbot.AsyncMessageAPI(token, False)
    qqbot.logger.info(f"事件{event}，收到消息：{message.content}")
    api = qqbot.UserAPI(token, False)

    # 图片查询
    if message.content.startswith(f'<@!{api.me().id}> /图片'):
        await msg_api.post_message(message.channel_id, search(message))
        return

    # 每日一句查询
    if message.content.startswith(f'<@!{api.me().id}> /每日一句:'):
        await msg_api.post_message(message.channel_id, daily(message))
        return


