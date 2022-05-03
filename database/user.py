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


# 添加成员信息
def add_user_info(user_id: str, user_name: str, user_avatar: str, is_bot: bool):
    conn.ping(reconnect=True)
    cursor = conn.cursor()
    sql_add_user = f"""
    insert into user(number, name, avatar, bot) values ('{user_id}','{user_name}','{user_avatar}',{is_bot});
    """
    cursor.execute(sql_add_user)
    conn.commit()
    cursor.close()


# 获取成员名称
def get_user_name(user_id: str):
    conn.ping(reconnect=True)
    cursor = conn.cursor()
    sql_check_divine = f"""
    select name from user where number='{user_id}';
    """
    cursor.execute(sql_check_divine)
    conn.commit()
    return cursor.fetchall()[0][0]


# 检查用户是否存在
def check_user_exists(user_id: str) -> bool:
    conn.ping(reconnect=True)
    cursor = conn.cursor()
    sql_check_user = f"""
    select * from user where number='{user_id}';
    """
    cursor.execute(sql_check_user)
    conn.commit()
    if len(cursor.fetchall()) != 0:
        cursor.close()
        return True
    else:
        cursor.close()
        return False
