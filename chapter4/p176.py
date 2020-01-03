#with構文/使う事で自動的にcloseメソッドを自動的に読んでくれる

with  open("test.txt2", mode= "w",encoding="utf-8") as f:
  f.write("私は失敗した事がない。\n")
  f.write("ただ一万通りの方法を\n 見つけただけだ。\n")
  f.write("トーマスエジソン\n")