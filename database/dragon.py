import datetime
import os

import pymysql
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


# 增加一次发言记录
def add_dragon_once(user_id: str):
    conn.ping(reconnect=True)
    cursor = conn.cursor()
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    sql_add_speak = f"""
    update dragon set speak_count=speak_count+1 where user_id='{user_id}'and date='{current_date}';
    """
    cursor.execute(sql_add_speak)
    conn.commit()
    cursor.close()


# 检查今日是否已创建
def check_dragon_exists(user_id: str) -> bool:
    conn.ping(reconnect=True)
    cursor = conn.cursor()
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    sql_check_user = f"""
    select * from dragon where user_id='{user_id}'and date='{current_date}'；
    """
    cursor.execute(sql_check_user)
    conn.commit()
    if len(cursor.fetchall()) != 0:
        cursor.close()
        return True
    else:
        cursor.close()
        return False


# 创建今日统计
def add_dragon_today(user_id: str):
    conn.ping(reconnect=True)
    cursor = conn.cursor()
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    sql_add_today = f"""
    insert into dragon(user_id, speak_count, date) values ('{user_id}',1,'{current_date}');
    """
    cursor.execute(sql_add_today)
    conn.commit()
    cursor.close()
