from tool import gett
import json

def get_calendar_announcement():
    data = json.loads(gett('data/announcement','json'))
    an = gett('announcement/announcement')
    info_text = gett('announcement/info/text')
    info_linkbtn = gett('announcement/info/link_btn')
    output = ''
    for a in data:
        output += an.replace('{{title}}',a['title'])\
        .replace('{{tip}}','False' if a['tip'] else 'True')\
        .replace('{{date}}',a['date'])\
        .replace('{{info}}',''.join([
            info_text.replace('{{text}}',i['data']) if i['type'] == 'text' else
            info_linkbtn.replace('{{text}}',i['data'])
            .replace('{{url}}',i['url']) if i['type'] == 'link' else

            ''
            for i in a['info']
        ]))
    return output