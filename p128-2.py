#辞書型可変長引数
#変数名の前にアスタリスクを２個つける(**args)
  

def sample(**args):
  print(args)
sample(a=30,b=50,c=40)
sample(aa="hoge",bb="fuga")

#アスタリスク１つだとタプルにアスタリスク２つだと辞書型になる。