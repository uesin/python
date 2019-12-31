#画面に３００本の線を引く
#グラフィックの盛り込み
from tkinter import *
#画面の初期化
w = Canvas(Tk(), width=900, height=400)
w.pack()
 #線をひくお

for i in range(300):
   x = i * 100

   w.create_line(x, 0, x, 400,fill = "#FF0000")

mainloop()