from tool import gett

def calendar_week_day_card_get(json_data, i):
    print(f'calendar_week_day_card - 获取番剧卡片列表 - {i}')
    output = ''
    t = gett('calendar/week/day/card')
    for index, item in enumerate(json_data[i]['items'], start=1):
        print(f'calendar_week_day_card - 获取番剧卡片 - {i} - {index}')
        itemt = t
        if 'rank' in item:
            itemt = itemt.replace('{{rank}}', str(item['rank']))
        else:
            itemt = itemt.replace('{{rank}}', '--')

        if 'rating' in item:
            itemt = itemt\
            .replace('{{score}}',str(item['rating']['score']))\
            .replace('{{score-all}}',str(item['rating']['total']))\
            .replace('{{score-10}}',str(item['rating']['count']['10']))\
            .replace('{{score-9}}',str(item['rating']['count']['9']))\
            .replace('{{score-8}}',str(item['rating']['count']['8']))\
            .replace('{{score-7}}',str(item['rating']['count']['7']))\
            .replace('{{score-6}}',str(item['rating']['count']['6']))\
            .replace('{{score-5}}',str(item['rating']['count']['5']))\
            .replace('{{score-4}}',str(item['rating']['count']['4']))\
            .replace('{{score-3}}',str(item['rating']['count']['3']))\
            .replace('{{score-2}}',str(item['rating']['count']['2']))\
            .replace('{{score-1}}',str(item['rating']['count']['1']))
        else:
            itemt = itemt\
            .replace('{{score}}','--')\
            .replace('{{score-all}}','--')\
            .replace('{{score-10}}','--')\
            .replace('{{score-9}}','--')\
            .replace('{{score-8}}','--')\
            .replace('{{score-7}}','--')\
            .replace('{{score-6}}','--')\
            .replace('{{score-5}}','--')\
            .replace('{{score-4}}','--')\
            .replace('{{score-3}}','--')\
            .replace('{{score-2}}','--')\
            .replace('{{score-1}}','--')

        if 'name_cn' in item:
            itemt = itemt\
                .replace('{{name-cn}}',item['name_cn'])
        else:
            itemt = itemt\
                .replace('{{name-cn}}',item['name'])
        
        itemt = itemt\
            .replace('{{name}}',item['name'])\
            .replace('{{pic}}',item['images']['common'] if item.get('images',None) != None else 'https://pbp.kaphia.qzz.io/images/image_placeholder_1_1.png')\
            .replace('{{link}}',item['url'])

        output += itemt

    return output