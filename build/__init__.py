from .calendar import calendar_build
from .anime_rank import anime_rank_build
from .html import html_build
from .random import random_build
from tool import savef, BUILD_VERSION, savefb, gettb, logs_add, logs_result, gett, VERSION

import requests
import json

def build():
    print('init - 获取api数据中')
    data = requests.get('https://api.bgm.tv/calendar')
    logs_add('init','api_status_code',data.status_code)
    if data.status_code != 200:
        print(f'init - 无法获取api数据 ({data.status_code})')
        exit()
    json_data = json.loads(data.text)
    calendar_build(json_data)
    anime_rank_build()
    random_build()
    html_build()
    print('init - 复制图片中')
    for imagename in (
        'image_placeholder_1_1.png','image_placeholder_3_4.png'
    ):
        savefb(imagename,gettb(f'images/{imagename}'))
        logs_add('init','copy_image',imagename)
    logs_add('init','build_information','start')
    bit_main = gett('build_information/main','md')
    bit_main_buildlog = gett('build_information/main/build_log','md')

    savef('build_info.md',bit_main\
          .replace('{{version}}',VERSION)\
          .replace('{{build_version}}',BUILD_VERSION)\
          .replace('{{build_log}}',\
          '\n'.join([
                '\n'.join([
                    bit_main_buildlog
                    .replace('{{region}}',region) 
                    .replace('{{name}}',name) 
                    .replace('{{info}}',str(result)) 
                    for name, result in data
                ]) 
                for region, data in logs_result().items()
          ]))
    )