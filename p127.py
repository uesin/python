#名前付き引数の指定
def calcTime (dist,speed):
  t = dist/speed
  t = round (t,1)
  return t
#通常の呼び出し
print( calcTime(500,100))
#名前付き呼び出し
print( calcTime(dist=500,speed=1000))