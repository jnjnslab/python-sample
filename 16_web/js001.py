#指定した地名の天気予報を表示する
import json, requests, sys

# OpenWeatherMap.orgのAPIからJSONデータをダウンロードする
#url ='http://api.openweathermap.org/data/2.5/weather?units=metric&q=Tokyo&lang=ja&appid=01ef9dfa3ab6284f9832aa71a8b2070e'
url = 'https://api.openweathermap.org/data/2.5/forecast?lat=35.18028&lon=136.90667&units=metric&lang=ja&appid=01ef9dfa3ab6284f9832aa71a8b2070e'

print(url)
response = requests.get(url)
response.raise_for_status()
# JSONデータからPython変数に読み込む
weather_data = json.loads(response.text)
print(weather_data)
#print(weather_data['weather'][0]['main'])
