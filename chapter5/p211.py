#GUIプログラミング

#tkinterの取り込み
from tkinter import *
import tkinter.messagebox as mb
#ボタンが押された時の動作を関数で定義
def say_hello():
  mb.showinfo("挨拶","おはヨーソロー")

#メインウィンドウの作成Tk
root  = Tk()
root.title('挨拶')#ウィンドウのタイトル

#ラベルの作成
desc_label  = Label(text = "以下のボタンを押してください")
desc_label.pack()#packでラベルをウィンドウに配置

hello_button = Button(
  text="挨拶",
  width= 10,height=3,#メインウィンドウの大きさ
  command=say_hello #ボタンを押した時のクリック動作
)
hello_button.pack()
root.mainloop() #イベントループ