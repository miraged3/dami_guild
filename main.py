import os

import qqbot
from qqbot.core.util.yaml_util import YamlUtil

from handler import message_handler, at_message_handler

if __name__ == '__main__':
    config = YamlUtil.read(os.path.join(os.path.dirname(__file__), "config.yaml"))
    token = qqbot.Token(config["token"]["appid"], config["token"]["token"])

    # 普通消息
    message_handler = qqbot.Handler(qqbot.HandlerType.MESSAGE_EVENT_HANDLER, message_handler)

    # 被@的消息
    at_message_handler = qqbot.Handler(qqbot.HandlerType.AT_MESSAGE_EVENT_HANDLER, at_message_handler)

    # 注册消息处理器并启动
    qqbot.async_listen_events(token, False, message_handler, at_message_handler)
