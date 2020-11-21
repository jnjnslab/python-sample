import requests
from bs4 import BeautifulSoup
# Webページを取得する
load_url = "https://webhtml-7f629.web.app/test1.html"
html = requests.get(load_url)
#ダウンロードが成功したか確認する
html.raise_for_status()
#取得したページを解析のためパースする
soup = BeautifulSoup(html.content, "html.parser")
# titleタグを検索して、そのテキスト部分を表示する
el1 = soup.find("title")
print(el1)
print(el1.text)
#h2タグを検索して、そのテキスト部分を表示する
el2 = soup.find("h2")
print(el2)
print(el2.text)
#liタグを検索して、そのテキスト部分を表示する
el3 = soup.find("li")
print(el3)
print(el3.text)