import requests
from bs4 import BeautifulSoup
# Webページを取得する
load_url = "https://webhtml-7f629.web.app/test1.html"
html = requests.get(load_url)
#ダウンロードが成功したか確認する
html.raise_for_status()
#取得したページを解析のためパースする
soup = BeautifulSoup(html.content, "html.parser")
# すべてのliタグを検索して、その文字列を表示する
elements = soup.find_all("li")
for element in elements:
    print(element)
    print(element.text)