#リストを連列して文字列にする
print(','.join(['cats','bats','rats']))
print(' '.join(['cats','bats','rats']))
print(''.join(['cats','bats','rats']))
#文字列を分割してリストにする
print('cats,bats,rats'.split(','))
print('cats bats rats'.split())
spam = '''line1
line2
line3
line4'''
print(spam.split('\n'))