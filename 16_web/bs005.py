import requests
from bs4 import BeautifulSoup
import urllib
# Webページを取得する
load_url = "https://webhtml-7f629.web.app/test2.html"
html = requests.get(load_url)
#ダウンロードが成功したか確認する
html.raise_for_status()
#取得したページを解析のためパースする
soup = BeautifulSoup(html.content, "html.parser")
# すべてのaタグを検索し、リンクを絶対URLで表示する
for element in soup.find_all("a"):
    print(element.text)
    url = element.get("href")
    print(url)
    link_url = urllib.parse.urljoin(load_url, url)
    print(link_url)
