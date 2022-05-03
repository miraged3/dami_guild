#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os.path

import qqbot
from qqbot.core.util.yaml_util import YamlUtil

from service.divine import divine
from service.english import daily
from service.image import search
from service.summon import summon, ranking, inquire

config = YamlUtil.read(os.path.join(os.path.dirname(__file__), "config.yaml"))
token = qqbot.Token(config["token"]["appid"], config["token"]["token"])


async def message_handler(event, message: qqbot.Message):
    """
    频道消息处理
    :param event: 事件类型
    :param message: 事件对象（如监听消息是Message对象）
    :return:
    """
    # TODO: 龙王统计


async def at_message_handler(event, message: qqbot.Message):
    """
    频道被@消息处理
    :param event: 事件类型
    :param message: 事件对象（如监听消息是Message对象）
    """
    msg_api = qqbot.AsyncMessageAPI(token, False)
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
