import requests
from bs4 import BeautifulSoup
import urllib
from pathlib import Path
import time
# Webページを取得する
load_url = "https://webhtml-7f629.web.app/test2.html"
html = requests.get(load_url)
#ダウンロードが成功したか確認する
html.raise_for_status()
#取得したページを解析のためパースする
soup = BeautifulSoup(html.content, "html.parser")
# 保存用フォルダを作る
out_folder = Path("download")
out_folder.mkdir(exist_ok=True)
# すべてのimgタグを検索し、リンクを取得する
for element in soup.find_all("img"):
    src = element.get("src")  
    # 絶対URLを作って、画像データを取得する
    image_url = urllib.parse.urljoin(load_url, src)
    imgdata = requests.get(image_url)   
    # URLから最後のファイル名を取り出して、保存フォルダ名とつなげる
    filename = image_url.split("/")[-1]
    out_path = out_folder.joinpath(filename)
    # 画像データを、ファイルに書き出す
    with open(out_path, mode="wb") as f:
        f.write(imgdata.content)
    # 1回アクセスしたので1秒待つ
    time.sleep(1)