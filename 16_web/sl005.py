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

#スクリーンショットを取得する
browser.save_screenshot('image/screenshot.png')

time.sleep(5)
#ブラウザを終了する
browser.quit()