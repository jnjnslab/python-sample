from selenium import webdriver
import time

#Firefoxを起動する
#browser = webdriver.Firefox()
#Chromeを起動する
browser = webdriver.Chrome()
#browser = webdriver.Chrome(executable_path=r'C:\lib\chromedriver.exe')
#Edgeを起動する
#browser = webdriver.Edge(executable_path='msedgedriver.exe')

#URLを指定して開く
browser.get('https://webhtml-7f629.web.app/test1.html')

#タイトル
print(browser.title)
#ソース取得
html = browser.page_source
print(html)
#現在のURL
current = browser.current_url
print(current)

time.sleep(5)
#ブラウザを終了する
browser.quit()