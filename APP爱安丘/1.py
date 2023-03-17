import random
import string
import requests

def gen_imei():
    return "".join(random.choices(string.digits + "abcdef", k=16))

imei = gen_imei()

session = requests.Session()
session.cookies.set("orgid", "137")
headers = {
    'user-agent':'chuangqi.o.137.com.iqilu.app137/0.0.36.1008',
    "cq-agent": '{"os":"android","imei":"%s"},"osversion":"6.0.1","network":"wifi","version":"0.0.36.1008","core":"1.7.4","brand":"OPPO"}'% imei,
    'content-type':'application/json',
    "orgid": "137",
    'host':'app-auth.iqilu.com',
}
print(headers)
session.headers.update(headers)

phone_number = "18979934000"
# phone_number = input("请输入手机号：")

resp = session.post(
    url="https://app-auth.iqilu.com/member/phone/code",
    data={
        "phone": phone_number,
        "senderName":"aliyun",
        "tokenCode":"",
    }
)
resp_dict = resp.json()
print(resp_dict)




# import requests
# import base64

# headers = {
#  'host':'app-auth.iqilu.com',
#  'user-agent':'chuangqi.o.137.com.iqilu.app137/0.0.36.1008',
#  'accept':'*/*',
#  'orgid':'137',
#  'cq-agent':'{"os":"android","imei":"fe9709f1c1747a90","osversion":"6.0.1","network":"wifi","version":"0.0.36.1008","core":"1.7.4","brand":"OPPO"}',
#  'content-type':'application/json',
#  'content-length':'148',
#  'accept-encoding':'gzip',
#  'cookie':'orgid=137'}
# payload=base64.b64decode("eyJwaG9uZSI6IjE4OTc5MzM1NTU0Iiwic2VuZGVyTmFtZSI6ImFsaXl1biIsInRva2VuQ29kZSI6InVwc0NPZzRYV1lTVzFQRGdyR040eVlMVW9uZGVWWXU4MUlZRm8xYklrU2JteFFibktTZDBIWDJRWlNTOG9yUDlrTHdLZHFieXBlUktvQXljMmFabDlBPT0ifQ==")
# print(payload)




