spam='     Hello world     '
#前後の空白を除去する
print(spam.strip())
print(len(spam.strip()))
#前の空白を除去する
print(spam.lstrip())
print(len(spam.lstrip()))
#後の空白を除去する
print(spam.rstrip())
print(len(spam.rstrip()))
#前後の指定した文字を除去する
spam2 = 'aabbccSpamSpamccbbaa'
print(spam2.strip('abc'))
