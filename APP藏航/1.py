import requests
import base64

headers = {
    'Host':'cd.tibetairlines.com.cn:9100',
    'Proxy-Connection':'keep-alive',
    'Content-Length':'62',
    'Pragma':'no-cache',
    'Cache-Control':'no-cache',
    'Accept':'application/json, text/plain, */*',
    'Authorization':'Bearer undefined',
    'User-Agent':'android_system_webview',
    'Content-Type':'application/x-www-form-urlencoded;charset=UTF-8',
    'X-Requested-With':'hyz.pm.tibet.preparation.android.uat',
    'Accept-Encoding':'gzip, deflate',
    'Accept-Language':'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7'
}

payload = {
    'grant_type': 'password',
    'isLogin': 'true',
    'password': 'fuck',
    'username': 'alex,A',
}


resp = requests.post("http://cd.tibetairlines.com.cn:9100/login", headers=headers, data=payload)
print(resp.text)
