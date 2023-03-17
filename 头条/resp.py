# import requests
# import execjs

# url = 'https://www.toutiao.com/api/pc/list/feed?channel_id=3189398996&min_behot_time=0&refresh_count=1&category=pc_profile_channel'

# _signature = execjs.compile(open("./sdk2.js", mode="r", encoding="utf-8").read()).call("get_signature", url)

# final_url = url + f"&_signature={_signature}"

# headers = {
#  'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
#  'Host':'www.toutiao.com',
#  'Content-Type':'text/plain'}

# resp = requests.request("GET", final_url, headers=headers, data=None)
# print(resp.text)

from Crypto.Cipher import AES
import base64
import binascii

password = bytes('1234567812345678', encoding="UTF-8") #秘钥，b就是表示为bytes类型
iv = bytes('1234567812345678', encoding="UTF-8") # iv偏移量，bytes类型
text = bytes('abcdefghijklmnhi', encoding="UTF-8") #需要加密的内容，bytes类型
aes = AES.new(password, AES.MODE_CBC, iv) #创建一个aes对象
# AES.MODE_CBC 表示模式是CBC模式
en_text = aes.encrypt(text)
print(en_text) 
hex_text = binascii.b2a_hex(en_text)
print("密文：", hex_text) #加密明文，bytes类型
aes = AES.new(password, AES.MODE_CBC, iv) #CBC模式下解密需要重新创建一个aes对象
den_text = aes.decrypt(en_text)
print("明文：",den_text.decode("utf-8"))
