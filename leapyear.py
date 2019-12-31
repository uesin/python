year = int(input("西暦何年ですか？"))
is_leap = False
#(1)4で割れたらうるう年
if year % 4 == 0:
  #（２）100で割れたらうるう年ではない
  if year % 100 == 0:
    #(3)400で割り切れればうるう年
    if year % 400 == 0:
      is_leap = True
    else:
      is_leap = False
  else:
    is_leap = True
else:
  is_leap = False
if is_leap:
    print("うるう年")
else:
    print("平年です")

# 書き換え

year = int(input("西暦何年ですか？"))

is_leap = False
if year % 400 == 0:
  is_leap = True
elif year % 100 == 0:
  is_leap = False
elif year % 4 == 0:
  is_leap = True
else:
    is_leap = False
if is_leap == True:
  print("うるう年")
else:
  print("平年です")

#書き換え論理演算
year = int(input("西暦何年ですか？"))

is_leap = (year % 400 == 0) or ((year % 100 != 0 and year % 4 == 0))
if is_leap == True:
  print("うるう年")
else:
  print("平年です")




    