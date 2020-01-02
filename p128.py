#可変長引数
#可変長引数とは引数の数を変えられて何個でも引数に指定ができる。変数の前に＊をつける。

def sumargs(*args):
  v = 0
  for n in args:
    v+=n
  return v
print (sumargs(1,2,3))
print (sumargs(1,2,3,4,5,6,7,8,9,10))
print (sumargs(1,2,3,1000,40000))
