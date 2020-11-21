from selenium import webdriver
import time

#Firefoxを起動する
#browser = webdriver.Firefox()
#Chromeを起動する
browser = webdriver.Chrome()
#Edgeを起動する
#browser = webdriver.Edge(executable_path='msedgedriver.exe')
#URLを指定して開く
browser.get('https://webhtml-7f629.web.app/test1.html')

#タグ名から要素を取得する
els = browser.find_elements_by_tag_name("li")
#見つかったタグの個数を表示する
print(len(els))
for el in els:
    #タグ名を表示する
    print(el.tag_name)
    #タグ内のテキスト部分を表示する
    print(el.text)

time.sleep(5)
#ブラウザを終了する
browser.quit()