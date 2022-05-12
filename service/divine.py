import random

import qqbot
from qqbot import MessageSendRequest

from database import coin
from database.divine import check_divine_today, add_divine_today


def divine(message: qqbot.Message) -> MessageSendRequest:
    if check_divine_today(message.author.id):
        return qqbot.MessageSendRequest(f"<@{message.author.id}>今天已经打卡过啦~~明天再来吧", message.id)
    luck = random.randint(1, 100)
    if luck > 95:
        coin_number = 3
    elif luck > 75:
        coin_number = 2
    else:
        coin_number = 1
    add_divine_today(message.author.id, luck, coin_number)
    coin.add_coin(message.author.id, coin_number, '占卜')
    return qqbot.MessageSendRequest(f"<@{message.author.id}><emoji:299>打卡成功，获得了{coin_number}金币！",
                                    message.id)


def beg(message: qqbot.Message) -> MessageSendRequest:
    if check_divine_today(message.author.id):
        return qqbot.MessageSendRequest(f"<@{message.author.id}><emoji:32>要过饭了还想要？没完没了了是吧？", message.id)
    luck = random.randint(1, 100)
    if luck > 97:
        coin_number = 5
        comment = '我看你骨骼惊奇天赋异禀将来必成大器，这5金币就送给你！'
    elif luck > 90:
        coin_number = 4
        comment = '好可怜一孩子，快收下这4金币'
    elif luck > 80:
        coin_number = 3
        comment = '好吧好吧，3金币给你了~~'
    elif luck > 60:
        coin_number = 2
        comment = '你有点烦诶，2金币拿去'
    elif luck > 10:
        coin_number = 1
        comment = '怎么又来要饭了？算了给你个币吧'
    else:
        coin_number = 0
        comment = '哈哈，我今天不想给你币，快走吧快走吧'
    add_divine_today(message.author.id, luck, coin_number)
    coin.add_coin(message.author.id, coin_number, '乞讨')
    return qqbot.MessageSendRequest(f"<@{message.author.id}>{comment}", message.id)
