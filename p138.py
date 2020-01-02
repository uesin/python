#リストの値を並び替えよう

#sorted( データの型,key = 無名関数,reverse=True or False(デフォルトは小さい順))

animal = [
  ("ライオン",580,200),
  ("チーター",110,599),
  ("シマウマ",600,500),
  ("トナカイ",80,7000),
]
faster = sorted( animal,key = lambda ani :ani[1],reverse=True) #キーの番号が関係してくる。

for i in faster : print(i)