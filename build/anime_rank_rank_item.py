from tool import gett, escape_xaml, resources

from .anime_rank_rank_item_tag import anime_rank_rank_item_tag_get

def anime_rank_rank_item_get(json_data, i):
    print(f'anime_rank_rank_item - 获取排行榜item - {i}')
    t = gett('anime_rank/rank/item')

    if json_data.get('images',None) != None:
        if json_data['images'].get('common',None) != None:
            resources[f'fanimage_common_{json_data['id']}.jpg'] = json_data['images']['common']
        else:
            resources[f'fanimage_common_{json_data['id']}.jpg'] = json_data['images'][list(json_data['images'].keys)[0]]
    
    return t\
    .replace('{{pic}}', f'https://bangumi.p.kaphia.qzz.io/resources/{f'fanimage_common_{json_data['id']}.jpg'}' if json_data.get('images',None) != None else 'https://bangumi.p.kaphia.qzz.io/resources/image_placeholder_1_1.png')\
    .replace('{{p}}', 'No. '+str(i))\
    .replace('{{rank}}', str(json_data['rating']['rank']))\
    .replace('{{score}}', str(json_data['rating']['score']))\
    .replace('{{name-cn}}', escape_xaml(json_data['name_cn'] if json_data['name_cn'] != '' else json_data['name']))\
    .replace('{{name}}', escape_xaml(json_data['name']))\
    .replace('{{tag}}', anime_rank_rank_item_tag_get(json_data['tags'][:5]))\
    .replace('{{link}}', 'https://bgm.tv/subject/'+str(json_data['id']))