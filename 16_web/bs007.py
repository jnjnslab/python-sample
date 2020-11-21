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
# すべてのimgタグを検索し、リンクを表示する
for element in soup.find_all("img"):
    src = element.get("src") 
    # 絶対URLと、ファイルを表示する
    image_url = urllib.parse.urljoin(load_url, src)
    filename = image_url.split("/")[-1] #画像ファイル名部分を切り取る
    print(image_url, ">>", filename)
