import random

import qqbot


def ma_reply(message: qqbot.Message):
    split_message = message.content.rpartition('吗')
    return qqbot.MessageSendRequest(f"{split_message[0]}! ", message.id)


def repeat(message: qqbot.Message):
    reply_words = ['真的吗', '就是啊', '不会吧', '笑死', '就这啊', '怎么会这样', '+1', '饿了', '绝了', '好困', '哈人']
    i = random.randint(1, 100)
    if i > 95:
        return qqbot.MessageSendRequest(message.content, message.id)
    else:
        return qqbot.MessageSendRequest(reply_words[random.randint(0, len(reply_words) - 1)], message.id)
