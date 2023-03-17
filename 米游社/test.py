import requests
import uuid

headers = {
    'host': 'bbs-api.miyoushe.com',
    'ds': '1671720802,9fg989,4c8c6c559777bca4adc11552099a6061',
    'x-rpc-client_type': '2',
    'x-rpc-app_version': '2.42.1',
    'x-rpc-sys_version': '12',
    'x-rpc-channel': 'miyousheluodiye_PC',
    'x-rpc-device_id': str(uuid.uuid4()),
    'x-rpc-device_name': 'Vivo VIVO X20 Plus',
    'x-rpc-device_model': 'VIVO X20 Plus',
    'referer': 'https://app.mihoyo.com',
    # 'accept-encoding': 'gzip',
    'user-agent': 'okhttp/4.9.3',
}

params = {
    'forum_id': '4',
    'is_hot': 'false',
    'is_good': 'false',
    'sort_type': '1',
    'last_id': '',
    'page_size': '20',
}

response = requests.get('https://bbs-api.miyoushe.com/post/api/getForumPostList', params=params, headers=headers, verify=False)

with open('0.dat', 'wb') as f:
    f.write(response.content)