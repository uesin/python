#名前は？
name = input("お名前は？")
#挨拶は？
print(name+"さん,こんにちは!")


#変数の元になる値
per_inch = 2.54

#ユーザーから入力を得る

user = input("inch? ")

inch = float(user)

cm = inch * per_inch

desc = "{0}inch =　{1}cm".format(inch, cm)

print(desc)