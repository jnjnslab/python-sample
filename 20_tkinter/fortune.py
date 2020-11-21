import tkinter as tk
import time
import random as rd


class Fortune():
    def __init__(self,canvas,x,y,color,tag):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.color = color
        self.tag = tag

    def createFortuneBox(self): #くじ箱を作る
        self.canvas.create_polygon(self.x,self.y,self.x+20,self.y-25,self.x+80,self.y-25,self.x+100,self.y,self.x+100,self.y+100,self.x+80,self.y+125,self.x+20,self.y+125,self.x,self.y+100,fill=self.color,tag=self.tag)
        self.createFortuneText()

    def createFortuneText(self): #おみくじの文字を表示
        return self.canvas.create_text(self.x+50,self.y+50,text="お\nみ\nく\nじ",font=("Helvetica", 18, "bold"),fill="white",tag=self.tag)

    def drawLots(self): #くじ箱の動き
        sleepTime=0.03

        for i in range(10):
            self.canvas.move(self.tag,0,5)
            time.sleep(sleepTime)
            self.canvas.update()
            self.canvas.move(self.tag,-5,0)
            time.sleep(sleepTime)
            self.canvas.update()
            self.canvas.move(self.tag,0,-5)
            time.sleep(sleepTime)
            self.canvas.update()
            self.canvas.move(self.tag,5,0)
            time.sleep(sleepTime)
            self.canvas.update()

        self.resultLots()

    def resultLots(self): #結果を表示
        resultNumber=rd.randint(1,28)

        if resultNumber==1:
            self.canvas.create_polygon(self.x+25,self.y-50,self.x+75,self.y-50,self.x+75,self.y-25,self.x+25,self.y-25,fill="yellow",tag="lot")
            self.canvas.create_text(self.x+150,self.y,text="大\n吉",font=("Helvetica", 30, "bold"),fill="yellow",tag="resultText")
        elif resultNumber>1 and resultNumber<=3:
            self.canvas.create_polygon(self.x+25,self.y-50,self.x+75,self.y-50,self.x+75,self.y-25,self.x+25,self.y-25,fill="orange",tag="lot")
            self.canvas.create_text(self.x+150,self.y,text="吉",font=("Helvetica", 30, "bold"),fill="orange",tag="resultText")
        elif resultNumber>3 and resultNumber<=6:
            self.canvas.create_polygon(self.x+25,self.y-50,self.x+75,self.y-50,self.x+75,self.y-25,self.x+25,self.y-25,fill="pink",tag="lot")
            self.canvas.create_text(self.x+150,self.y,text="中\n吉",font=("Helvetica", 30, "bold"),fill="pink",tag="resultText")
        elif resultNumber>6 and resultNumber<=10:
            self.canvas.create_polygon(self.x+25,self.y-50,self.x+75,self.y-50,self.x+75,self.y-25,self.x+25,self.y-25,fill="green",tag="lot")
            self.canvas.create_text(self.x+150,self.y,text="小\n吉",font=("Helvetica", 30, "bold"),fill="green",tag="resultText")
        elif resultNumber>10 and resultNumber<=15:
            self.canvas.create_polygon(self.x+25,self.y-50,self.x+75,self.y-50,self.x+75,self.y-25,self.x+25,self.y-25,fill="blue",tag="lot")
            self.canvas.create_text(self.x+150,self.y,text="末\n吉",font=("Helvetica", 30, "bold"),fill="blue",tag="resultText")
        elif resultNumber>15 and resultNumber<=21:
            self.canvas.create_polygon(self.x+25,self.y-50,self.x+75,self.y-50,self.x+75,self.y-25,self.x+25,self.y-25,fill="white",tag="lot")
            self.canvas.create_text(self.x+150,self.y,text="凶",font=("Helvetica", 30, "bold"),fill="white",tag="resultText")
        else:
            self.canvas.create_polygon(self.x+25,self.y-50,self.x+75,self.y-50,self.x+75,self.y-25,self.x+25,self.y-25,fill="gray",tag="lot")
            self.canvas.create_text(self.x+150,self.y,text="大\n凶",font=("Helvetica", 30, "bold"),fill="gray",tag="resultText")


class Application(tk.Frame):
    def __init__(self,master):
        super().__init__(master)
        self.pack()

        self.width=self.height=300
        self.buttonClick=True

        master.geometry(str(self.width)+"x"+str(self.height))
        master.title("おみくじ")

        self.canvas = tk.Canvas(master,width=self.width,height=self.height,bg="black") #キャンバスの作成
        self.canvas.pack()

        self.omikuji = Fortune(self.canvas,100,90,"red","omikuji") #インスタンスomikujiの生成
        self.omikuji.createFortuneBox()

        self.drawButton = tk.Button(text="くじを引く",command=self.drawButtonClick,width=10) #くじを引くボタンの作成
        self.drawButton.place(x=110, y=250)

    def drawButtonClick(self): #ボタンが押されたら
        if self.buttonClick:
            self.buttonClick=False
            self.canvas.delete("lot")
            self.canvas.delete("resultText")
            self.omikuji.drawLots()
            self.buttonClick=True

def main():
    win = tk.Tk()
    app = Application(master=win)
    app.mainloop()

if __name__ == "__main__":
    main()