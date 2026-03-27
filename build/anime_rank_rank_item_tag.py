from tool import gett, savef

def anime_rank_rank_item_tag_get(tag_data):
    print(f'anime_rank_rank_item - 获取排行榜item标签')
    o = ''
    t = gett('anime_rank/rank/item/tag')
    for tag in tag_data:
        o += t\
        .replace('{{text}}', tag['name'])\
        .replace('{{count}}', str(tag['count']))

    return o