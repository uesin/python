while True:
    tubo = input("坪数を入れて下さい")
    if tubo == "" or tubo == "q" : break
    m2 = tubo * 3.31
    s= ("{0}坪は{1}平方メートルです".format(tubo,m2))
    print(s)