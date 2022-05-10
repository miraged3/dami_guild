#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os.path

import qqbot
from qqbot import GuildMember
from qqbot.core.util.yaml_util import YamlUtil
from qqbot.model.ws_context import WsContext

config = YamlUtil.read(os.path.join(os.path.dirname(__file__), "../config.yaml"))
token = qqbot.Token(config["token"]["appid"], config["token"]["token"])


def guild_member_event_handler(context: WsContext, guild_member: GuildMember):
    return
