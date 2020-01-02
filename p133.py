def mul_func(a,b): return a*b
def add_func(a,b): return a+b

def calc(func):
  return func(5,3)
resulut = calc(mul_func)
print (resulut)

resulut = calc(add_func)
print(resulut)