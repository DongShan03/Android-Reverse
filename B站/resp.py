import requests
import json
import re
import time, random
import math

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
}

start_url = "https://www.bilibili.com/video/BV1U64y1h7Zy/?spm_id_from=333.999.0.0"

#获取随机16进制数
def get_random_hex_number(num) -> str:
    data = ""
    for _ in range(num):
        v1 = math.floor(16 * random.uniform(0, 1))
        v2 = hex(v1)[2:].upper()
        # print(v2)
        data += v2
    data = data.rjust(num, "0")
    return data

#计算b_lsid
def get_b_lsid():
    t = hex(int(time.time() * 1000))[2:]
    data = get_random_hex_number(8)
    return f"{data}_{t}"

#计算_uuid
def get__uuid():
    values = []
    for value in [8, 4, 4, 4, 12]:
        values.append(get_random_hex_number(value))
    return "-".join(values) + str(int(time.time() * 1000 % 1e5)).rjust(5, "0") + "infoc"

def get_sid(cookies):
    url = f"https://api.bilibili.com/x/player/v2?aid={cookies['aid']}&cid={cookies['cid']}"
    real_time_cookies = {
        "buvid3": cookies["buvid3"],
        "b_nut": cookies["b_nut"],
        "CURRENT_FNVAL": "4048",
    }
    resp = requests.get(url, cookies=real_time_cookies, headers=headers)
    return resp.cookies.items()[0][1]

#获取buvid4
def get_buvid4(cookies):
    url = "https://api.bilibili.com/x/frontend/finger/spi"
    real_time_cookies = {
        "buvid3": cookies["buvid3"],
        "b_nut": cookies["b_nut"],
        "CURRENT_FNVAL": cookies["CURRENT_FNVAL"],
        "sid": cookies["sid"],
        "b_lsid": cookies["b_lsid"],
        "_uuid": cookies["_uuid"],
    }
    resp = requests.get(url, cookies=real_time_cookies, headers=headers).json()
    return resp['data']["b_4"]

def get_video_info(session, aid):
    url = f"https://api.bilibili.com/x/web-interface/view?aid={aid}"
    resp = session.get(url=url, headers=headers).json()
    view_count = resp["data"]["stat"]["view"]
    print(f"原视频播放量: {view_count}")
   
def increase_view_count(cookies):
    ctime = int(time.time())
    url = "https://api.bilibili.com/x/click-interface/click/web/h5"
    data={
        "aid": str(cookies['aid']),
        "cid": str(cookies['cid']),
        "part": "1",
        "lv": "0",
        "ftime": ctime - random.randint(100, 500),
        "stime": ctime,
        "type": "3",
        "sub_type": "0",
        "refer_url": "https://www.bilibili.com/",
        "spmid": "",
        "from_spmid": "",
        "csrf" : "",
    }
    resp = requests.post(url, data=data, headers=headers, cookies=cookies)
    print(resp)

def get_cookies(session):
    # while True:
    resp = session.get(url=start_url, headers=headers)
    data_list = re.findall(r"window.__INITIAL_STATE__=(.+);\(function", resp.text)
    data_dict = json.loads(data_list[0])
    get_video_info(session, data_dict["aid"])

    cookies = resp.cookies.get_dict()
    cookies["aid"] = data_dict["aid"]
    cookies["cid"] = data_dict["videoData"]["cid"]
    cookies["bvid"] = data_dict["bvid"]
    cookies["b_lsid"] = get_b_lsid()
    cookies["_uuid"] = get__uuid()
    cookies["theme_style"] = "light"
    cookies["buvid_fp_plain"] = "undefined"
    cookies["CURRENT_FNVAL"] = "4048"
    cookies["sid"] = get_sid(cookies)
    cookies["buvid4"] = get_buvid4(cookies)
    return dict(cookies)

def main():
    session = requests.Session()
    cookies = get_cookies(session)
    # for key, value in cookies.items():
    #     session.cookies.update({key: value})
    increase_view_count(cookies)
    


if __name__ == "__main__":
    main()