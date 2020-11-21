import tkinter as tk

class Application(tk.Frame):
    #コンストラクター
    def __init__(self,master):
        super().__init__(master)
        self.pack()
        #タイトルの設定
        master.title("テキストボックスの内容を取得")
        #サイズ指定(幅:450 高さ:350 x座標:350 y座標:250)
        master.geometry("450x350+400+150")
         #部品の作成/配置
        self.create_widget()
    #部品の作成/配置
    def create_widget(self):
        #ラベル
        self.lb = tk.Label(self)
        self.lb["text"] = "ラベル"
        self.lb.pack(side="top")
        #テキストボックス
        self.en = tk.Entry(self)
        self.en.pack()
        self.en.focus_set()
        #ボタンにアクションを組み込む
        self.bt = tk.Button(self)
        self.bt["text"] = "ボタン"
        self.bt["command"] = self.print_txtval
        self.bt.pack(side="bottom")
    #ボタンが押された時の処理
    def print_txtval(self):
        #テキストボックスの内容を取得する
        val_en = self.en.get()
        print(val_en)

#ルート(メインウィンドウ)の作成
root = tk.Tk()
#
app = Application(master=root)
#メイン処理
root.mainloop()