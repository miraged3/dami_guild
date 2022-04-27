#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import asyncio
import base64
import json
import logging
import os.path
import shutil

import numpy as np
import qqbot
import requests
from PIL import Image
from qqbot.core.util.yaml_util import YamlUtil

from image_util import stitch_image
from onmyoji import summon

config = YamlUtil.read(os.path.join(os.path.dirname(__file__), "config.yaml"))
token = qqbot.Token(config["token"]["appid"], config["token"]["token"])


async def message_handler(event, message: qqbot.Message):
    """
    频道消息处理
    :param event: 事件类型
    :param message: 事件对象（如监听消息是Message对象）
    :return:
    """
    pass


async def at_message_handler(event, message: qqbot.Message):
    """
    频道被@消息处理
    :param event: 事件类型
    :param message: 事件对象（如监听消息是Message对象）
    """
    msg_api = qqbot.AsyncMessageAPI(token, False)
    qqbot.logger.info(f"事件{event}，收到消息：{message.content}")
    api = qqbot.UserAPI(token, False)

    # 图片查询
    if message.content.startswith(f'<@!{api.me().id}> /图片'):
        headers = {'Content-Type': 'application/json'}
        keyword = message.content.split('/图片')[1].strip()
        datas = json.dumps({"keyword": keyword})
        response = requests.post("http://maoookai.cn:318/image", data=datas, headers=headers)
        img_data = base64.b64decode(json.loads(response.content).get("image"))
        with open(f'/home/wwwroot/default/dami_images/{message.id}.jpg', 'wb') as f:
            f.write(img_data)
            f.close()
        send = qqbot.MessageSendRequest(f"<@{message.author.id}>你要的{keyword}：", message.id,
                                        image=f'https://maoookai.cn/dami_images/{message.id}.jpg')
        # 通过api发送回复消息
        await msg_api.post_message(message.channel_id, send)
        return

    # 每日一句查询
    if message.content.startswith(f'<@!{api.me().id}> /每日一句:'):
        response = requests.get("https://open.iciba.com/dsapi/")
        english_data = json.loads(response.content)
        await asyncio.sleep(1)
        # 构造消息发送请求数据对象
        send = qqbot.MessageSendRequest(
            f'{english_data.get("dateline")} 每日一句\n{english_data.get("content")}\n{english_data.get("note")}',
            message.id)
        # 通过api发送回复消息
        await msg_api.post_message(message.channel_id, send)
        return

    # 阴阳师单抽
    if message.content.startswith(f'<@!{api.me().id}> /抽卡'):
        shutil.copyfile(summon(), f'/home/wwwroot/default/dami_images/{message.id}.jpg')
        send = qqbot.MessageSendRequest(f"<@{message.author.id}>你召唤出了：", message.id,
                                        image=f'https://maoookai.cn/dami_images/{message.id}.jpg')
        await msg_api.post_message(message.channel_id, send)
        return

    # 阴阳师十连
    if message.content.startswith(f'<@!{api.me().id}> /十连'):
        img_list = []
        for i in range(10):
            img_list.append(summon())
        img1 = stitch_image(img_list[0], img_list[1])
        img2 = stitch_image(img_list[4], img_list[5])
        img1.save('tmp/stitch1.jpg')
        img2.save('tmp/stitch2.jpg')
        for i in range(2, 4):
            img_tmp1 = stitch_image('tmp/stitch1.jpg', img_list[i])
            img_tmp1.save('tmp/stitch1.jpg')
        for i in range(6, 8):
            img_tmp2 = stitch_image('tmp/stitch2.jpg', img_list[i])
            img_tmp2.save('tmp/stitch2.jpg')
        stitch_image('/usr/local/dami/res/null.jpg', img_list[8]).save('tmp/stitch3.jpg')
        stitch_image(img_list[9], '/usr/local/dami/res/null.jpg').save('tmp/stitch4.jpg')
        stitch_image('tmp/stitch3.jpg', 'tmp/stitch4.jpg').save('tmp/stitch5.jpg')
        stitch_image('tmp/stitch1.jpg', 'tmp/stitch2.jpg', False).save('tmp/stitch6.jpg')
        stitch_image('tmp/stitch6.jpg', 'tmp/stitch5.jpg', False).save(
            f'/home/wwwroot/default/dami_images/{message.id}.jpg')
        send = qqbot.MessageSendRequest(f"<@{message.author.id}>你召唤出了：", message.id,
                                        image=f'https://maoookai.cn/dami_images/{message.id}.jpg')
        await msg_api.post_message(message.channel_id, send)
        return
