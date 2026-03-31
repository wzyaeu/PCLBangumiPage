from tool import gett, savef, BUILD_VERSION, VERSION, y

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
        .replace('{{gv}}',BUILD_VERSION))
    )