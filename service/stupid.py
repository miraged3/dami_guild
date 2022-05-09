import qqbot


def ma_reply(message: qqbot.Message):
    split_message = message.content.rpartition('吗')
    return qqbot.MessageSendRequest(f"{split_message[0]}! ", message.id)
