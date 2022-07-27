import datetime
import os

import pymysql as pymysql
import qqbot
from qqbot.core.util.yaml_util import YamlUtil

config = YamlUtil.read(os.path.join(os.path.dirname(__file__), "../config.yaml"))
token = qqbot.Token(config["token"]["appid"], config["token"]["token"])
conn = pymysql.connect(
    host=config['mysql']['address'],
    port=config['mysql']['port'],
    user=config['mysql']['user'], password=config['mysql']['password'],
    database=config['mysql']['database'],
    charset='utf8')


# 增加抽卡记录
def add_summon(used_coin: int, card_id: int, card_name: str, user_id: str, star: int):
    conn.ping(reconnect=True)
    cursor = conn.cursor()
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    sql_add_summon = f"""
    insert into summon(time, used_coin, card_id, card_name, user_id,card_star) values ('{current_time}',{used_coin},'{card_id}','{card_name}','{user_id}',{star});
    """
    cursor.execute(sql_add_summon)
    conn.commit()
    cursor.close()


# 查询已有
def already_summon(user_id: str):
    conn.ping(reconnect=True)
    cursor = conn.cursor()
    sql_already_summon = f"""
    select card_id,card_name from summon where user_id='{user_id}' order by time desc;
    """
    cursor.execute(sql_already_summon)
    result = cursor.fetchall()
    print(result)
    cursor.close()
    return result
