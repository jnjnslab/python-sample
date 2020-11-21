from selenium import webdriver
from bs4 import BeautifulSoup
import time

#Firefoxを起動する
#browser = webdriver.Firefox()
#Chromeを起動する
browser = webdriver.Chrome()
#Edgeを起動する
#browser = webdriver.Edge(executable_path='msedgedriver.exe')
#指定したURLを開く
browser.get("http://www.google.co.jp")
#名前から要素を取得する
element = browser.find_element_by_name("q")
#入力する
element.send_keys("selenium")
#サブミットする
element.submit()

#ソースを取得する
html = browser.page_source
#取得したページを解析のためパースする
soup = BeautifulSoup(html, "html.parser")
#検索結果のリンクを取得する
elems = soup.select(".rc")
#取得数を表示する
print(len(elems))
#リンク先を表示する
for elem in elems:
    el1 = elem.select(".yuRUbf a")
    url = el1[0].get('href')
    span = el1[0].select("h3 span")
    print(span[0].text)
    print(url)

time.sleep(5)
#ブラウザを終了する
#browser.quit()