import os
import random
import shutil

import qqbot

from image_util import stitch_image

path = '/usr/local/dami/res/'


def summon():
    result = random.randint(1, 1000)
    if result < 762:
        return path + 'R/' + random.choice(os.listdir(f'{path}R'))
    elif result < 962:
        return path + 'SR/' + random.choice(os.listdir(f'{path}SR'))
    elif result < 987:
        return path + 'SSR/' + random.choice(os.listdir(f'{path}SSR'))
    else:
        return path + 'SP/' + random.choice(os.listdir(f'{path}SP'))


def summon_one(message):
    shutil.copyfile(summon(), f'/home/wwwroot/default/dami_images/{message.id}.jpg')
    return qqbot.MessageSendRequest(f"<@{message.author.id}>你召唤出了：", message.id,
                                    image=f'https://maoookai.cn/dami_images/{message.id}.jpg')


def summon_ten(message):
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
    return qqbot.MessageSendRequest(f"<@{message.author.id}>你召唤出了：", message.id,
                                    image=f'https://maoookai.cn/dami_images/{message.id}.jpg')
