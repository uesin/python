from tkinter import * 

#テキスト文字を数える関数
def count_text(event):
  s = main_text.get(1.0, END)
  info_label.config(text="{0}文字".format(len(s)))

root = Tk()
root.title("テキストカウンタ")

#テキストボックスを作成
main_text = Text(root)
main_text.bind("<Key>", count_text)#キーボードからの文字入力の際count_text(event)を実行bind()メソッド
main_text.pack()

#文字を表示するラベル
info_label = Label(root)
info_label.pack()

root.mainloop()