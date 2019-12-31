#条件分岐

num = int(input("数値を入れてね"))

if num % 2 == 0:
  print("偶数です")
else:
  print("奇数です")

  #else省略

  level = int(input("レベルを入れてくれ"))

  if level > 5:
    print("攻撃力をあげるのだ")
  if level > 13:
    print("魔法を覚えよう")