#breakによる繰り返しの中断
name = ''
while True:
    print('あなたの名前を入力してください')
    name = input()
    if name == 'Tom':
        break
print('どうも!')