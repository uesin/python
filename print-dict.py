fruits= {
  "バナナ":300,
  "オレンジ":3500,
  "りんご":700,
}
for name in fruits.keys():

  price = fruits[name]

  s= "{0}は、{1}円です。".format(name,price)

  print(s)

for name,price in fruits.items():
  s= "{0}は、{1}円です。".format(name,price)
  print(s)


