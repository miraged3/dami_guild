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


# 增加卡片
def add_card(card_name: str, star: int, detail: str, image: str):
    conn.ping(reconnect=True)
    cursor = conn.cursor()
    sql_add_card = f"""
    insert into card (name,star,detail,image) values ('{card_name}',{star},'{detail}','{image}');
    """
    cursor.execute(sql_add_card)
    conn.commit()
    sql_find_id = f"""
    select id from card where name='{card_name}'and star={star} and detail='{detail}' and image='{image}';
    """
    cursor.execute(sql_find_id)
    conn.commit()
    card_id = cursor.fetchall()[0][0]
    cursor.close()
    return card_id


# 删除卡片
def delete_card(card_id: int):
    conn.ping(reconnect=True)
    cursor = conn.cursor()
    sql_add_card = f"""
    delete from card where id={card_id};
    """
    cursor.execute(sql_add_card)
    conn.commit()
    cursor.close()


# 抽取卡片
def get_all_cards(star: int) -> tuple:
    conn.ping(reconnect=True)
    cursor = conn.cursor()
    sql_get_all_cards = f"""
    select name,star,detail,image,id from card where star={star}; 
    """
    cursor.execute(sql_get_all_cards)
    conn.commit()
    result = cursor.fetchall()
    cursor.close()
    return result
