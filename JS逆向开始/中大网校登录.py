import requests
import base64
from Crypto.Cipher import PKCS1_v1_5
from Crypto.PublicKey import RSA


userName = "18979334079"
password = "cheng521210"

headers = {
    "Content-Type": "application/json;charset=UTF-8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
}

sess = requests.Session()
sess.get("https://user.wangxiao.cn/login")

verify_code_url = "https://user.wangxiao.cn/apis/common/getImageCaptcha"
verify_code_resp = sess.post(verify_code_url, headers=headers)
image_base64 = verify_code_resp.json()["data"].split(",")[1]
image = base64.b64decode(image_base64)


get_time_url = "https://user.wangxiao.cn/apis//common/getTime"
get_time_resp = sess.post(get_time_url, headers=headers)
get_time_data = get_time_resp.json()["data"]
password = password + str(get_time_data)



public_key = "-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDA5Zq6ZdH/RMSvC8WKhp5gj6Ue4Lqjo0Q2PnyGbSkTlYku0HtVzbh3S9F9oHbxeO55E8tEEQ5wj/+52VMLavcuwkDypG66N6c1z0Fo2HgxV3e0tqt1wyNtmbwg7ruIYmFM+dErIpTiLRDvOy+0vgPcBVDfSUHwUSgUtIkyC47UNQIDAQAB\n-----END PUBLIC KEY-----"
rsa_key = RSA.import_key(public_key)

rsa = PKCS1_v1_5.new(rsa_key)
mi = rsa.encrypt(password.encode("utf-8"))
print(base64.b64encode(mi).decode("utf-8"))

