from tool import gett, savef, START_TIME, VERSION, y

import json

def about_build():
    print('about_build - 生成中')
    savef('about.json',json.dumps(
        {
            "Title": "关于 PCL Bangumi"
        }
    ,ensure_ascii=False))
    savef('about.xaml',y(gett('about')\
        .replace('{{version}}',VERSION)\
        .replace('{{gid}}',str(START_TIME)))
    )