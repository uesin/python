#カラットからグラム変換
#変換の元になる値
per_ct = 0.2
#ユーザーからの情報
user = input("何カラッとですか？")

ct = float(user)

#計算する

g = ct * per_ct

desc=("{0}カラッと={1}グラム".format(ct,g))
print(desc)

