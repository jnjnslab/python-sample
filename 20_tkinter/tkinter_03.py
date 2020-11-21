import tkinter as tk

#ボタンが押された時の処理
def print_txtval():
    #テキストボックスの内容を取得する
    val_en = en.get()
    print(val_en)
#ルート(メインウィンドウ)の作成
root = tk.Tk()
#タイトルの設定
root.title("テキストボックスの内容を取得")
#サイズ指定(幅:450 高さ:350 x座標:350 y座標:250)
root.geometry("450x350+400+150")
#部品(widget)の作成
#ラベル
lb = tk.Label(text="ラベル")
#ボタンにアクションを組み込む
bt = tk.Button(text="ボタン",command=print_txtval)
#テキストボックス
en = tk.Entry()
#部品の配置
[widget.pack() for widget in(lb,en,bt)]
#メイン処理
root.mainloop()