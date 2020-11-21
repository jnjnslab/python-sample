from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.alert import Alert
import time

#Firefoxを起動する
#browser = webdriver.Firefox()
#Chromeを起動する
browser = webdriver.Chrome()
#Edgeを起動する
#browser = webdriver.Edge(executable_path='msedgedriver.exe')
#URLを指定して開く
browser.get('https://webhtml-7f629.web.app/coffee.html')

#プルダウン要素からvalueで選択する
el1 = browser.find_element_by_name("num")
select_num = Select(el1)
select_num.select_by_value("1")
select_num.select_by_value("2")
#ラジオボタンを選択する
#element = browser.find_element_by_xpath("/html/body/form/input[2]")
el2 = browser.find_element_by_css_selector("input[type=radio][value='ice']")
el2.click()
#チェックボックスを操作する
chk_sugar = browser.find_element_by_css_selector("input[name='included'][value='sugar']")
chk_milk = browser.find_element_by_css_selector("input[name='included'][value='milk']")
chk_cream = browser.find_element_by_css_selector("input[name='included'][value='cream']")
chk_sugar.click()
print(chk_sugar.is_selected())
print(chk_milk.is_selected())
print(chk_cream.is_selected())
#キー入力する
el4 = browser.find_element_by_name("remarks")
el4.send_keys("熱めでお願いします")

time.sleep(5)
#サブミット
el5 = browser.find_element_by_css_selector("input[type='submit']")
el5.click()

#AlertでOKを押下
Alert(browser).accept()
#AlertでCancelを押下
#Alert(browser).dismiss()

#現在のURLを表示する
print(browser.current_url)

time.sleep(5)
#ブラウザを終了する
browser.quit()