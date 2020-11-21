#英文字だけか判定する
print('hello'.isalpha())
print('hello123'.isalpha())
#英文字と数字だけか判定する
print('hello'.isalnum())
print('hello123'.isalnum())
print('123'.isalnum())
print('hello123#'.isalnum())
#数字だけか判定する
print('123'.isdecimal())
print('hello'.isdecimal())
#スペース、タブ、改行のみか判定する
print(' '.isspace())
print(' \t\n'.isspace())
#単語の先頭が大文字で残りが小文字か判定する
print('This Is Title Case'.istitle())
print('This Is not Title Case'.istitle())
