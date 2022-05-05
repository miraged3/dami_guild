import qqbot

from database.dragon import check_dragon_exists, add_dragon_once, add_dragon_today, dragon_top
from database.user import check_user_exists, add_user_info, get_user_name


# 龙王统计
def count_speak(message: qqbot.Message):
    if check_user_exists(message.author.id):
        if check_dragon_exists(message.author.id):
            add_dragon_once(message.author.id)
        else:
            add_dragon_today(message.author.id)
    else:
        add_user_info(message.author.id, message.author.username, message.author.avatar, message.author.bot)
        add_dragon_today(message.author.id)


def dragon_today(message: qqbot.Message):
    data = dragon_top()
    result = '今日水群统计: '
    for person in data:
        result = result + '\n' + get_user_name(person[0]) + ' ' + str(person[1]) + '条'
    return qqbot.MessageSendRequest(result, message.id)
