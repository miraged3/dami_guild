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


# 增加金币
def add_coin(user_id: str, number: int, reason: str):
    cursor = conn.cursor()
    sql_check_user = f"""
    select number from coin where user_id='{user_id}';
    """
    if cursor.execute(sql_check_user):
        new_coin = cursor.fetchall()[0][0] + number
        add_coin_change(user_id, number, reason)
        sql_add_coin = f"""
        update coin set number={new_coin} where user_id='{user_id}';
        """
        cursor.execute(sql_add_coin)
        conn.commit()
    else:
        sql_add_user = f"""
        insert into coin (user_id, number) values ('{user_id}','{number}');
        """
        cursor.execute(sql_add_user)
        conn.commit()
        add_coin_change(user_id, number, reason)
    cursor.close()


# 增加金币记录
def add_coin_change(user_id: str, amount: int, reason: str):
    cursor = conn.cursor()
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    sql_add_coin_change = f"""
    insert into coin_change (user_id,time,amount,reason) values ('{user_id}','{current_time}','{amount}','{reason}');
    """
    cursor.execute(sql_add_coin_change)
    conn.commit()
    cursor.close()
