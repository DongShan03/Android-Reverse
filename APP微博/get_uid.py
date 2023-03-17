import requests, random
import time, uuid


def gen_random_hex(i, sep=""):

    mac_part = []
    for _ in range(i):
        part = "".join(random.sample("0123456789ABCDEF", 2))
        mac_part.append(part)
    mac = sep.join(mac_part)
    return mac


from_unknown = gen_random_hex(10)[:10]
android_id = gen_random_hex(16).lower()
device = "M2007J22C_9_weibo_10.12.1_android"
device_all = "Xiaomi-M2007J22C__weibo__10.12.1__android__android9"
x_sessionid = str(uuid.uuid4())

headers = {
    'host': 'api.weibo.cn',
    'user-agent': device,
    'x-sessionid': x_sessionid,
    'content-type': 'application/x-www-form-urlencoded',
}

params = {
    'networktype': 'wifi',
    'launchid': '10000365--x',
    'moduleID': '700',
    'wb_version': '4764',
    'c': 'android',
    'ft': '0',
    'ua': device_all,
    'wm': '5311_4002',
    'v_f': '2',
    'v_p': '86',
    'from': from_unknown,
    'lang': 'zh_CN',
    'skin': 'default',
    'oldwm': '5311_4002',
    'sflag': '1',
    'android_id': android_id,
    'ul_ctime': str(int(time.time())),
    'cum': '1040542B',
}

data = 'device_name=Xiaomi-M2007J22C&appkey=7501641714&checktoken=aafac66844f03cb06013d76349d71939&preload_ab=1&ds=00000000&did=49113ca554fa9fcb9282e9b033984ed1&mfp=01IU2MB8Gp%%2BtPU3ZT3fA0nrWzpXmJynr3HJKmUge1EX%%2FvnmbS6y6mnnwzj8CYrVe%%2FSk3aNjhzKRmy2G4fT0PEliO0cI4ZcnMk6HE%%2F4ogLIoWYdFiazvNOj9uYmlrPAo8ClFG%%2BsB6PDkqaiCpmE9AR7AtTLLL3yLoOrUJ1Lzbkjoe48%%2FdEIzH881tok6Z%%2BSIq2HvmAv%%2Fq4AGDEiH58T7jRGCVljpjyDwGuoX39sI55ABgKNIIKD1KfA1QEmEw44aUVbh3PX6gQi896Fhask4qxpdlToAdgIRmn3vCw9qI9yJgQdSgObkLO97340SVyVpTr1b%%2BArQkZg7RzmcoknIuX1frEmK5Yrk7ViddikR3fnCB6g3ylNrhdcuqsOZyJ%%2FnayohYlrX1TOvZfcSO7huBhDNfuUGt2fKmFULtanl7Kj8GdirHL70K%%2Fp%%2B4ZrT64CigxSaK6PiZRZpi%%2B%%2FL%%2Bxf51umcU66OoZMVW3AJewscDGA2KwNF0YJtIQ97058b2SNKpnO&imei=&device_id=49113ca554fa9fcb9282e9b033984ed105545053&request_ab=1&key_hash=18da2bf10352443a00a5e046d9fca6bd&android_id=15e7fbb18a3e8ef0&permission_status=00&packagename=com.sina.weibo'

response = requests.post('https://api.weibo.cn/2/guest/login', params=params, headers=headers, data=data)
