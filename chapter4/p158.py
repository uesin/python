#特定のモジュールのみインポート

#from p156 import syaku_to_cm  #*にするとモジュールの全てをインポート

#モジュールに別名を付けれる as 

from p156 import syaku_to_cm as sc2cm

print("10尺=",sc2cm(10),"cm")
print("20尺=",sc2cm(20),"cm")
