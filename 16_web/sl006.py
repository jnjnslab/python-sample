from selenium import webdriver
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

time.sleep(5)
#ブラウザを終了する
browser.quit()