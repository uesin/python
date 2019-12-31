#成績を定義
records = {"kanan":72,"tika":65,"riko":100,"ruby":56,"you":66,"mari":80}
#合計を求める
sum_v = 0
for v  in records.values():#点数だけ取得
    sum_v += v
ave_v = sum_v/len(records)
print("合計は",sum_v,"点")
print("平均は",ave_v,"点")

#データー一覧と平均点のさを表示
fmt = "|{0:<7}|{1:>4}|{2:>5}"#7文字左寄せ、４文字右寄せ、５文字右寄せ
print("|名前  |点数 |差")
for name,v in sorted(records.items()):
  diff_v = v - ave_v
  diff_v = round(diff_v,1)
  print(fmt.format(name, v, diff_v))