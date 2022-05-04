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


# 增加积分
def add_point(user_id: str, point: int):
    conn.ping(reconnect=True)
    cursor = conn.cursor()
    sql_add_point = f"""
    insert into point(user_id, point) values ('{user_id}',{point});
    """
    cursor.execute(sql_add_point)
    conn.commit()


# 积分排行榜查询
def top_point():
    conn.ping(reconnect=True)
    cursor = conn.cursor()
    sql_top_point = f"""
    select user_id,point from point order by point desc limit 10;
    """
    cursor.execute(sql_top_point)
    result = cursor.fetchall()
    conn.commit()
    print(result)
    return result
