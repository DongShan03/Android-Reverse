from Crypto.Cipher import AES
import base64

# s = "瓦哈提"

# """
# key:
#     16, 24, 32
# """
# bs = s.encode("UTF-8")
# que = 16 - len(bs) % 16
# bs += (que * chr(que)).encode("UTF-8")
# aes = AES.new(b'jajajajajajajaja', mode=AES.MODE_CBC, IV=b'0102030405060708')

# result = aes.encrypt(bs)
# b64 = base64.b64encode(result).decode("utf-8")
# print(b64)
miwen = "esw6l2wvUrDIX5Atki9Wzw=="
aes = AES.new(b'jajajajajajajaja', mode=AES.MODE_CBC, IV=b'0102030405060708')
bs = base64.b64decode(miwen)

result = aes.decrypt(bs)
print(result.decode("utf-8"))
