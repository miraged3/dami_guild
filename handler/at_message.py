import os

import qqbot
from qqbot.core.util.yaml_util import YamlUtil

from service.coin import coin_have
from service.divine import divine
from service.dragon import dragon_today
from service.english import daily
from service.image import search
from service.kfc import add_kfc_content, random_kfc_notice
from service.summon import summon, inquire, ranking, add

config = YamlUtil.read(os.path.join(os.path.dirname(__file__), "../config.yaml"))
token = qqbot.Token(config["token"]["appid"], config["token"]["token"])


async def at_message_handler(event, message: qqbot.Message):
    """
    频道被@消息处理
    :param event: 事件类型
    :param message: 事件对象（如监听消息是Message对象）
    """
    msg_api = qqbot.AsyncMessageAPI(token, False)
    if hasattr(message, 'content'):
        qqbot.logger.info(f"{message.author.username}：{message.content}")
    api = qqbot.UserAPI(token, False)

    # 图片查询
    if message.content.startswith(f'<@!{api.me().id}> /图片'):
        await msg_api.post_message(message.channel_id, search(message))
        return

    # 每日一句查询
    if message.content.startswith(f'<@!{api.me().id}> /每日一句'):
        await msg_api.post_message(message.channel_id, daily(message))
        return

    # 金币查询
    if message.content.startswith(f'<@!{api.me().id}> /查询'):
        await msg_api.post_message(message.channel_id, coin_have(message))
        return

    # 占卜/签到
    if message.content.startswith(f'<@!{api.me().id}> /占卜') or message.content.startswith(f'<@!{api.me().id}> /打卡'):
        await msg_api.post_message(message.channel_id, divine(message))
        return

    # 签到
    if message.content.startswith(f'<@!{api.me().id}> /乞讨'):
        await msg_api.post_message(message.channel_id, divine(message))
        return

    # 梭哈
    if message.content.startswith(f'<@!{api.me().id}> /梭哈'):
        pass

    # 召唤
    if message.content.startswith(f'<@!{api.me().id}> /召唤'):
        await msg_api.post_message(message.channel_id, summon(message))
        return

    # 召唤查询
    if message.content.startswith(f'<@!{api.me().id}> /抽卡查询'):
        await msg_api.post_message(message.channel_id, inquire(message))
        return

    # 排行榜
    if message.content.startswith(f'<@!{api.me().id}> /排行榜'):
        await msg_api.post_message(message.channel_id, ranking(message))
        return

    # 龙王查询
    if message.content.startswith(f'<@!{api.me().id}> /水群'):
        await msg_api.post_message(message.channel_id, dragon_today(message))
        return

    # 增加卡池
    if message.content.startswith(f'<@!{api.me().id}> /add_card'):
        await msg_api.post_message(message.channel_id, add(message))
        return

    # 增加疯狂星期四
    if message.content.startswith(f'<@!{api.me().id}> /add_kfc'):
        await msg_api.post_message(message.channel_id, add_kfc_content(message))
        return

    # 获取当前频道id
    if message.content.startswith(f'<@!{api.me().id}> /get_current_id'):
        send = qqbot.MessageSendRequest(
            f'current guild:{message.guild_id}\ncurrent channel:{message.channel_id}', message.id)
        await msg_api.post_message(message.channel_id, send)
        return

    # 测试疯狂星期四
    if message.content.startswith(f'<@!{api.me().id}> /get_random_kfc'):
        await msg_api.post_message(message.channel_id, random_kfc_notice(message))
        return
