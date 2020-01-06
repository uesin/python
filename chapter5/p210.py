#ファイル選択の為のダイアログ

#ダイアログに必要の為のモジュール
import tkinter.filedialog as fd

#ファイル選択の為のダイアログ
path  = fd.askopenfilename(
  title = "処理ファイルを選択してください",#ダイアログ上タイトル部分
  filetypes=[('HTML','.html')]) #HTML,htmlファイルのみ表示
print(path)