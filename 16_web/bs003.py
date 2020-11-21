import requests
from bs4 import BeautifulSoup
# Webページを取得する
load_url = "https://webhtml-7f629.web.app/test2.html"
html = requests.get(load_url)
#ダウンロードが成功したか確認する
html.raise_for_status()
#取得したページを解析のためパースする
soup = BeautifulSoup(html.content, "html.parser")
# idで検索し、その中のすべてのliタグを検索して表示する
chap2 = soup.find(id="chap2")
print(chap2)
elements = chap2.find_all("li")
for element in elements:
    print(element.text)
