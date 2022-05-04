import random
import urllib.request

import qqbot
from qqbot import MessageSendRequest

from database.card import add_card, delete_card, get_all_cards
from database.coin import add_coin
from database.point import top_point, add_point
from database.summon import add_summon, already_summon
from database.user import get_user_name


def summon(message: qqbot.Message) -> MessageSendRequest:
    used_coin = 5
    chance = random.randint(1, 100)
    if chance > 85:
        star = 5
        point = 3
    elif chance > 55:
        star = 4
        point = 2
    else:
        star = 3
        point = 1
    all_cards = get_all_cards(star)
    selected = all_cards[random.randint(0, len(all_cards) - 1)]
    name = selected[0]
    detail = selected[2]
    card_id = selected[4]
    image = f'https://maoookai.cn/dami_images/cards/{selected[3]}.jpg'
    add_coin(message.author.id, used_coin, '抽卡')
    add_summon(used_coin, card_id, name, message.author.id, star)
    add_point(message.author.id, point)
    if detail is not None and '暂无' != detail and '' != detail:
        return qqbot.MessageSendRequest(
            f"<@{message.author.id}>你召唤出了：{name}，获得{point}积分！\n稀有度：{star_generater(int(star))}\n介绍：{detail}",
            message.id, image=image)
    else:
        return qqbot.MessageSendRequest(
            f"<@{message.author.id}>你召唤出了：{name}，获得{point}积分！\n稀有度：{star_generater(int(star))}", message.id,
            image=image)


def inquire(message: qqbot.Message) -> MessageSendRequest:
    result = '你已经抽到了：'
    data = already_summon(message.author.id)
    for card in data:
        result = result + '\n' + str(card[0]) + '：' + card[1]
    return qqbot.MessageSendRequest(result, message.id)


def ranking(message: qqbot.Message) -> MessageSendRequest:
    data = top_point()
    result = '当前排行榜为：'
    for person in data:
        result = result + '\n' + get_user_name(person[0]) + '：' + str(person[1]) + '分'
    return qqbot.MessageSendRequest(result, message.id)


def add(message: qqbot.Message) -> MessageSendRequest:
    splited_content = message.content.split(' ')
    card_name = splited_content[2]
    star = int(splited_content[3])
    url = 'https://' + message.attachments[0].url
    filename = f"/home/wwwroot/default/dami_images/cards/{message.id}.jpg"
    urllib.request.urlretrieve(url, filename)
    if len(splited_content) == 5:
        detail = splited_content[4]
        card_id = add_card(card_name, star, detail, message.id)
    else:
        card_id = add_card(card_name, star, '暂无', message.id)
    return qqbot.MessageSendRequest(f"{card_name}添加成功，ID为{card_id}", message.id)


def delete(message: qqbot.Message) -> MessageSendRequest:
    splited_content = message.content.split(' ')
    card_id = splited_content[2]
    delete_card(int(card_id))
    return qqbot.MessageSendRequest(f"{card_id}添加成功", message.id)


def star_generater(number: int):
    star = ''
    for i in range(0, number):
        star = star + '★'
    return star
