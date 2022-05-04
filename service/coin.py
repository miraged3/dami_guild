import random

import qqbot
from qqbot import MessageReference

from database.coin import coin_inquiry, add_coin


# 金币查询
def coin_have(message: qqbot.Message):
    return qqbot.MessageSendRequest(f"<@{message.author.id}>你有{coin_inquiry(message.author.id)}枚金币", message.id)


# 随机获得金币
def random_add_coin(message: qqbot.Message):
    message_reference = MessageReference()
    message_reference.message_id = message.id
    salt = random.randint(1, 4)
    if salt == 1:
        coin = random.randint(1, 3)
        add_coin(message.author.id, coin, '发言随机金币')
        return qqbot.MessageSendRequest(f"感觉你说的很有道理，送你{coin}金币！", message.id, message_reference=message_reference)
    elif salt == 2:
        coin = random.randint(1, 3)
        add_coin(message.author.id, coin, '发言随机金币')
        return qqbot.MessageSendRequest(f"你这话真有意思，给你{coin}金币！", message.id, message_reference=message_reference)
    elif salt == 3:
        coin = random.randint(1, 3)
        add_coin(message.author.id, coin, '发言随机金币')
        return qqbot.MessageSendRequest(f"好，这是{coin}金币，请收下", message.id, message_reference=message_reference)
    elif salt == 4:
        coin = random.randint(1, 3)
        add_coin(message.author.id, coin, '发言随机金币')
        return qqbot.MessageSendRequest(f"笑死，给你{coin}金币", message.id, message_reference=message_reference)
