import random #消すと機能しない

aqours = ["松浦果南","渡辺曜","高海千歌","国木田花丸","黒澤ダイヤ","黒澤ルビィ"]
aqours.append("小原鞠莉") #リストに追加
i = random.randint(0,len(aqours)-1) #-1するのは0から始まるため

print(aqours[i])