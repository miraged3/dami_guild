import os

from pychatgpt import Chat
from qqbot.core.util.yaml_util import YamlUtil

config = YamlUtil.read(os.path.join(os.path.dirname(__file__), "../config.yaml"))


def ask_gpt(message: str) -> str:
    chat = Chat(email=config["chatgpt"]["email"], password=config["chatgpt"]["password"],
                proxies="http://localhost:7890")
    return chat.ask(message)
