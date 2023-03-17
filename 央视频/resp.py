import execjs
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import time, datetime
import requests, json
import re
from concurrent.futures import ThreadPoolExecutor
import binascii

def aes_encrypt(data):
    key_str = "4E2918885FD98109869D14E0231A0BF4"
    key = binascii.a2b_hex(key_str)

    iv_str = "16B17E519DDD0CE5B79D7A63A4DD801C"
    iv = binascii.a2b_hex(iv_str)

    aes = AES.new(
        key=key,
        mode=AES.MODE_CBC,
        iv=iv
    )
    raw = pad(data.encode("utf-8"), 16)
    aes_bytes = aes.encrypt(raw)
    return binascii.b2a_hex(aes_bytes).decode().upper()

def get_guid_pid():
    javascript = """
    function get_grid(){
        var t = (new Date).getTime().toString(36);
        var r = Math.random().toString(36).replace(/^0./, "");

        return "".concat(t, "_").concat(r);
    }
    """
    JS = execjs.compile(javascript)
    return JS.call("get_grid")

def get_vid(url):
    return re.findall(r"&vid=(.+?)&", url)[0]

def get_qn(Gn):
    javascript = """
        function Qn(Vn){
        var Yn = 0;
        for (var Ur = 0; Ur < Vn["length"]; Ur++) {
            Qn = Vn["charCodeAt"](Ur);
            Yn = (Yn << -5516 + 1360 + 9081 - 4920) - Yn + Qn,
            Yn &= Yn;}
        return Yn;
    }
    """
    JS = execjs.compile(javascript)
    return JS.call("Qn", Gn)

def get_vurl(guid, vid, cKey, pid):
    payload = {
        "callback": "jsonp3",
        "guid": guid,
        "platform": "4330701",
        "vid": vid,
        "defn": "auto",
        'charge': '0',
        'defaultfmt': 'auto',
        'otype': 'json',
        'defnpayver': '1',
        'appVer': '1.25.0',
        'sphttps': '1',
        'sphls': '1',
        'spwm': '4',
        'dtype': '3',
        'defsrc': '1',
        'encryptVer': '8.1',
        'sdtfrom': '4330701',
        "cKey": cKey,
        'panoramic': 'false',
        'flowid': pid,
    }
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Referer': 'https://w.yangshipin.cn/',
        'Sec-Fetch-Dest': 'script',
        'Sec-Fetch-Mode': 'no-cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    resp = requests.get(url="https://playvv.yangshipin.cn/playvinfo", params=payload, headers=headers, cookies={
        "guid": guid,
    }).text
    resp_json = json.loads(resp[7: -1])
    vkey = resp_json["vl"]["vi"][0]["fvkey"]
    fn = resp_json["vl"]["vi"][0]["fn"]
    return f"https://mp4playcnc-cdn.ysp.cctv.cn/{fn}?sdtfrom=4330701&guid={guid}&vkey={vkey}&platform=2"

def play(base_url, guid, vid, pid, vurl):
    post_url = "https://btrace.yangshipin.cn/kvcollect"
    headers = {
        'authority': 'btrace.yangshipin.cn',
        'accept': '*/*',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'no-cache',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://w.yangshipin.cn',
        'pragma': 'no-cache',
        'referer': 'https://w.yangshipin.cn/',
        'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    }

    params = {
        'BossId': '2865',
    }

    data = json.dumps({
        "ctime": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "ua": "mozilla/5.0 (windows nt 10.0; win64; x64) applewebkit/537.36 (khtml, like gecko) chrome/108.0.0.0 safari/537.36",
        "hh_ua": "mozilla/5.0 (windows nt 10.0; win64; x64) applewebkit/537.36 (khtml, like gecko) chrome/108.0.0.0 safari/537.36",
        "platform": "4330701",
        'guid': guid,
        'Pwd': '1698957057',
        'version': 'wc-1.25.0',
        'url': base_url,
        'hh_ref': base_url,
        'vid': vid,
        'isfocustab': '1',
        'isvisible': '1',
        'idx': '0',
        'val': '449',
        'pid': pid,
        'bi': '0',
        'bt': '0',
        'defn': 'hd',
        'vurl': vurl,
        'step': '6',
        'val1': '1',
        'val2': '1',
        'fact1': "",
        'fact2': "",
        'fact3': "",
        'fact4': "",
        'fact5': "",
    })
    response = requests.post(post_url, params=params, headers=headers, data=data)
    print(response.status_code)
    # print(data)

def task(url):
    try:
        guid = get_guid_pid()
        pid = get_guid_pid()
        vid = get_vid(url)
        
        data_string = "|".join(["", vid, str(int(time.time())), "mg3c3b04ba", "1.25.0", guid, "4330701", "https://w.yangshipin.cn/|mozilla/5.0 (windows nt |https://m.yangshipin.cn/|Mozilla|Netscape|Win32|"])
        Qn = get_qn(data_string)
        Wn = f"|{Qn}{data_string}"
        cKey = "--01" + aes_encrypt(Wn)
        
        vurl = get_vurl(guid, vid, cKey, pid)
        play(url, guid, vid, pid, vurl)
    except Exception as e:
        print(e)

def main():
    url = "https://w.yangshipin.cn/video?type=0&vid=a000033lo5y&channel=m_h5&channel_origin=m_h5"
    # task(url)
    start = time.time()

    pool = ThreadPoolExecutor(30)
    for _ in range(300):
        pool.submit(task, url)
    pool.shutdown()

    end = time.time()
    print("执行完成，耗时", end - start)


if __name__ == "__main__":
    main()