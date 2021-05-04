from icecream import ic
import json

with open('../解析json配置文件/db.json') as f:
    cfg = json.load(f)['localdb']

ic(cfg)
