import random

import qqbot

from database.kfc import add_kfc, get_all


def add_kfc_content(message: qqbot.Message):
    splited_content = message.content.split(' ')
    content = splited_content[2]
    add_kfc(content)
    return qqbot.MessageSendRequest('添加成功', message.id)


def random_kfc_notice(message: qqbot.Message):
    all_kfc = get_all()
    return qqbot.MessageSendRequest(all_kfc[random.randint(0, len(all_kfc) - 1)][0], message.id)
