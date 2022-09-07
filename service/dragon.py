import datetime

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
    week_list = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"]
    today = datetime.date.today()
    date_today = today.strftime('%Y-%m-%d')
    date_weekday = week_list[today.weekday()]
    if today.weekday() <= 3:
        date_thursday = 3 - today.weekday()
    else:
        date_thursday = 10 - today.weekday()
    if today.weekday() < 5:
        date_weekend = 5 - today.weekday()
    else:
        date_weekend = 0

    date_new_year = (datetime.datetime.strptime(f"{today.year}-01-01", "%Y-%m-%d").date() - today).days
    if date_new_year < 0:
        date_new_year = (datetime.datetime.strptime(f"{today.year + 1}-01-01", "%Y-%m-%d").date() - today).days

    date_labour = (datetime.datetime.strptime(f"{today.year}-05-01", "%Y-%m-%d").date() - today).days
    if date_labour < 0:
        date_labour = (datetime.datetime.strptime(f"{today.year + 1}-05-01", "%Y-%m-%d").date() - today).days

    date_national_day = (datetime.datetime.strptime(f"{today.year}-10-01", "%Y-%m-%d").date() - today).days
    if date_national_day < 0:
        date_national_day = (datetime.datetime.strptime(f"{today.year + 1}-10-01", "%Y-%m-%d").date() - today).days

    morning_message = f"""
    【摸鱼办】提醒您：
    今天是：{date_today} {date_weekday}
    上午好，摸鱼人！工作再累，一定不要忘记摸鱼哦！有事没事起身去茶水间，去厕所，去廊道走走。别老在工位上坐着，钱是老板的，但命是自己的。
    昨日【龙王】{dragon_username}，发言{dragon_speak_count}条，获得5金币奖励。
    距离【疯狂星期四】还有{date_thursday}天
    距离【周末】还有{date_weekend}天
    距离【元旦】还有{date_new_year}天
    距离【五一】还有{date_labour}天
    距离【国庆】还有{date_national_day}天

    上班是帮老板赚钱，摸鱼是赚老板的钱！
    """
    return qqbot.MessageSendRequest(morning_message)
