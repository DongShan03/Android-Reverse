# import frida, sys, uuid
# import random


# session = frida.get_remote_device().attach("车智赢+")


# scr = """
# Java.perform(function() {
#     var LaunchModel = Java.use("com.che168.autotradercloud.launch.model.LaunchModel");

#     LaunchModel.lambda$initRequestCommonParams$0.implementation = function(i, treeMap) {
#         console.log("输入了：", treeMap);

#         var res = this.lambda$initRequestCommonParams$0(i, treeMap);
#         console.log("输出了：", res);
#         return res;
#     }
# });
# """

# script = session.create_script(scr)

# script.load()
# sys.stdin.read()

import uuid, random, base64
from Crypto.Cipher import DES3
import hashlib, requests


def md5_encrypt(input):
    obj = hashlib.md5()
    obj.update(input.encode("utf-8"))
    return obj.hexdigest()

def get_udid():
    BS = 8
    pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
    device_id = ""
    imei = str(uuid.uuid4())
    nano_time = str(random.randint(1000000000000, 100000000000000))
    text = pad(imei + "|" + nano_time + "|" + device_id).encode("utf-8")
    # text = pad("3e67fabf-6214-3681-81f6-bffe946dc8f9|13040407580188|").encode("utf-8")

    iv = b"appapich"
    key = b"appapiche168comappapiche168comap"[0: 24]

    cipher = DES3.new(key, DES3.MODE_CBC, iv)
    result = cipher.encrypt(text)
    udid = base64.b64encode(result).decode("utf-8")

    return imei, udid


def get_sign(treeMap):

    v2 = "W@oC!AH_6Ew1f6%8"

    sb = v2 + "".join([str(key) + str(value) for key, value in sorted(treeMap.items())]) + v2
    return md5_encrypt(sb)

def post_request(imei, treeMap):
    headers = {
        'host':'dealercloudapi.che168.com',
        'cache-control':'public, max-age=0',
        'traceid':f'atc.android_{imei}',
        'content-type':'application/x-www-form-urlencoded',
        'content-length':'237',
        'accept-encoding':'gzip',
        'user-agent':'okhttp/3.14.9'
    }
    url = "https://dealercloudapi.che168.com/tradercloud/sealed/login/login.ashx"

    return requests.post(url, headers=headers, data=treeMap)

def main():
    # username = input("请输入手机号：")
    # password = input("请输入密码:")
    username = "18979334079"
    password = "12315456"
    pwd = md5_encrypt(password)
    imei, udid = get_udid()
    treeMap = {
        '_appid': 'atc.android', 
        'appversion': '2.9.7',
        'channelid': 'csy',
        'pwd': pwd,
        'username': username,
        'udid': udid,
    }
    _sign = get_sign(treeMap)
    treeMap["_sign"] = _sign
    resp = post_request(imei, treeMap).text
    print(resp)


if __name__ == '__main__':
    main()
