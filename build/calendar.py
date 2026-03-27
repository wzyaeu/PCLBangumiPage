from tool import gett, savef, START_TIME, y
from .calendar_week import calendar_week_get

import json
import re

def calendar_build(json_data):
    print(f'calendar - 获取页面内容')
    savef('Custom.json',json.dumps(
        {
            "Title": "PCL Bangumi 每日放送"
        }
    ,ensure_ascii=False))
    savef('Custom.xaml.ini',str(START_TIME))

    s = gett('calendar/_style')
    savef(
        'Custom.xaml',
        y(gett('calendar-today')\
        .replace('{{style}}',s)\
        .replace('{{week}}',calendar_week_get(json_data, homepage=True)))
    )
    savef('calendar_all.json',json.dumps(
        {
            "Title": "PCL Bangumi 本周放送"
        }
    ,ensure_ascii=False))
    savef(
        'calendar_all.xaml',
        y(gett('calendar')\
        .replace('{{style}}',s)\
        .replace('{{week}}',calendar_week_get(json_data)))
    )