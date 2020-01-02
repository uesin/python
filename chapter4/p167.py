#QRコード作成

import qrcode
img = qrcode.make("https://www.youtube.com/")

img.save("qrcode-test.png")