#Crypto.CipherからAESを使う事を宣言
from Crypto.Cipher import AES
import base64
#暗号化したいデーターとパスワードを指定
message = "あけましておめでとうございます"
password  = "aaaaaaaa" #適当なパスワードを指定
iv = "abcdefgh12345678" #初期ベクトル(16文字で適当な値を指定)
mode = AES.MODE_CBC # 暗号化モードを指定

def mkpad(s,size):
  s = s.encode("utf-8")#UTF-8文字列をバイト列に変換
  pad = b'' * (size - len(s) % size)#特定の長さの文字列にする為に空白を生成
  return s  + pad 
#暗号化する
def encrypt(password,data):
  password = mkpad(password,16) #任意の倍数に変更
  data = mkpad(data,16)#バイト列に変換して１６の倍数に揃える
  password = password[:16]#ちょうど１６文字に揃える
  #暗号化
  aes = AES.new(password,mode,iv)
  data_cipher = aes.encrypt(data)
  return base64.b64decode(data_cipher).decode("utf-8")
#復号化する
def decrypt(password,encdata):
  password = mkpad(password,16) #任意の倍数に変更
  password = password[:16]#ちょうど１６文字に揃える
  #復号化
  aes = AES.new(password,mode,iv)
  encdata = base64.b64decode(encdata)
  data  = aes.decrypt(encdata)
  return data.decode("utf-8")
#暗号化する
enc  = encrypt(password,message)
#復号化する
dec = decrypt(password,enc)

print("暗号化:",enc)
print("復号化:",dec)
