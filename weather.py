import requests
city = "Moscow,RU"
appid = '893035d199d12800234311ee176f29a3'
res = requests.get('http://api.openweathermap.org/data/2.5/forecast', params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
data = res.json()
print('Прогноз погоды на неделю:')
for i in data['list']:
    print()
    print('Дата <', i['dt_txt'], '> \r\nВидимость <', '{0:+3.0f}'.format(i['visibility']),'m' '> \r\nСкорость ветра <',i['wind']['speed'],'m/s >')
