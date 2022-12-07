import os

import qqbot
from pychatgpt import Chat
from qqbot import MessageReference
from qqbot.core.util.yaml_util import YamlUtil

config = YamlUtil.read(os.path.join(os.path.dirname(__file__), "../config.yaml"))


def ask_gpt(message: qqbot.Message):
    message_reference = MessageReference()
    message_reference.message_id = message.id
    chat = Chat(email=config["chatgpt"]["email"], password=config["chatgpt"]["password"],
                proxies="http://localhost:7890")
    return qqbot.MessageSendRequest(chat.ask(message.content), message.id, message_reference=message_reference)
