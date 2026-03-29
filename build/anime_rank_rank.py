from tool import gett

from .anime_rank_rank_item import anime_rank_rank_item_get

def anime_rank_rank_get(json_data, offset):
    print(f'anime_rank_rank - 获取排行榜内容')
    t = gett('anime_rank/rank')

    o = ''
    for index, item in enumerate(json_data['data'], start=offset+1):
        o += anime_rank_rank_item_get(item, index)

    return t\
    .replace('{{item}}', o)