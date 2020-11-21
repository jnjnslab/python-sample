#continue 繰り返しの先頭に戻るJoe
while True:
    print('あなたはだれ?')
    name = input()
    if name != 'Joe':
        continue
    print('こんにちはJoe。パスワードは何?(魚の名前)')
    password = input()
    if password == 'sordfish':
        break
print('認証しました')