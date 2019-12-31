def calcvalue(who,hour,count,value):
  '''あるスーパーの割引をする計算'''
  info = "割引なし"
  #１４時に３つ以上で１割引き
  if (hour == 14) and (count >= 3 ):
    value *=0.9
    info ="一割引"
  #１５時に５個以上で２割引き
  if (hour == 15) and (count >= 5):
    value *= 0.8
    info = "２割引き"
  value = int(value)
  print("{0}さんは{1}={2}円".format(who,info,value))
#結果を表示する所まで関数やからreturnがいらん
calcvalue("A",15,3,1200)
calcvalue("B",14,5,2000)
calcvalue("C",15,8,5400)
