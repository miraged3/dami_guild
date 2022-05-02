import random

import qqbot
from qqbot import MessageSendRequest, Emoji
from qqbot.model.emoji import EmojiType

from database import coin
from database.divine import check_divine_today, add_divine_today


def divine(message: qqbot.Message) -> MessageSendRequest:
    if check_divine_today(message.author.id):
        return qqbot.MessageSendRequest(f"<@{message.author.id}>今天已经占卜过啦~~明天再来吧", message.id)
    luck = random.randint(1, 100)
    if luck > 95:
        coin_number = 3
        description = '大吉'
    elif luck > 75:
        coin_number = 2
        description = '中吉'
    elif luck > 5:
        coin_number = 1
        description = '小吉'
    else:
        coin_number = 0
        description = '凶'
    add_divine_today(message.author.id, luck, coin_number)
    coin.add_coin(message.author.id, coin_number, '占卜')
    return qqbot.MessageSendRequest(f"<@{message.author.id}><emoji:299>你今天的运势为~~{description}，获得了{coin_number}金币！",
                                    message.id)
