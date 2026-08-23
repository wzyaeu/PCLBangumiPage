from tool import gett, savef, BUILD_VERSION, y, logs_add

import json

def about_get():
    print('about_get - 生成中')
    return y(gett('calendar/about')\
        .replace('{{gv}}',BUILD_VERSION))