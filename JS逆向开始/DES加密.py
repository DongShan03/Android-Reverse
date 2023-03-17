import base64
from Crypto.Cipher import DES

s = "二比"


des = DES.new(b'alexissb', mode=DES.MODE_CBC, IV=b'01020304')
bs = s.encode("utf-8")
que = 8 - len(bs) % 8
bs += (que * chr(que)).encode("utf-8")

result = des.encrypt(bs)
print(result)

