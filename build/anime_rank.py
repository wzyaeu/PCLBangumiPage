from tool import gett, savef, y, HEADER
from .anime_rank_rank import anime_rank_rank_get
import json
import requests

def anime_rank_build():

    print(f'anime_rank - 获取页面内容')
    
    limit = 25
    pages = 4

    t = gett('anime_rank')
    for p in range(pages):
        print(f'anime_rank - 获取页面 {p+1}')
        data = requests.get(f'https://api.bgm.tv/v0/subjects?type=2&sort=rank&limit={limit}&offset={(limit*p)}', headers=HEADER)
        if data.status_code != 200:
            print(f'anime_rank - 无法获取页面api数据 ({data.status_code})')
            exit()
        json_data = json.loads(data.text)

        pagebtn = gett('anime_rank/pagebtn')
        pagebtn = pagebtn\
        .replace('{{p}}',str(p+1))\
        .replace('{{a}}',str(pages))
        if p != 0:
            pagebtn = pagebtn\
            .replace('{{lbtn}}',\
                     gett('anime_rank/pagebtn/left').replace('{{num}}',str(p))
            )
        else:
            pagebtn = pagebtn\
            .replace('{{lbtn}}','')

        if p+1 != pages:
            pagebtn = pagebtn\
            .replace('{{rbtn}}',\
                     gett('anime_rank/pagebtn/right').replace('{{num}}',str(p+2))
            )
        else:
            pagebtn = pagebtn\
            .replace('{{rbtn}}','')

        savef(f'anime_rank_{p+1}.json',json.dumps(
            {
                "Title": f"PCL Bangumi 动漫排行榜 | 第 {p+1} / {pages} 页"
            }
        ,ensure_ascii=False))
        savef(f'anime_rank_{p+1}.xaml',
            y(t\
            .replace('{{style}}',gett('anime_rank/_style'))\
            .replace('{{p}}',str(p+1))\
            .replace('{{a}}',str(pages))\
            .replace('{{rank}}',anime_rank_rank_get(json_data, p*limit))\
            .replace('{{pagebtn}}',pagebtn))
        )