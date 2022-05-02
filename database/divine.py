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


# 今日占卜
def add_divine_today(user_id: str, luck: int, add_coin: int):
    cursor = conn.cursor()
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    sql_add_divine = f"""
    insert into divine (date, luck, user_id, add_coin) values ('{current_date}','{luck}','{user_id}','{add_coin}');
    """
    cursor.execute(sql_add_divine)
    conn.commit()
    cursor.close()


# 查询今日是否已占卜
def check_divine_today(user_id: str) -> bool:
    cursor = conn.cursor()
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    sql_check_divine = f"""
    select * from divine where user_id='{user_id}' and date='{current_date}';
    """
    cursor.execute(sql_check_divine)
    if len(cursor.fetchall()) != 0:
        return True
    else:
        return False
