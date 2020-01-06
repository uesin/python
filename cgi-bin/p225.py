#!/usr/bin/env python3
#足算を行うプログラム
import cgi

print("Content-Type: text/html; charset=utf-8")
print("")

#フォームの取得
form = cgi.FieldStorage()

#フォームにデーターがあるかどうか
if (not 'v1' in form) or (not 'v2' in form):
  print("""
      <form>
      <input type="text" name="v1"> +
      <input type="text" name="v2">
      <input type="submit" value="計算">
      </form>
  """)
#フォームの値を取得して計算
else:
    v1 = form.getvalue("v1","0")
    v2 = form.getvalue("v2","0")
    try:
        ans = int(v1) + int(v2)
    except:
        ans = 0
    print("<h1>", ans, "</h1>")
