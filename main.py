import os

import pytz
import qqbot
from apscheduler.schedulers.background import BackgroundScheduler
from qqbot.core.util.yaml_util import YamlUtil

from cronjob.dragon import cron_add_dragon_coin
from handler.at_message import at_message_handler
from handler.member_event import guild_member_event_handler
from handler.message import message_handler

#                  ___====-_  _-====___
#            _--^^^#####//      \\#####^^^--_
#         _-^##########// (    ) \\##########^-_
#        -############//  |\^^/|  \\############-
#      _/############//   (@::@)   \\############\_
#     /#############((     \\//     ))#############\
#    -###############\\    (oo)    //###############-
#   -#################\\  / VV \  //#################-
#  -###################\\/      \//###################-
# _#/|##########/\######(   /\   )######/\##########|\#_
# |/ |#/\#/\#/\/  \#/\##\  |  |  /##/\#/  \/\#/\#/\#| \|
# `  |/  V  V  `   V  \#\| |  | |/#/  V   '  V  V  \|  '
#    `   `  `      `   / | |  | | \   '      '  '   '
#                     (  | |  | |  )
#                    __\ | |  | | /__
#                   (vvv(VVV)(VVV)vvv)
#                  神兽保佑
#                代码无BUG!

if __name__ == '__main__':
    config = YamlUtil.read(os.path.join(os.path.dirname(__file__), "config.yaml"))
    token = qqbot.Token(config["token"]["appid"], config["token"]["token"])

    # 普通消息
    message_handler = qqbot.Handler(qqbot.HandlerType.MESSAGE_EVENT_HANDLER, message_handler)

    # 被@的消息
    at_message_handler = qqbot.Handler(qqbot.HandlerType.AT_MESSAGE_EVENT_HANDLER, at_message_handler)

    # 成员信息更新
    guild_member_event_handler = qqbot.Handler(qqbot.HandlerType.GUILD_MEMBER_EVENT_HANDLER, guild_member_event_handler)

    # 定时任务
    scheduler = BackgroundScheduler(timezone=pytz.timezone('Asia/Shanghai'))
    scheduler.add_job(cron_add_dragon_coin, 'cron', hour='8', minute='1')
    scheduler.start()

    # 注册消息处理器并启动
    qqbot.async_listen_events(token, False, message_handler, at_message_handler, guild_member_event_handler)
