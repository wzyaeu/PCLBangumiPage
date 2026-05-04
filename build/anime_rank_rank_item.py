from tool import gett, logs_add

from .anime_rank_rank_item_tag import anime_rank_rank_item_tag_get

def anime_rank_rank_item_get(json_data, i):
    print(f'anime_rank_rank_item - 获取排行榜item - {i}')
    t = gett('anime_rank/rank/item')

    return t\
    .replace('{{pic}}', json_data['images']['common'])\
    .replace('{{p}}', 'No. '+str(i))\
    .replace('{{rank}}', str(json_data['rating']['rank']))\
    .replace('{{score}}', str(json_data['rating']['score']))\
    .replace('{{name-cn}}', json_data['name_cn'] if json_data['name_cn'] != '' else json_data['name'])\
    .replace('{{name}}', json_data['name'])\
    .replace('{{tag}}', anime_rank_rank_item_tag_get(json_data['tags'][:5]))\
    .replace('{{link}}', 'https://bgm.tv/subject/'+str(json_data['id']))