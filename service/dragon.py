import qqbot

from database.coin import add_coin
from database.dragon import check_dragon_exists, add_dragon_once, add_dragon_today, dragon_top, dragon_top_yesterday
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
    result = result.replace('.', ' ')
    qqbot.logger.info(result)
    return qqbot.MessageSendRequest(result, message.id)


def dragon_add_coin():
    dragon_user_id = dragon_top_yesterday()[0][0]
    dragon_username = get_user_name(dragon_user_id)
    dragon_speak_count = dragon_top_yesterday()[0][1]
    add_coin(dragon_user_id, 5, '龙王发放5金币')
    return qqbot.MessageSendRequest(f'昨日龙王为~~{dragon_username}<emoji:128166>，狂水了{dragon_speak_count}条消息！送上五个金币。')
