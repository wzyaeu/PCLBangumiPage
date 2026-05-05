from tool import gett, HEADER, escape_xaml
from .anime_rank_rank_item_tag import anime_rank_rank_item_tag_get

import requests
import json

def random_item_get(rs):
    t = gett('random/item')
    o = ''
    for r in rs:
        data = requests.post(
            f'https://api.bgm.tv/v0/search/subjects?limit=1&offset={r}',
            json={
                'sort': 'rank',
                'filter': {'type': [2],'rating': ['>=6']}
            },
            headers=HEADER
        )
        data = json.loads(data.text)['data'][0]
        o += t\
        .replace('{{pic}}', data['images']['common'])\
        .replace('{{rank}}', str(data['rating']['rank']))\
        .replace('{{score}}', str(data['rating']['score']))\
        .replace('{{name-cn}}', escape_xaml(data['name_cn'] if data['name_cn'] != '' else data['name']))\
        .replace('{{name}}', escape_xaml(data['name']))\
        .replace('{{tag}}', anime_rank_rank_item_tag_get(data['tags'][:5]))\
        .replace('{{link}}', 'https://bgm.tv/subject/'+str(data['id']))

    return o