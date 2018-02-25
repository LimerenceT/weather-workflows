import sys
import os
import requests
import json

API_KEY = 'da76af79dbb64fcfa5c840dbd4a1fb83'
DIC = {"items": []}
RESULT = True


def gen_json(data):
    try:
        city = data['basic']['location']
        #cnty = data.get('basic').get('cnty')
        for day in data.get('daily_forecast'):
            date = day.get('date')
            cond_txt_d = day.get('cond_txt_d')
            cond_txt_n = day.get('cond_txt_n')
            cond_code = day.get('cond_code_d')
            tmp_max = day.get('tmp_max')+'℃'
            tmp_min = day.get('tmp_min')+'℃'
            title = '白天：' + cond_txt_d + '    晚上：' + cond_txt_n + '     ' + tmp_min + ' ~ ' + tmp_max
            DIC['items'].append({
                "title": title,
                "subtitle": city + '  ' + date,
                "icon": {
                    "path": os.path.abspath('.') + '/icon/' + cond_code + '.png',
                }
            })
    except:
        DIC['items'].append({
            "title": '没有查到这个城市',
            "subtitle": "",
            "icon": {
                "path": os.path.abspath('.') + '/icon/' + str(100) + '.png',
            }
        })


def get_data(location='auto_ip'):
    api = 'https://free-api.heweather.com/s6/weather/forecast'
    parameters = {
        'location': location,
        'key': 'da76af79dbb64fcfa5c840dbd4a1fb83',
    }
    r = requests.get(api, params=parameters)
    return r.json()


def main():
    if sys.argv[1] == '':
        data = get_data().get('HeWeather6')[0]
    else:
        data = get_data(sys.argv[1]).get('HeWeather6')[0]
    gen_json(data)


if __name__ == '__main__':
    main()
    js = json.dumps(DIC, indent=4, )
    print(js)
