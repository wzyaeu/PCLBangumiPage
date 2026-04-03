from tool import gett, logs_add
from .calendar_week_day_card import calendar_week_day_card_get

def calendar_week_day_get(json_data, i, today):
    print(f'calendar_week_day - 获取天番剧内容 - {i}')
    logs_add('calendar_week_day','get_page',f'page: {i+1}')
    week_map = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"]

    if today:
        t = gett('calendar/week/day-today')
    else:
        t = gett('calendar/week/day')
    return t\
    .replace('{{text}}',week_map[i])\
    .replace('{{card}}',calendar_week_day_card_get(json_data, i))\
    # .replace('{{id}}',str(i)) # day.reserved