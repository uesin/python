#数値文字列連結
kion_i = 30
kion = str(kion_i)
print("今日の気温は" + kion + "度です")

name = "kanan"

age = 19

desc = name + "は今年で" + str(age) + "才です"
print(desc)

#インチをセンチメートルに変換

per_inch = 2.54

inch = 24

cm = inch*per_inch

desc = str(inch) + "インチ = "  +str(cm) + "センチ"

print(desc)

per_inch = 2.54

#formatver
per_inch = 2.54


inch = 24

cm = inch * per_inch

desc = "{0}インチ = {1}センチ".format(inch,cm)

print(desc)

#名前付き引数ver

print("私は{name}です".format(name="ミドリ"))

fmt = "年齢は,{age}才で, {job}をやってます。"
s = fmt.format(age = 22,job = "プログラマー")
print(s)