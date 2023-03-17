import time
import requests, datetime
import re, random
from urllib.parse import quote, urlsplit
import hashlib, base64
import json, string
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from concurrent.futures import ThreadPoolExecutor




class BiliBili(object):

    def __init__(self, proxies=None):

        self.session = requests.Session()
        self.session.proxies = proxies
        # self.session.verify = False
        self.mac = self.gen_random_mac().upper()
        self.device_id = self.gen_device_id(self.mac)
        self.buvid = self.gen_buvid(self.mac)
        self.session_id = self.get_session_id()
        self.heart_beat_session_id = self.gen_heart_beat_session_id()

        self.brand = "HUAWEI"
        self.build_model = "Mate 10 Pro"

        self.fp_local = self.gen_fp_local(self.buvid, self.build_model, "")
        self.fp_remote = self.gen_fp_local(self.buvid, self.build_model, "")

        self.app_first_runtime = str(int(time.time() - random.randint(100, 6000)))
        self.ts = str(int(time.time() - 10))

    def get_video_id_info(self, url):

        def get_video_info(session, aid):
            url = f"https://api.bilibili.com/x/web-interface/view?aid={aid}"
            resp = session.get(url=url, headers=headers).json()
            view_count = resp["data"]["stat"]["view"]
            duration = resp["data"]["duration"]
            return view_count, duration
    
        headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
        }
        # while True:
        resp = self.session.get(url=url, headers=headers)
        data_list = re.findall(r"window.__INITIAL_STATE__=(.+);\(function", resp.text)
        data_dict = json.loads(data_list[0])
        view_count, duration = get_video_info(self.session, data_dict["aid"])

        aid = data_dict["aid"]
        cid = data_dict["videoData"]["cid"]
        bvid = data_dict["bvid"]
        return aid, cid, bvid, view_count, duration

    def gen_random_mac(self, sep=":"):

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
        return self.gen_random_mac(sep)

    def get_session_id(self):
        return "".join([hex(random.randint(0, 255))[2:] for _ in range(4)])

    def gen_device_id(self, mac):

        def gen_random_sn():
            return "".join(random.sample("123456789" + string.ascii_lowercase, 10))

        def base64_self_encode(input):
            data_bytes = bytearray(input.encode('utf8'))
            data_bytes[0] = data_bytes[0] ^ (len(data_bytes) &  0xFF)
            for i in range(1, len(data_bytes)):
                data_bytes[i] = (data_bytes[i - 1] ^ data_bytes[i]) &  0xFF
            res = base64.encodebytes(bytes(data_bytes))
            return res.strip().strip(b"==").decode("utf8")
        mac_string = mac
        mac_str = re.sub("[^0-9A-Fa_f]", "", mac_string)
        mac_str = mac_str.lower()

        sn = gen_random_sn()

        total_string = f"{mac_str}|||{sn}"
        return base64_self_encode(total_string)
        
    def gen_buvid(self, mac):
        md5 = hashlib.md5()
        md5.update(mac.encode("utf8"))
        d2 = md5.hexdigest()
        e_d2 = f"{d2[2]}{d2[12]}{d2[22]}"
        return ("XY" + e_d2 + d2).upper()
    
    def gen_fp_local(self, buvid, phone_model, phone_band):
        def a_b(arg):
            g = 0
            h = 60
            i2 = 2
            v5 = 0
            while True:
                string = arg[g: g+2]
                v5 += int(string, base=16)
                if g != h:
                    g += i2
                    continue
                break
            data = "%02x" % (v5 % 0x100, )
            return data

        def misc_helper_kt(data_bytes):
            data_list = []
            v7 = len(data_bytes)
            v0 = 0
            while v0 < v7:
                v2 = data_bytes[v0]
                data_list.append("%02x" % v2)
                v0 += 1
            return "".join(data_list)
        
        data_string = f"{buvid}{phone_model}{phone_band}"
        hash_object = hashlib.md5()
        hash_object.update(data_string.encode("utf-8"))
        data = hash_object.digest()

        arg1 = misc_helper_kt(data)
        arg2 = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        arg3 = misc_helper_kt([random.randint(1, 255) for _ in range(8)])
        str1 = f"{arg1}{arg2}{arg3}"
        str2 = a_b(str1)
        return str1 + str2

    def gen_heart_beat_session_id(self):
        timestamp = str(int(time.time()))
        random_num = str(random.randint(0, 999999))

        input = timestamp + random_num
        sha1 = hashlib.sha1()
        sha1.update(input.encode("utf-8"))

        return sha1.hexdigest()

    def get_param_s_sign(self, data):
        ordered_string = "&".join(["{}={}".format(key, value) for key, value in sorted(data.items())])
        encrypt_string = ordered_string + "560c52ccd288fed045859ed18bffd973"
        obj = hashlib.md5(encrypt_string.encode("utf-8"))
        sign = obj.hexdigest()
        return ordered_string + "&sign=" + sign

    def get_param_so_sign(self, data):
        ordered_string = "&".join(["{}={}".format(key, value) for key, value in sorted(data.items())])
        encrypt_string = ordered_string + "60698ba2f68e01ce44738920a0ffe768"
        obj = hashlib.md5(encrypt_string.encode("utf-8"))
        sign = obj.hexdigest()
        return ordered_string + "&sign=" + sign

    def x_report_click_android2(self, info_url):
        self.url = info_url
        self.aid, self.cid, self.bvid, self.view_count, self.duration = self.get_video_id_info(self.url) 
        
        def aes_encrypt(data):
            key_str = "fd6b639dbcff0c2a1b03b389ec763c4b"
            iv_str = "77b07a672d57d64c"
            aes = AES.new(
                key=key_str.encode("utf-8"),
                mode=AES.MODE_CBC,
                iv=iv_str.encode("utf-8"),
            )
            raw = pad(data.encode("utf-8"), 16)
            aes_bytes = aes.encrypt(raw)
            return aes_bytes
        
        def sha_256_encrypt(data_string):
            salt = "9cafa6466a028bfb"
            sha = hashlib.sha256()
            sha.update(data_string.encode("utf-8"))
            sha.update(salt.encode("utf-8"))
            return sha.hexdigest()
        
        ctime = int(time.time())
        info = {
            "aid": self.aid,
            "cid": self.cid,
            "part": 1,
            "mid": 0,
            "lv": 0,
            "ftime": ctime - random.randint(100, 1000),
            "stime": ctime,
            "did": self.device_id,
            "type": 3,
            "sub_type": 0,
            "sid": "0",
            "epid": "",
            "auto_play": 0,
            "build": 6240300,
            "mobi_app": "android",
            "spmid": "main.ugc-video-detail.0.0",
            "from_spmid": "search.search-result.0.0",
        }
        data = ", ".join(["{}={}".format(key, info[key]) for key in sorted(info.keys())])
        sign = sha_256_encrypt(data).lower()
        data = f"{data}, sign={sign}"
        aes_string = aes_encrypt(data)

        resp = self.session.post(
            url = "https://api.bilibili.com/x/report/click/android2",
            headers = {
                'host':'api.bilibili.com',
                'buvid':self.buvid,
                'device-id':self.device_id,
                'fp_local':self.fp_local,
                'fp_remote':self.fp_remote,
                'session_id': self.session_id,
                'env':'prod',
                'app-key':'android',
                'user-agent':'Mozilla/5.0 BiliDroid/6.24.0 (bbcallen@gmail.com) os/android model/M2007J22C mobi_app/android build/6240300 channel/xiaomi innerVer/6240300 osVer/9 network/2',
                'content-type':'application/octet-stream',
                'content-length':'336',
                'accept-encoding':'gzip'
            },
            data = aes_string,
            timeout = 10,
        )
        return resp.text

    def x_report_heartbeat_start(self):
        self.start_ts = ts = int(time.time())
        headers = {
            'host': 'api.bilibili.com',
            'buvid': self.buvid,
            'device-id': self.device_id,
            'fp_local': self.fp_local,
            'fp_remote': self.fp_remote,
            'session_id': self.session_id,
            'env': 'prod',
            'app-key': 'android',
            'user-agent': 'Mozilla/5.0 BiliDroid/6.24.0 (bbcallen@gmail.com) os/android model/M2007J22C mobi_app/android build/6240300 channel/xiaomi innerVer/6240300 osVer/9 network/2',
            'content-type': 'application/x-www-form-urlencoded; charset=utf-8',
        }
        data = {
            'actual_played_time':"0", 
            "aid": self.aid, 
            "appkey":"1d8b6e7d45233436", 
            "auto_play":'0', 
            "build":"6240300", 
            "c_locale":"zh_CN", 
            "channel":"xiaomi", 
            "cid": self.cid, 
            "epid":'0', 
            "epid_status":"", 
            "from":'7', 
            "from_spmid":"tm.recommend.0.0", 
            "last_play_progress_time":'0', 
            "list_play_time":'0', 
            "max_play_progress_time":'0', 
            "mid":'0', 
            "miniplayer_play_time":'0', 
            "mobi_app":"android", 
            "network_type":'1', 
            "paused_time":'0', 
            "platform":"android", 
            "play_status":'0', 
            "play_type":'1', 
            "played_time":'0', 
            "quality":'32', 
            "s_locale":'zh_CN', 
            "session":self.heart_beat_session_id, 
            "sid": '0', 
            "spmid":'main.ugc-video-detail.0.0', 
            "start_ts": "0", 
            "statistics": quote(json.dumps({"appId": 1, "platform": 3, "version": "6.24.0", "abtest": ""}, separators=(",", ":"))), 
            "sub_type":'0', 
            "total_time":'0', 
            "ts": ts, 
            "type":'3', 
            "user_status":'0', 
            "video_duration": self.duration,
        }

        total_body_string = self.get_param_s_sign(data)
        resp = self.session.post(
            url="https://api.bilibili.com/x/report/heartbeat/mobile",
            headers=headers,
            data=total_body_string.encode("utf-8"),
            timeout=10,
        )
        print(resp.text)
        self.start_ts = resp.json()["data"]["ts"]
        resp.close()

    def x_report_heartbeat_end(self):
        headers = {
            'host': 'api.bilibili.com',
            'buvid': self.buvid,
            'device-id': self.device_id,
            'fp_local': self.fp_remote,
            'fp_remote': self.fp_remote,
            'session_id': self.session_id,
            'env': 'prod',
            'app-key': 'android',
            'user-agent': 'Mozilla/5.0 BiliDroid/6.24.0 (bbcallen@gmail.com) os/android model/M2007J22C mobi_app/android build/6240300 channel/xiaomi innerVer/6240300 osVer/9 network/2',
            'content-type': 'application/x-www-form-urlencoded; charset=utf-8',
        }
        
        current_ts = int(time.time())
        data = {
            'actual_played_time': self.duration,
            'aid': self.aid,
            'appkey': '1d8b6e7d45233436',
            'auto_play': '0',
            'build': '6240300',
            'c_locale': 'zh_CN',
            'channel': 'xiaomi',
            'cid': self.cid,
            'epid': '0',
            'epid_status': '',
            'from': '7',
            'from_spmid': 'tm.recommend.0.0',
            'last_play_progress_time': self.duration,
            'list_play_time': '0',
            'max_play_progress_time': self.duration,
            'mid': '0', 
            'miniplayer_play_time': '0',
            'mobi_app': 'android',
            'network_type': '1',
            'paused_time': current_ts - self.start_ts - self.duration,
            'platform': 'android',
            'play_status': '0',
            'play_type': '1',
            'played_time': self.duration,
            'quality': '32',
            's_locale': 'zh_CN',
            'session': self.heart_beat_session_id,
            'sid': '0',
            'spmid': 'main.ugc-video-detail.0.0',
            'start_ts': self.start_ts,
            'statistics': quote(json.dumps({"appId": 1, "platform": 3, "version": "6.24.0", "abtest": ""}, separators=(",", ":"))),
            'sub_type': '0',
            'total_time': current_ts - self.start_ts,
            'ts': current_ts,
            'type': '3',
            'user_status': '0',
            'video_duration': self.duration,
        }
        total_body_string = self.get_param_s_sign(data)

        resp = self.session.post(
            'https://api.bilibili.com/x/report/heartbeat/mobile', 
            headers=headers,
            data=total_body_string.encode("utf-8"),
            timeout=10
        )
        print(resp.text)
        resp.close()

    def x_report_heartbeat_Interruptions(self, times):
        current_ts = int(time.time())
        actual_played_time = int(self.duration * times)
        total_time = current_ts - self.start_ts
        pause_time = total_time - actual_played_time
        headers = {
            'host': 'api.bilibili.com',
            'buvid': self.buvid,
            'device-id': self.device_id,
            'fp_local': self.fp_local,
            'fp_remote': self.fp_remote,
            'session_id': self.session_id,
            'env': 'prod',
            'app-key': 'android',
            'user-agent': 'Mozilla/5.0 BiliDroid/6.24.0 (bbcallen@gmail.com) os/android model/M2007J22C mobi_app/android build/6240300 channel/xiaomi innerVer/6240300 osVer/9 network/2',
            'content-type': 'application/x-www-form-urlencoded; charset=utf-8',
        }

        data = {
            'actual_played_time': actual_played_time, 
            'aid': self.aid, 
            'appkey': '1d8b6e7d45233436', 
            'auto_play': '0', 
            'build': '6240300', 
            'c_locale': 'zh_CN', 
            'channel': 'xiaomi', 
            'cid': self.cid, 
            'epid': '0', 
            'epid_status': '', 
            'from': '7', 
            'from_spmid': 'tm.recommend.0.0', 
            'last_play_progress_time': '0', 
            'list_play_time': '0', 
            'max_play_progress_time': "0", 
            'mid': '0', 
            'miniplayer_play_time': '0', 
            'mobi_app': 'android', 
            'network_type': '1', 
            'paused_time': pause_time, 
            'platform': 'android', 
            'play_status': '0', 
            'play_type': '1', 
            'played_time': actual_played_time, 
            'quality': '32', 
            's_locale': 'zh_CN', 
            'session': self.heart_beat_session_id, 
            'sid': '0', 
            'spmid': 'main.ugc-video-detail.0.0', 
            'start_ts': '0', 
            'statistics': quote(json.dumps({"appId": 1, "platform": 3, "version": "6.24.0", "abtest": ""}, separators=(",", ":"))), 
            'sub_type': '0', 
            'total_time': total_time, 
            'ts': current_ts, 
            'type': '3', 
            'user_status': '0', 
            'video_duration': self.duration,
        }
        total_body_string = self.get_param_s_sign(data)
        resp = self.session.post(
            url='https://api.bilibili.com/x/report/heartbeat/mobile', 
            headers=headers, 
            data=total_body_string.encode("utf-8"), 
            timeout=10,
        )
        print(resp.text)
        resp.close()

    def Finish(self, url):
        self.x_report_click_android2(url)
        self.x_report_heartbeat_start()
        time.sleep(self.duration + random.randint(5, 15))
        self.x_report_heartbeat_end()
        self.session.close()

    def Interruptions(self, url):
        times = random.random() / 2 + 0.5
        self.x_report_click_android2(url)
        self.x_report_heartbeat_start()
        time.sleep(self.duration * times + random.randint(5, 10))
        self.x_report_heartbeat_Interruptions(times)
        self.session.close()

    def sms_send(self, address, tel):
        ts = int(time.time())
        headers = {
            'host': 'passport.bilibili.com',
            'buvid': self.buvid,
            'env': 'prod',
            'app-key': 'android',
            'user-agent': 'Mozilla/5.0 BiliDroid/6.24.0 (bbcallen@gmail.com) os/android model/M2007J22C mobi_app/android build/6240300 channel/xiaomi innerVer/6240300 osVer/9 network/2',
            'content-type': 'application/x-www-form-urlencoded; charset=utf-8',
        }

        data = {
            'appkey': 'bca7e84c2d947ac6',
            'build': '6240300',
            'c_locale': 'zh_CN',
            'channel': 'xiaomi',
            'cid': str(address),
            'mobi_app': 'android',
            'platform': 'android',
            's_locale': 'zh_CN',
            'tel': str(tel),
            'ts': ts,
        }
        total_body_string = self.get_param_so_sign(data)

        resp = self.session.post(
            'https://passport.bilibili.com/x/passport-login/sms/send', 
            headers=headers, 
            data=total_body_string.encode('utf-8'),
            timeout=10,
        )
        data_dict = resp.json()
        if data_dict.get("code") == 86200:
            print(data_dict["message"])
            return "操作频繁"
        
        recaptcha_url = data_dict["data"]["recaptcha_url"]
        if not recaptcha_url:
            return "False"

        v1 = urlsplit(recaptcha_url)
        data_dict = {item.split("=")[0]: item.split("=")[1] for item in v1.query.split("&")}
        return "滑动验证码"



def get_proxy_dict():

    resp = requests.post("https://proxy.qg.net/allocate?Pool=1&Key=2A8DC741")
    print(resp.json())
    proxyAddr = resp.json()["Data"][0]["host"]
    authKey = "2A8DC741"
    password = "C19BB50A522D"
    # 账密模式
    proxyUrl = "http://%(user)s:%(password)s@%(server)s" % {
        "user": authKey,
        "password": password,
        "server": proxyAddr,
    }
    proxies = {
        "http": proxyUrl,
        "https": proxyUrl,
    }
    return proxies

def run(i):
    url = "https://www.bilibili.com/video/BV1B14y1P7L5/"
    if i % 2 == 0:
        try:
            proxies = get_proxy_dict()
            bili = BiliBili(proxies=proxies)
            bili.Finish(url)
            print("\n播放量:", bili.view_count)
        except Exception as e:
            print(e)
    else:
        try:
            proxies = get_proxy_dict()
            bili = BiliBili(proxies=proxies)
            bili.Interruptions(url)
            print("\n播放量:", bili.view_count)
        except Exception as e:
            print(e)

    # try:
    #     proxies = get_proxy_dict()
    #     bili = BiliBili(proxies=proxies)
    #     bili.Interruptions(url)
    # except Exception as e:
    #     print(e)

    # proxies = get_proxy_dict()
    # bili = BiliBili(proxies=proxies)
    # result = bili.sms_send(1, 7828099329)
    # print(result)
    # bili.sms_send(1, 7828099329)
    # print("\n播放量:", bili.view_count)
def task(i):
    run(i)



if __name__ == "__main__":
    # run()
    # print(get_proxy_dict())
    pool = ThreadPoolExecutor(max_workers = 1)
    for i in range(1):
        pool.submit(task, i)
        time.sleep(5)

