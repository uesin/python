#ファイルの書き込み
a_file = open("test.txt", mode= "w",encoding="utf-8")
try:
  a_file.write("私は失敗した事がない。\n")
  a_file.write("ただ一万通りの方法を\n 見つけただけだ。\n")
  a_file.write("トーマスエジソン\n")
finally:
  a_file.close()