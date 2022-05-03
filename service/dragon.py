import qqbot

from database.dragon import check_dragon_exists, add_dragon_once, add_dragon_today
from database.user import check_user_exists, add_user_info


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
