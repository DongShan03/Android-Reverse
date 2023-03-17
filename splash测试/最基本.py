import requests

resp = requests.get(url="http://192.168.1.5:8050/render.html", params={
    "url": "https://endata.com.cn/BoxOffice/Schedule/Index",
    "wait": 3,
})

print(resp.text)
