import qqbot

from database.kfc import add_kfc


def add_kfc_content(message: qqbot.Message):
    splited_content = message.content.split(' ')
    content = splited_content[2]
    add_kfc(content)
    return qqbot.MessageSendRequest('添加成功', message.id)
