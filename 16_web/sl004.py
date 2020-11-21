from selenium import webdriver
import time

#Firefoxを起動する
#browser = webdriver.Firefox()
#Chromeを起動する
browser = webdriver.Chrome()
#Edgeを起動する
#browser = webdriver.Edge(executable_path='msedgedriver.exe')
#URLを指定して開く
browser.get('https://webhtml-7f629.web.app/test2.html')

time.sleep(5)

#テキストからリンクを取得する
el = browser.find_element_by_link_text("リンク1")
#クリックする
el.click()
#現在のURLを表示する
current = browser.current_url
print(current)

time.sleep(5)
#ブラウザを終了する
browser.quit()