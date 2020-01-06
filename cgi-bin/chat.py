#!/usr/bin/env python3

import cgi
import cgitb
import os.path
import html
#プラウザでのデバックを有効にする
cgitb.enable()

#全体の設定
FILE_LOG = "chat-log.txt"

#HTMLを画面に出力
def print_html(body):
  #ヘッダ出力
  print("Content-Type: text/html; charset=utf-8")
  print("")
  #HTMLを出力
  print("""
<html><head><mata charset="utf-8">
<title>チャット</title></head><body>
<h1>チャット</h1>
<div><form>
名前:<input type="text" name="name" size="8">  
本文:<input type="text" name="body" size="20">
<input type="submit" value="発言">
<input type="hidden" name="mode" value="write">
</form></div><hr>
{0}
</body></html>
  """.format(body))
#画面に書き込みログを表示する
def mode_read(form):
  #ログの読み取り
  log = ""
  if os.path.exists(FILE_LOG):
    with open(FILE_LOG, "r", encoding='utf-8') as f:
        log = f.read()
  print_html(log)
#任意のURLにジャンプする
def jump(url):
  #ヘッダ出力
  print("Status: 301 Moved Permanetly")
  print("Location: " + url)
  print("")
  #HTMLを出力（ヘッダがうまくいかなかった時の対策）
  print('<html><head>')
  print('<meta http-equiv="refresh" content="0;'+url+'">')
  print('</head><body>')
  print('<a href="'+url+'">jump</a></body></html>')
def mode_write(form):
  name = form.getvalue("name","no name")
  body = form.getvalue("body","")
  #HTMLに変換
  name = html.escape(name)
  body = html.escape(body)
  #ファイルに保存
  with open(FILE_LOG, "a+", encoding='utf-8') as f :
      f.write("<p>{0}: {1}</p><hr>\n".format(name,body))
  #書き込み後にリダイレクトする
  jump('chat.py')

#メイン処理
def main():
#フォームの取得
  form = cgi.FieldStorage()
  #modeパラメーター取得
  mode = form.getvalue("mode", "read")
  #modeの値によって処理を変更
  if mode == "read": mode_read(form)
  elif mode =="write": mode_write(form)
  else: mode_read(form)
if __name__ == "__main__": #---
    main()