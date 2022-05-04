#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os.path
import random

import qqbot
from qqbot.core.util.yaml_util import YamlUtil

from service.coin import coin_have, random_add_coin
from service.divine import divine
from service.dragon import count_speak
from service.english import daily
from service.image import search
from service.summon import summon, ranking, inquire, add

config = YamlUtil.read(os.path.join(os.path.dirname(__file__), "config.yaml"))
token = qqbot.Token(config["token"]["appid"], config["token"]["token"])


async def message_handler(event, message: qqbot.Message):
    """
    频道消息处理
    :param event: 事件类型
    :param message: 事件对象（如监听消息是Message对象）
    :return:
    """
    # TODO:疯狂星期四提醒
    if message.guild_id == '1010148535400755610':
        return
    msg_api = qqbot.AsyncMessageAPI(token, False)
    if None is not message.content:
        qqbot.logger.info(f"发生事件{event}，收到消息：{message.content}")
    count_speak(message)
    if random.randint(1, 100) == 50:
        await msg_api.post_message(message.channel_id, random_add_coin(message))
    return


async def at_message_handler(event, message: qqbot.Message):
    """
    频道被@消息处理
    :param event: 事件类型
    :param message: 事件对象（如监听消息是Message对象）
    """
    if message.guild_id == '1010148535400755610':
        return
    msg_api = qqbot.AsyncMessageAPI(token, False)
    if message.content is not None:
        qqbot.logger.info(f"发生事件{event}，收到消息：{message.content}")
    api = qqbot.UserAPI(token, False)

    # 图片查询
    if message.content.startswith(f'<@!{api.me().id}> /图片'):
        await msg_api.post_message(message.channel_id, search(message))
        return

    # 每日一句查询
    if message.content.startswith(f'<@!{api.me().id}> /每日一句'):
        await msg_api.post_message(message.channel_id, daily(message))
        return

    # 金币查询
    if message.content.startswith(f'<@!{api.me().id}> /查询'):
        await msg_api.post_message(message.channel_id, coin_have(message))
        return

    # 占卜/签到
    if message.content.startswith(f'<@!{api.me().id}> /占卜'):
        await msg_api.post_message(message.channel_id, divine(message))
        return

    # 召唤
    if message.content.startswith(f'<@!{api.me().id}> /召唤'):
        await msg_api.post_message(message.channel_id, summon(message))
        return

    # 召唤查询
    if message.content.startswith(f'<@!{api.me().id}> /抽卡查询'):
        await msg_api.post_message(message.channel_id, inquire(message))
        return

    # 排行榜
    if message.content.startswith(f'<@!{api.me().id}> /排行榜'):
        await msg_api.post_message(message.channel_id, ranking(message))
        return

    # 增加卡池
    if message.content.startswith(f'<@!{api.me().id}> /add_card'):
        await msg_api.post_message(message.channel_id, add(message))

    # 获取当前频道id
    if message.content.startswith(f'<@!{api.me().id}> /get_current_id'):
        send = qqbot.MessageSendRequest(
            f'current guild:{message.guild_id}\ncurrent channel:{message.channel_id}', message.id)
        await msg_api.post_message(message.channel_id, send)
        return
