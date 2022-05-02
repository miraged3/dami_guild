import random

import qqbot
from qqbot import MessageSendRequest


# TODO:complete

def divine(message: qqbot.Message) -> MessageSendRequest:
    user_id = message.author.id
    luck = random.randint(1, 100)
    if luck > 95:
        add_coin = 3
    elif luck > 75:
        add_coin = 2
    elif luck > 5:
        add_coin = 1
    else:
        add_coin = 0
    pass
