import requests
import time
from urllib.parse import quote
import random
import hmac
from hashlib import sha1


def gen_random_mac(sep=":"):

    def mac_same_char(mac_string):
        v0 = mac_string[0]
        index = 1
        while index < len(mac_string):
            if v0 != mac_string[index]:
                return False
            index += 1
        return True

    mac_part = []
    for _ in range(6):
        part = "".join(random.sample("0123456789ABCDEF", 2))
        mac_part.append(part)
    mac = sep.join(mac_part)

    if not mac_same_char(mac) and mac != "00:90:4C:11:22:33":
        return mac
    return gen_random_mac(sep)

def signature(appid, sign_version, data, ts):
    key = "dd49a835-56e7-4a0f-95b5-efd51ea5397f"

    v23 = "{}{}{}{}".format(appid, sign_version, data, ts)
    mac_code = hmac.new(key.encode("utf-8"), v23.encode("utf-8"), sha1)
    return mac_code.hexdigest()


def get_udid():
    gen_mac = gen_random_mac()

    sign_version = 2
    appid = 1355
    ts = int(time.time())
    data = "app_build=1031&app_version=5.32.1&bt_ck=1&bundle_id=com.zhihu.android&cp_ct=4&cp_fq=2803200&cp_tp=ARMv8%20processor%20rev%201%20%28aarch64%29&cp_us=51.612904&d_n=M2007J22C&fr_mem=9&fr_st=116623&im_e=354730440868028&latitude=0.0&longitude=0.0&mc_ad={}&mcc=CN&nt_st=1&ph_br=Xiaomi&ph_md=M2007J22C&ph_os=Android%209&ph_sn=bb18a3e8ef015e7f&pvd_nm=CHINA%20MOBILE&tt_mem=18&tt_st=120026&tz_of=28800".format(quote(gen_mac))
    sign = signature(appid, sign_version, data, ts)

    headers = {
        'x-app-id': str(appid),
        'x-req-ts': str(ts),
        'x-sign-version': str(sign_version),
        'x-req-signature': str(sign),
        'user-agent': 'com.zhihu.android/Futureve/5.32.1 Mozilla/5.0 (Linux; Android 9; M2007J22C Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4515.131 Mobile Safari/537.36',
    }

    resp = requests.post('https://appcloud.zhihu.com/v1/device', headers=headers, data=data)
    return resp.json()["udid"]

def get_hd(udid):
    url = "https://api.zhihu.com/guests/token"

    headers = {
        'x-udid': udid,
        'Host': 'api.zhihu.com',
    }

    resp = requests.post(url, headers=headers)
    return resp.json()["id"]


udid = get_udid()
hd = get_hd(udid)
print(hd)
