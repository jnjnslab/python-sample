from selenium import webdriver
from bs4 import BeautifulSoup
import time

#SeleniumとBeautifulSoupを組み合わせる

#Firefoxを起動する
#browser = webdriver.Firefox()
#Chromeを起動する
browser = webdriver.Chrome()
#Edgeを起動する
#browser = webdriver.Edge(executable_path='msedgedriver.exe')
#URLを指定して開く
browser.get('https://webhtml-7f629.web.app/test2.html')

#タイトルを表示する
print(browser.title)
#ソースを取得する
html = browser.page_source
#取得したページを解析のためパースする
soup = BeautifulSoup(html, "html.parser")
# すべてのaタグを検索して、リンクを表示する
for element in soup.find_all("a"):
    #タグ内のテキスト部分を表示する
    print(element.text)
    #href属性(リンク)先を表示する
    url = element.get("href")
    print(url)

time.sleep(5)
#ブラウザを終了する
browser.quit()