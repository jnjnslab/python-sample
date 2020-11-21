import requests
from bs4 import BeautifulSoup
# Webページを取得する
load_url = "https://news.yahoo.co.jp/categories/it"
html = requests.get(load_url)
#ダウンロードが成功したか確認する
html.raise_for_status()
#取得したページを解析のためパースする
soup = BeautifulSoup(html.content, "html.parser")
# classで検索し、その中のすべてのaタグを検索してリンクを表示する
topic = soup.find(class_="topicsList_main")
#print(topic)
elements = topic.find_all("a")
for element in elements:
    print(element.text)
    url = element.get("href")
    print(url)
