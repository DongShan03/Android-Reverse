import re
import requests
import json
import time
import math
import random
import uuid

# 代理池
def get_prox():
    url = "http://webapi.http.zhimacangku.com/getip?num=11&type=2&pro=0&city=0&yys=0&port=1&pack=226047&ts=0&ys=0&cs=0&lb=1&sb=0&pb=4&mr=1&regions="
    res = requests.get(url=url).json()
    data_lis = res["data"]
    ip_list = []
    for i in data_lis:
        ip = str(i["ip"])
        port = str(i["port"])
        ip_port = f"http://{ip}:{port}"
        ip_list.append(ip_port)
    return ip_list


# 获取请求参数及cookies
def get_cookies_payload(proxy):
    session = requests.Session()
    # 获取aid cid bvid ftime stime 以及 buvid3
    # print("get_cookies_payload")
    # session.proxies = proxy
    res = session.get(url="https://www.bilibili.com/video/BV1U64y1h7Zy/?spm_id_from=333.999.0.0")
    result = re.findall(r"window.__INITIAL_STATE__=(.+);\(function",res.text)
    result = json.loads(result[0])
    aid = result["aid"]
    bvid = result["bvid"]
    cid = result["videoData"]["cid"]
    ftime = int(time.time()) - random.randint(100, 500)
    stime = int(time.time())
    buvid3_dic = res.cookies.get_dict()
    buvid3 = buvid3_dic["buvid3"]
    session.cookies.set("buvid3", buvid3)
    # b_lsid
    # 获取当前时间戳，并将其转为16进制大写;  *1000是因为python返回的是s，js是以毫秒计算
    a1 = hex(int(time.time()*1000))[2:].upper()
    # 随机生成8位16进制大写字符串
    b_lsid = ""
    for _ in range(8):
        v1 = math.ceil(16 * random.uniform(0,1))
        v2 = hex(v1)[2:].upper()
        b_lsid += v2
    a2 = b_lsid.rjust(8,"0")
    b_lsid = a1 + "_" + a2
    session.cookies.set("b_lsid", b_lsid)

    
    # 获取_uuid
    u = str(uuid.uuid4())
    time_sec = (str(int(time.time() * 1000) % 1e5)).strip(".0")
    time_sec = time_sec.rjust(5,"0")
    _uuid = u + time_sec + "infoc"
    session.cookies.set("_uuid", _uuid)


    #获取buvid4
    res = session.get(url="https://api.bilibili.com/x/frontend/finger/spi")
    dic = res.text
    dic = json.loads(dic)
    buvid4 = dic["data"]["b_4"]
    session.cookies.set("buvid4", buvid4)

    # 获取sid
    b3 = buvid3_dic["buvid3"]
    cookies = {
    "buvid3":b3,
    "CURRENT_BLACKGAP":"1",
    "CURRENT_FNVAL":"4048"
    }
    resp = session.get(url="https://api.bilibili.com/x/player/v2?aid=385535851&cid=761767676")
    sid_dic = resp.cookies.get_dict()
    sid = sid_dic["sid"]
    session.cookies.set("sid", sid)
    session.cookies.set("CURRENT_FNVAL", "4048")

    # 增加播放量的url
    url = "https://api.bilibili.com/x/click-interface/click/web/h5"
    data = {
        "aid": aid,
        "cid": cid,
        "bvid": bvid,
        "part": "1",
        "lv": "0",
        "ftime": ftime,
        "stime": stime,
        "jsonp": "jsonp",
        "type": "3",
        "sub_type": "0",
        "from_spmid": "333.1073.sub_channel.latest_video.click",
        "auto_continued_play": "0",
        "refer_url": "",
        "bsource": "",
        "spmid": "333.788.0.0"
    }
    resp = session.post(url=url,data=data)
    return aid, cid, bvid, ftime, stime, buvid3,b_lsid,_uuid,buvid4,sid

# 获取当前播放量
def get_video_id_info(video_url,proxy):
    session = requests.Session()
    session.proxies = proxy
    bvid = video_url.rsplit('/')[-1]
    res = session.get(url="https://api.bilibili.com/x/player/pagelist?bvid={}&jsonp=jsonp".format(bvid))

    cid = res.json()['data'][0]['cid']

    res = session.get(
        url="https://api.bilibili.com/x/web-interface/view?cid={}&bvid={}".format(cid, bvid))
    res_json = res.json()
    aid = res_json['data']['aid']
    view_count = res_json['data']['stat']['view']
    duration = res_json['data']['duration']
    print("\n视频 {}，平台播放量为：{}".format(bvid, view_count))
    session.close()
    return aid, bvid, cid, duration, int(view_count)



if __name__ == "__main__":
    ip_list = [None]
    video_url = "https://www.bilibili.com/video/BV1DZ4y1e7Tm"
    while True:
        i = random.choice(ip_list)
        proxy = {"http": i}
        try:
            aid, bvid, cid, duration, view_count = get_video_id_info(video_url,proxy)
            get_cookies_payload(proxy)
            view_count += 1
            print("理论刷的播放量：", view_count)
            time.sleep(10)
        except Exception as e:
            print(e)