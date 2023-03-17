import requests
import base64
import execjs

headers = {
 'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
 'Accept-Language':'zh-CN,zh;q=0.9',
 }

data = {
    "city": "杭州",
    'endTime': "2022-12-15 21:00:00",
    'startTime': "2022-12-12 18:00:00",
    'type': "HOUR",
}

# result = execjs.compile(open("JS逆向开始/空气质量/请求加密.js", "r", encoding="utf-8").read(), cwd="D:\\nodejs\\node_modules").call("b", data)
result = execjs.compile(open("JS逆向开始/空气质量/请求加密.js", "r", encoding="utf-8").read()).call("b", data)
print(result)
# payload=base64.b64decode("aGVST2hLRXRMPWV5SmhjSEJKWkNJNklqZzNPVGxrTXpZMU9UZ3laRFUxTUdNeE9UVXhNREV5WTJOa01UVTFaVEEySWl3aWJXVjBhRzlrSWpvaVIwVlVSRVZVUVVsTUlpd2lkR2x0WlhOMFlXMXdJam94TmpjeE1UazJNalkxTVRneExDSmpiR2xsYm5SMGVYQmxJam9pVjBWQ0lpd2liMkpxWldOMElqcDdJbU5wZEhraU9pTG1uYTNsdDU0aUxDSjBlWEJsSWpvaVNFOVZVaUlzSW5OMFlYSjBWR2x0WlNJNklqSXdNakl0TVRJdE1UVWdNVGc2TURBNk1EQWlMQ0psYm1SVWFXMWxJam9pTWpBeU1pMHhNaTB4TmlBeU1Ub3dNRG93TUNKOUxDSnpaV055WlhRaU9pSXdZekk1TUdFeVpESmxOV000TkdSaFltTXdaakZoTXpVMFpUaGhNemxsTnlKOQ==")

# response0 = requests.request("POST", "https://www.aqistudy.cn/apinew/aqistudyapi.php", headers=headers, data=payload)

