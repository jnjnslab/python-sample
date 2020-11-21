import tkinter as tk

#ボタンが押された時の処理
def action_btn_press():
    print("ボタンが押されました")
#ルート(メインウィンドウ)の作成
root = tk.Tk()
#タイトルの設定
root.title("タイトル")
#サイズ指定(幅:450 高さ:350 x座標:350 y座標:250)
root.geometry("450x350+350+250")
#部品(widget)の作成
#ラベル
lb = tk.Label(text="ラベル")
#ボタンにアクションを組み込む
bt = tk.Button(text="ボタン",command=action_btn_press)
#部品の配置
lb.pack()
bt.pack()
#メイン処理
root.mainloop()