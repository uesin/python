#無名関数 lamda式を使う 名前のない関数
# v  = lamda 引数1,引数2,引数3,:式

def calc(func):
  return func(5,3)
resulut = calc (lambda a, b : a*b )
print(resulut)

resulut = calc (lambda a, b : a+b )
print(resulut)

#関数を定義する手間が省ける。