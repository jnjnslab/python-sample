import tkinter as tk

class Application(tk.Frame):
    def __init__(self,master):
        super().__init__(master)
        self.pack()

        master.geometry("700x155")
        master.title("簡易電卓")

        self.exp = ""
        self.has_op = False

        self.createButton()
        self.createCanvas()

        master.after(50, self.update)

    def createButton(self): #ボタンの配置
        tk.Button(text="AC",command=self.allclear,width=13).place(x=0, y=80)
        tk.Button(text="=",command=self.calc,width=13).place(x=100, y=80)

        tk.Button(text="+",command=lambda:self.op("+"),width=13).place(x=200, y=80)
        tk.Button(text="-",command=lambda:self.op("-"),width=13).place(x=300, y=80)
        tk.Button(text="×",command=lambda:self.op("×"),width=13).place(x=400, y=80)
        tk.Button(text="÷",command=lambda:self.op("÷"),width=13).place(x=500, y=80)
        tk.Button(text="%",command=lambda:self.op("%"),width=13).place(x=600, y=80)

        tk.Button(text="0",command=lambda:self.digit(0),width=19).place(x=0, y=105)
        tk.Button(text="1",command=lambda:self.digit(1),width=19).place(x=140, y=105)
        tk.Button(text="2",command=lambda:self.digit(2),width=19).place(x=280, y=105)
        tk.Button(text="3",command=lambda:self.digit(3),width=19).place(x=420, y=105)
        tk.Button(text="4",command=lambda:self.digit(4),width=19).place(x=560, y=105)
        tk.Button(text="5",command=lambda:self.digit(5),width=19).place(x=0, y=130)
        tk.Button(text="6",command=lambda:self.digit(6),width=19).place(x=140, y=130)
        tk.Button(text="7",command=lambda:self.digit(7),width=19).place(x=280, y=130)
        tk.Button(text="8",command=lambda:self.digit(8),width=19).place(x=420, y=130)
        tk.Button(text="9",command=lambda:self.digit(9),width=19).place(x=560, y=130)

    def digit(self, digit):
        if digit != 0 or self.exp and self.exp[-1].isdigit():
            self.exp += str(digit)

    def op(self, op):
        if self.exp and not self.has_op:
            self.exp += op
            self.has_op = True

    def calc(self):
        self.exp = str(eval(self.exp.replace("×", "*").replace("÷", "/")))
        self.has_op = False

    def allclear(self):
        self.exp = ""
        self.has_op = False

    def createCanvas(self): #キャンバスの作成
        self.canvas = tk.Canvas(self.master,width=700,height=80,bg="black")
        self.canvas.pack()
        self.resultText = self.canvas.create_text(680,40,text=self.exp,fill="white",font=("Helvetica",30,"bold"),anchor="e")

    def update(self):
        self.canvas.delete(self.resultText)
        self.resultText = self.canvas.create_text(680,40,text=self.exp,fill="white",font=("Helvetica",30,"bold"),anchor="e")

        self.master.after(50,self.update)

def main():
    win = tk.Tk()
    win.resizable(width=False, height=False) #ウィンドウを固定サイズに
    app = Application(master=win)
    app.mainloop()

if __name__ == "__main__":
    main()