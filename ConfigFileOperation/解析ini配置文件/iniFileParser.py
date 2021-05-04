from icecream import ic
from configparser import ConfigParser
import pymysql

cfg = ConfigParser()
cfg.read("../解析ini配置文件/dbConfig.ini")

dbConfig = dict(cfg.items('localdb'))  # 转换为dict更容易解包处理传参
ic(dbConfig)
"""
ic| dbConfig: {'database': 'mysql',
               'host': '127.0.0.1',
               'password': '123456',
               'port': '3306',
               'user': 'root'}
"""

con = pymysql.connect(**dbConfig)
