#遊園地の入園料を計算するプログラム
children = int(input("13歳未満は何人ですか？"))
normal = int(input("13才〜６４才は何人ですか？"))
elder = int(input("６５歳以上は何人ですか？"))
tortal_num = children + normal + elder

children_price = 500 * children
normal_price = 1000 * normal
elder_price = 700 * elder

tortal_price = children_price + normal_price + elder_price

if tortal_num >= 10:
  print("団体割引があります")
  tortal_price = tortal_price * 0.8
else:
  print("割引はありません")
#結果表示
print("子供料金 :{0}人 × 500円 = {1}円".format(children,children_price))
print("大人料金 :{0}人 × 1000円 = {1}円".format(normal,normal_price))
print("年配料金 :{0}人 × 700円 = {1}円".format(elder,elder_price))
print("合計 : {0}人 {1}円".format(tortal_num,tortal_price))

