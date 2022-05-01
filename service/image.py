import base64
import json

import qqbot
import requests
from qqbot import MessageSendRequest


def search(message: qqbot.Message) -> MessageSendRequest:
    """
    搜索并生成图片
    :param message: 消息
    :return: MessageSendRequest
    """
    headers = {'Content-Type': 'application/json'}
    keyword = message.content.split('/图片')[1].strip()
    datas = json.dumps({"keyword": keyword})
    response = requests.post("http://maoookai.cn:318/image", data=datas, headers=headers)
    img_data = base64.b64decode(json.loads(response.content).get("image"))
    with open(f'/home/wwwroot/default/dami_images/{message.id}.jpg', 'wb') as f:
        f.write(img_data)
        f.close()
    return qqbot.MessageSendRequest(f"<@{message.author.id}>你要的{keyword}：", message.id,
                                    image=f'https://maoookai.cn/dami_images/{message.id}.jpg')
