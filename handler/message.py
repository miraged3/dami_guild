#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os.path
import random

import qqbot
from qqbot.core.util.yaml_util import YamlUtil

from database.dragon import dragon_get_coin_add
from service.coin import random_add_coin, check_get_coin
from service.dragon import count_speak
from service.stupid import ma_reply

config = YamlUtil.read(os.path.join(os.path.dirname(__file__), "../config.yaml"))
token = qqbot.Token(config["token"]["appid"], config["token"]["token"])


async def message_handler(event, message: qqbot.Message):
    """
    频道消息处理
    :param event: 事件类型
    :param message: 事件对象（如监听消息是Message对象）
    :return:
    """
    # TODO:疯狂星期四提醒
    msg_api = qqbot.AsyncMessageAPI(token, False)
    if hasattr(message, 'content'):
        qqbot.logger.info(f"{message.author.username}：{message.content}")
        if random.randint(1, 100) < 4:
            if check_get_coin(message):
                qqbot.logger.info('触发发言掉落金币: ' + message.author.username)
                dragon_get_coin_add(message.author.id)
                await msg_api.post_message(message.channel_id, random_add_coin(message))
            return
        if message.content.endswith('吗？') or message.content.endswith('吗') or message.content.endswith('吗?'):
            if random.randint(1, 100) < 3:
                qqbot.logger.info('触发人工智障: ' + message.author.username)
                await msg_api.post_message(message.channel_id, ma_reply(message))
    count_speak(message)
    return
