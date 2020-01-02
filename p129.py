#ローカル変数とグローバル変数
#ローカル変数はその関数のなかでのみ有効
#変数の有効範囲をスコープと呼ぶ


value = 100

def changevalue():
  #valueをグローバル宣言 global 変数名で関数外でも使える
  global value
  #関数の内側でvalueを変更
  value = 20
changevalue()
print (value)