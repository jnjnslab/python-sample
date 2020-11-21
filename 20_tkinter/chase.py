import tkinter as tk
import numpy as np

class Circle():
    def __init__(self,canvas,x,y,r,color,tag=None):
        self.canvas = canvas
        self.x = x #円の中心のx座標
        self.y = y #円の中心のy座標
        self.r = r #円の半径
        self.color = color
        self.tag = tag

    def createCircle(self):
        self.canvas.create_oval(self.x-self.r,self.y-self.r,self.x+self.r,self.y+self.r,fill=self.color,tag=self.tag)

class Application(tk.Frame):
    def __init__(self,master):
        super().__init__(master)
        self.pack()

        self.width=self.height=500
        master.geometry(str(self.width)+"x"+str(self.height))
        master.title("追いかけっこゲーム")

        self.canvas = tk.Canvas(master,width=self.width,height=self.height,bg="black")
        self.canvas.pack()

        self.player = Circle(self.canvas,250,250,30,"red","player") #インスタンスplayerの生成
        self.enemy = Circle(self.canvas,0,0,30,"blue","enemy") #インスタンスenemyの生成

        self.canvas.bind("<Motion>",self.mouseEvent)
        self.master.after(50,self.update)

    def update(self):
        if self.judgeflag(self.player,self.enemy):
            eV = self.enemyVec(self.player,self.enemy,10)
            self.enemy.x += eV[0]
            self.enemy.y += eV[1]
            self.canvas.delete("player")
            self.canvas.delete("enemy")
            self.player.createCircle()
            self.enemy.createCircle()

        self.master.after(50,self.update)

    def enemyVec(self,player,enemy,speed): #敵の動き(x,y)のベクトルを返す
        rad=np.arctan((player.y-enemy.y)/(player.x-enemy.x)) #向き（角度の計算）
        if player.x-enemy.x >= 0:
            vx=np.cos(rad)*speed
            vy=np.sin(rad)*speed
        else:
            vx=np.cos(rad)*(-1*speed)
            vy=np.sin(rad)*(-1*speed)
        return [vx,vy]

    def judgeflag(self,player,enemy): #当たり判定
        if np.sqrt((player.x-enemy.x)**2+(player.y-enemy.y)**2) > player.r+enemy.r: return True
        else: return False

    def mouseEvent(self,event):
        self.player.x = event.x
        self.player.y = event.y

def main():
    win = tk.Tk()
    app = Application(master=win)
    app.mainloop()

if __name__ == "__main__":
    main()