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


def add_kfc(content: str):
    conn.ping(reconnect=True)
    cursor = conn.cursor()
    sql_add_kfc = f"""
    insert into kfc(content) values ('{content}');
    """
    cursor.execute(sql_add_kfc)
    conn.commit()
    cursor.close()
