# 金币查询
import qqbot

from database.coin import coin_inquiry


def coin_have(message: qqbot.Message):
    return qqbot.MessageSendRequest(f"<@{message.author.id}>你有{coin_inquiry(message.author.id)}枚金币", message.id)
