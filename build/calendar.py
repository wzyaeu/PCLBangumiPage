from tool import gett, savef, y, BUILD_VERSION, logs_add, BUILD_TIME
from .calendar_week import calendar_week_get
from .about import about_get

import json
import re
from datetime import datetime
from zoneinfo import ZoneInfo

def calendar_build(json_data):
    print(f'calendar - 获取页面内容')
    savef('Custom.json',json.dumps(
        {
            "Title": "PCL Bangumi 每日放送"
        }
    ,ensure_ascii=False))
    logs_add('calendar','save_file Custom.json','Success')
    savef('Custom.xaml.ini',BUILD_TIME)
    logs_add('calendar','save_file Custom.xaml.ini','Success')

    s = gett('calendar/_style')

    now = datetime.now(ZoneInfo("Asia/Shanghai"))
    year = now.year
    month = now.month
    day = now.day

    savef(
        'Custom.xaml',
        y(gett('calendar-today')\
        .replace('{{style}}',s)\
        .replace('{{title-date}}',f'{year}/{month}/{day}')\
        .replace('{{week}}',calendar_week_get(json_data, homepage=True))
        .replace('{{about}}',about_get()))
    )
    logs_add('calendar','save_file Custom.xaml','Success')
    savef('calendar_all.json',json.dumps(
        {
            "Title": "PCL Bangumi 本周放送"
        }
    ,ensure_ascii=False))
    logs_add('calendar','save_file calendar_all.json','Success')
    savef(
        'calendar_all.xaml',
        y(gett('calendar')\
        .replace('{{style}}',s)\
        .replace('{{week}}',calendar_week_get(json_data)))
    )
    logs_add('calendar','save_file calendar_all.xaml','Success')