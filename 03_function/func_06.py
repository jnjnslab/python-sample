#ローカルスコープからグローバル変数を変更する
def spam():
    global eggs
    eggs = 'spam'

eggs = 'global'
spam()
print(eggs)