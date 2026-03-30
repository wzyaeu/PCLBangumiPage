from tool import gett
from .calendar_week_day import calendar_week_day_get

from datetime import datetime
from zoneinfo import ZoneInfo

def calendar_week_get(json_data, homepage = False):
    wd = datetime.now(ZoneInfo("Asia/Shanghai")).weekday()
    print(f'calendar_week - 获取本周推荐番剧内容')
    print(homepage)
    if not homepage:
        d = {}
        for i in range(7):
            d[i] = calendar_week_day_get(json_data, i, False)

        o = [d[i] for i in sorted(d.keys())]

        return gett('calendar/week')\
        .replace('{{day}}','\n'.join(o))
    else:
        d = calendar_week_day_get(json_data, wd, True)
        return gett('calendar/week')\
        .replace('{{day}}',d)