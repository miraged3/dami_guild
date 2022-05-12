import os

import qqbot
from qqbot.core.util.yaml_util import YamlUtil

from service.dragon import dragon_add_coin

config = YamlUtil.read(os.path.join(os.path.dirname(__file__), "../config.yaml"))
token = qqbot.Token(config["token"]["appid"], config["token"]["token"])


# 发放龙王金币
def cron_add_dragon_coin():
    qqbot.logger.info('启动龙王金币发放')
    msg_api = qqbot.MessageAPI(token, False)
    msg_api.post_message('1356661', dragon_add_coin())



