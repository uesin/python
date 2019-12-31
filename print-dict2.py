fruits= {
  "バナナ":300,
  "オレンジ":3500,
  "りんご":700,
}

for name,price in fruits.items():
  s= "{0}は、{1}円です。".format(name,price)
  print(s)

