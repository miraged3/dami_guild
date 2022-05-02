import json

import qqbot
import requests
from qqbot import MessageSendRequest


def daily(message: qqbot.Message) -> MessageSendRequest:
    """
    金山词霸每日一句
    :param message: 消息
    :return: MessageSendRequest
    """
    response = requests.get("https://open.iciba.com/dsapi/")
    english_data = json.loads(response.content)
    return qqbot.MessageSendRequest(
        f'{english_data.get("dateline")} 每日一句：\n{english_data.get("content")}\n{english_data.get("note")}',
        message.id)
