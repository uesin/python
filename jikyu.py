#時給計算プログラム

#時給の入力
user = input("時給を入力して下さい")

jikyu = int(user)

#時間の入力

user = input("働いた時間を入力して下さい")
time = int(user)

#時給計算

money = jikyu*time

fmt = """
時給{0}円で{1}時間働いたので
給料は{2}円です
"""
desc = fmt.format(jikyu,time,money)

print(desc)