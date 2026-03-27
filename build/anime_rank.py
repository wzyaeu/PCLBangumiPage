from tool import gett, savef, y
from .anime_rank_rank import anime_rank_rank_get
import json
import requests

def anime_rank_build():
    savef('anime_rank.json',json.dumps(
        {
            "Title": "PCL Bangumi 动画Rank排行榜"
        }
    ,ensure_ascii=False))

    print(f'anime_rank - 获取页面内容')
    data = requests.get('https://api.bgm.tv/v0/subjects?type=2&sort=rank', headers={
        'user-agent': 'wzyaeu/PclBangumiPage'
    })
    if data.status_code != 200:
        print(f'anime_rank - 无法获取api数据 ({data.status_code})')
        exit()
    json_data = json.loads(data.text)

    t = gett('anime_rank')
    savef('anime_rank.xaml',
        y(t\
        .replace('{{style}}',gett('anime_rank/_style'))\
        .replace('{{rank}}',anime_rank_rank_get(json_data)))
    )