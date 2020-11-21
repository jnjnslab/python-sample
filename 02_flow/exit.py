#sys.exit() プログラムを終了する
import sys

while True:
    print('終了するにはexitと入力')
    response = input()
    if response == 'exit':
        sys.exit()
    print(response + 'と入力されました。')
print('終了')