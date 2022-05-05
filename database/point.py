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
    if not check_point_user(user_id):
        sql_add_point = f"""
        insert into point(user_id, point) values ('{user_id}',{point});
        """
        cursor.execute(sql_add_point)
        conn.commit()
        cursor.close()
    else:
        sql_add_point = f"""
        update point set point=point+{point} where user_id='{user_id}';
        """
        cursor.execute(sql_add_point)
        conn.commit()
        cursor.close()


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
    cursor.close()
    return result


# 检查用户是否已存在
def check_point_user(user_id: str):
    conn.ping(reconnect=True)
    cursor = conn.cursor()
    sql_check_user = f"""
    select * from point where user_id='{user_id}';
    """
    cursor.execute(sql_check_user)
    conn.commit()
    if len(cursor.fetchall()) != 0:
        cursor.close()
        return True
    else:
        cursor.close()
        return False
