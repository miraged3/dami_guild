import random

import qqbot
from qqbot import MessageReference

from database.coin import coin_inquiry, add_coin
from database.dragon import dragon_get_coin


# 金币查询
def coin_have(message: qqbot.Message):
    return qqbot.MessageSendRequest(f"<@{message.author.id}>你有{coin_inquiry(message.author.id)}枚金币", message.id)


# 发言掉落金币次数查询
def check_get_coin(message: qqbot.Message) -> bool:
    if dragon_get_coin(message.author.id) >= 1:
        return False
    else:
        return True


# 随机获得金币
def random_add_coin(message: qqbot.Message):
    message_reference = MessageReference()
    message_reference.message_id = message.id
    salt = random.randint(1, 10)
    reason = '发言随机金币'
    if salt == 1:
        coin = random.randint(1, 3)
        add_coin(message.author.id, coin, reason)
        return qqbot.MessageSendRequest(f"感觉你说的很有道理，送你{coin}金币！", message.id, message_reference=message_reference)
    elif salt == 2:
        coin = random.randint(1, 3)
        add_coin(message.author.id, coin, reason)
        return qqbot.MessageSendRequest(f"你这话真有意思，给你{coin}金币！", message.id, message_reference=message_reference)
    elif salt == 3:
        coin = random.randint(1, 3)
        add_coin(message.author.id, coin, reason)
        return qqbot.MessageSendRequest(f"好，这是{coin}金币，请收下", message.id, message_reference=message_reference)
    elif salt == 4:
        coin = random.randint(1, 3)
        add_coin(message.author.id, coin, reason)
        return qqbot.MessageSendRequest(f"笑死，给你{coin}金币", message.id, message_reference=message_reference)
    elif salt == 5:
        coin = random.randint(1, 3)
        add_coin(message.author.id, coin, reason)
        return qqbot.MessageSendRequest(f"他真的，我哭死，给你{coin}金币", message.id, message_reference=message_reference)
    elif salt == 6:
        coin = random.randint(1, 3)
        add_coin(message.author.id, coin, reason)
        return qqbot.MessageSendRequest(f"这都行? 给你{coin}金币", message.id, message_reference=message_reference)
    elif salt == 7:
        coin = random.randint(1, 3)
        add_coin(message.author.id, coin, reason)
        return qqbot.MessageSendRequest(f"怎会如此，请收下{coin}金币", message.id, message_reference=message_reference)
    elif salt == 8:
        coin = random.randint(1, 3)
        add_coin(message.author.id, coin, reason)
        return qqbot.MessageSendRequest(f"就这? 拿下这{coin}金币吧", message.id, message_reference=message_reference)
    elif salt == 9:
        coin = random.randint(1, 3)
        add_coin(message.author.id, coin, reason)
        return qqbot.MessageSendRequest(f"你真可爱! 我要给你{coin}金币!", message.id, message_reference=message_reference)
    elif salt == 10:
        coin = random.randint(1, 3)
        add_coin(message.author.id, coin, reason)
        return qqbot.MessageSendRequest(f"你看天上那朵云，像不像我现在送你的{coin}金币?", message.id, message_reference=message_reference)
    elif salt == 11:
        coin = random.randint(1, 3)
        add_coin(message.author.id, coin, reason)
        return qqbot.MessageSendRequest(f"你好，请问你需要{coin}金币吗? 送你了！", message.id, message_reference=message_reference)