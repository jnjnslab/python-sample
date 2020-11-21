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
# ファイルを書き込みモードで開く
filename = "link/linklist.txt"
with open(filename, "w", encoding='UTF-8') as f:
    # すべてのaタグを検索し、リンクを絶対URLでファイルに書き出す
    for element in soup.find_all("a"):
        url = element.get("href")
        link_url = urllib.parse.urljoin(load_url, url)
        f.write(element.text+"\n")
        f.write(link_url+"\n")
        f.write("\n")