from .calendar import calendar_build
from .anime_rank import anime_rank_build
from .html import html_build
from .random import random_build
from tool import savef, BUILD_VERSION, savefb, gettb, logs_add, logs_result, gett, HEADER, save_resources, resources

import requests
import json

def build():
    print('init - 获取api数据中')
    data = requests.get('https://api.bgm.tv/calendar',headers=HEADER)
    logs_add('init','api_status_code',data.status_code)
    if data.status_code != 200:
        print(f'init - 无法获取api数据 ({data.status_code})')
        exit()
    json_data = json.loads(data.text)
    calendar_build(json_data)
    anime_rank_build()
    random_build()
    # html_build()
    print('init - 复制图片中')
    for imagename in (
        'image_placeholder_1_1.png','image_placeholder_3_4.png','kaphia.jpg'
    ):
        savefb(f'resources/{imagename}',gettb(f'images/{imagename}'))
        logs_add('init','copy_image',imagename)
    logs_add('init','build_information','start')
    resources['logo.png'] = 'https://bgm.tv/img/logo_riff.png'
    save_resources()