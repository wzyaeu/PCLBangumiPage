from .calendar import calendar_build
from .anime_rank import anime_rank_build
from .about import about_build
from .html import html_build

import requests
import json

def build():
    print('init - 获取api数据中')
    data = requests.get('https://api.bgm.tv/calendar')
    if data.status_code != 200:
        print(f'init - 无法获取api数据 ({data.status_code})')
        exit()
    json_data = json.loads(data.text)
    calendar_build(json_data)
    anime_rank_build()
    about_build()
    html_build()