# -*- coding: utf-8 -*-
import os.path
import random
from datetime import datetime

import qqbot
from qqbot.core.util.yaml_util import YamlUtil

from database.dragon import dragon_get_coin_add
from service.coin import random_add_coin, check_get_coin, share_get_coin
from service.dragon import count_speak
from service.kfc import random_kfc_notice
from service.stupid import ma_reply, repeat
from util.chat_gpt import ask_gpt

config = YamlUtil.read(os.path.join(os.path.dirname(__file__), "../config.yaml"))
token = qqbot.Token(config["token"]["appid"], config["token"]["token"])


async def message_handler(event, message: qqbot.Message):
    """
    频道消息处理
    :param event: 事件类型
    :param message: 事件对象（如监听消息是Message对象）
    :return:
    """
    msg_api = qqbot.AsyncMessageAPI(token, False)
    # 消息是否包含文本
    if hasattr(message, 'content'):
        qqbot.logger.info(f"{message.author.username}：{message.content}")
        if message.channel_id == '1356661' and len(message.content) > 6:
            if random.randint(1, 100) < 2 or message.content.startswith('大米'):
                if message.content.startswith('大米'):
                    message.content = message.content[2:]
                qqbot.logger.info('触发ChatGPT: ' + message.author.username)
                await msg_api.post_message(message.channel_id, ask_gpt(message))
                return
        if message.channel_id == '1356645' or message.channel_id == '1369122':
            if message.content.startswith('[分享]') or message.content.startswith('当前版本不支持'):
                share_get_coin(message)
            return
        if random.randint(1, 100) < 4:
            if check_get_coin(message):
                qqbot.logger.info('触发发言掉落金币: ' + message.author.username)
                dragon_get_coin_add(message.author.id)
                await msg_api.post_message(message.channel_id, random_add_coin(message))
            return
        if message.content.endswith('吗？') or message.content.endswith('吗') or message.content.endswith('吗?'):
            if random.randint(1, 100) < 3:
                qqbot.logger.info('触发人工智障: ' + message.content)
                await msg_api.post_message(message.channel_id, ma_reply(message))
            return
        if datetime.today().weekday() == 3 and random.randint(1, 1000) < 3 and message.channel_id == '1356661':
            qqbot.logger.info('触发疯狂星期四: ' + message.author.username)
            await msg_api.post_message(message.channel_id, random_kfc_notice(message))
            return
        if random.randint(1, 100) < 2 and message.channel_id == '1356661':
            qqbot.logger.info('触发复读: ' + message.author.username)
            await msg_api.post_message(message.channel_id, repeat(message))
            return

    elif hasattr(message, 'attachments'):
        if message.channel_id == '1356645' or message.channel_id == '1369122':
            if message.attachments[0].url.startswith('gchat.qpic.cn/qmeetpic/'):
                share_get_coin(message)
        for attachment in message.attachments:
            qqbot.logger.info(f'{message.author.username}：{attachment.url}')
    count_speak(message)
    return
