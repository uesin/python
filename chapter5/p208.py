#ダイアログを使ったGUIアプリ
#ダイアログに必要の為のモジュール
import tkinter.messagebox as mb

ans = mb.askyesno("質問","ラーメンは好きですか？")

if ans == True:
  mb.showinfo("同意","僕も好きです.")
else :
  mb.showinfo("本当？","頭おかしいわね")