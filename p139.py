animal = {
  "ライオン":58,
  "チーター":100,
  "シマウマ":60,
  "トナカイ":80
}

li = sorted(animal.items(),#タップルのリストに変更
key  = lambda x :x[1],
reverse=True)

for name,speed in li:
  print(name,speed)
