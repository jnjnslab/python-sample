#lambda式  lambda {仮引数}:{処理}
items = ["aaa","bbb","ccc"]
items2 = map(lambda arg: arg + ".html", items)
for item in items2:
    print(item)
