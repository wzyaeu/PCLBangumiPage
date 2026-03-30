from tool import gett, savef, y, HEADER

import random
import requests
import json
from typing import Any

def s(data, i):
    l = int(data['rating']['count'][str(i)] / data['rating']['total'] * 53)
    return str(l)

def random_build():
    def check_r(r):
        data = requests.get(f'https://api.bgm.tv/v0/subjects/{r}',headers=HEADER)
        if data.status_code == 404:
            return (False, None)
        if data.status_code == 200:
            return (True, json.loads(data.text))
        return (False, data.status_code)
    print('random - 开始生成')
    t = gett('ramdom')
    data: Any
    while True:
        r = random.randint(1,700000)
        print(f'random - 测试id {r}')
        use, data = check_r(r)
        if use: o = all([use,data['rating']['score'] > 5,data['rating']['rank'] > 0, data['type'] == 2])
        else: o = use
        print(f'random - {o}')
        if o:
            break
    
    savef('random.json',json.dumps(
        {
            "Title": "PCL Bangumi 随机推番"
        }
    ,ensure_ascii=False))
    savef('random.xaml',t\
        .replace('{{pic}}', data['images']['medium'])\
        .replace('{{name-cn}}', data.get('name_cn',data['name']))\
        .replace('{{name}}', data['name'])\
        .replace('{{score}}', str(data['rating']['score']))\
        .replace('{{score-1}}', s(data, 1))\
        .replace('{{score-2}}', s(data, 2))\
        .replace('{{score-3}}', s(data, 3))\
        .replace('{{score-4}}', s(data, 4))\
        .replace('{{score-5}}', s(data, 5))\
        .replace('{{score-6}}', s(data, 6))\
        .replace('{{score-7}}', s(data, 7))\
        .replace('{{score-8}}', s(data, 8))\
        .replace('{{score-9}}', s(data, 9))\
        .replace('{{score-10}}', s(data, 10))\
        .replace('{{rank}}', str(data['rating']['rank']))\
        .replace('{{start}}', data['date'])\
        .replace('{{info}}', data['summary'])\
        .replace('{{link}}', 'https://bgm.tv/subject/'+str(data['id']))
    )
