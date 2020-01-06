#URLパラメーター値取得

#!/usr/bin/env python3
import cgi

print("Content-Type: text/html; charset=utf-8")
print("")

print("<pre>")
# URLパラメーターを取得
form = cgi.FieldStorage()
#URLパラメーターを取得して表示
mode = form.getvalue("mode", default="")
print("mode", mode)
#全てのパラメーターを取得して表示
print("---- all params ----------")

for k in form.keys():
    print(k,"=",form.getvalue(k))