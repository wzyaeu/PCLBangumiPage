from tool import gett, savef, logs_add, HEADER, y
from .random_item import random_item_get

import random
import requests
import json
from typing import Any

def s(data, i):
    l = int(data['rating']['count'][str(i)] / max([int(i) for i in list(data['rating']['count'].values())]) * 53)
    return str(l)

def random_build():
    print('random - 开始生成')
    rs = []
    for _ in range(5):
        r = random.randint(1,500)
        while (r in rs):
            r = random.randint(1,500)
        rs.append(r)
    logs_add('random','start',f'random_ids: {rs}')
    
    savef('random.json',json.dumps(
        {
            'Title': 'PCL Bangumi 随机推番'
        }
    ,ensure_ascii=False))
    logs_add('random','save_file random.json','Success')

    t = gett('random')

    savef('random.xaml',y(t
        .replace('{{style}}',gett('anime_rank/_style'))
        .replace('{{item}}', random_item_get(rs)))
    )
    logs_add('random','save_file random.xaml','Success')
