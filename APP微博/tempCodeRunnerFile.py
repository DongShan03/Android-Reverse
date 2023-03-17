
# x_sessionid = str(uuid.uuid4())
# # device = random.choice(['M2007J22C_9_weibo_10.12.1_android', "vivo-VIVO X20 Plus__weibo__10.12.1__android__android12"])
# device = "M2007J22C_9_weibo_10.12.1_android"
# device_all = "Xiaomi-M2007J22C__weibo__10.12.1__android__android9"

# headers = {
#     'host': 'api.weibo.cn',
#     'user-agent': device,
#     'x-log-uid': '2000713933834',
#     'x-sessionid': x_sessionid, # uuid4()???
#     'x-validator': 'PCf7Sk7u/JJ/iH0euQeI0UFKsb3L4Lxao14F7Bggkgc=',
# }

# """
# 'orifid': '231619%%24%%24100303type%%3D1%%26q%%3D%%E6%%AD%%A6%%E6%%B1%%89%%E5%%B8%%82%%26t%%3D0', 
# 'checktoken': '8f1642a16236665af420020a3052ca25', 
# 'aid': '01A2Wnnb805zx5rdXFwv7yLLP-UcxOSVgAL6fVx4gKnkcQXoQ.', 
# 'did': '49113ca554fa9fcb9282e9b033984ed105545053', 
# 'fid': '100808ad9efa2f14d42f7d14ef876725909e27_-_lbs', 
# 'uid': '2000713933834', 
# 'from': '10AC195010',    MAC地址
# 'gsid': '_2AkMU-6zEf8NhqwFRmPgSzWjrb45_yQzEieKip10fJRM3HRl-wT9jqndYtRV6XNyh2E1K7STxtCnUwactg1J0sl3GR4mk', 
# 'lfid': '100303type%%3D1%%26q%%3D%%E6%%AD%%A6%%E6%%B1%%89%%E5%%B8%%82%%26t%%3D0', 
# 'containerid': '100808ad9efa2f14d42f7d14ef876725909e27_-_lbs', 
# 'android_id': '15e7fbb18a3e8ef0', 
# 'ul_ctime': str(int(time.time() * 1000)), 
# 'cum': '0A7E432B'
# """
# params = {
#     'st_bottom_bar_new_style_enable': '1', 
#     'networktype': 'wifi', 
#     'extparam': 'frompoi', 
#     'page_reform_enable': '1', 
#     'launchid': '10000365--x', 
#     'page_interrupt_enable': '1', 
#     'orifid': '231619%%24%%24100303type%%3D1%%26q%%3D%%E6%%AD%%A6%%E6%%B1%%89%%E5%%B8%%82%%26t%%3D0', 
#     'uicode': '10000011', 
#     'moduleID': '708', 
#     'checktoken': '8f1642a16236665af420020a3052ca25', 
#     'featurecode': '10000085', 
#     'just_followed': 'false', 
#     'wb_version': '4764', 
#     'lcardid': 'frompoi', 
#     'c': 'android', 
#     's': '33333333',  #s = "00000000"
#     'ft': '0', 
#     'ua': 'Xiaomi-M2007J22C__weibo__10.12.1__android__android9',   # "vivo-VIVO X20 Plus__weibo__10.12.1__android__android12"
#     'wm': '5311_4002', 
#     'aid': '01A2Wnnb805zx5rdXFwv7yLLP-UcxOSVgAL6fVx4gKnkcQXoQ.', 
#     'did': '49113ca554fa9fcb9282e9b033984ed105545053', 
#     'fid': '100808ad9efa2f14d42f7d14ef876725909e27_-_lbs', 
#     'uid': '2000713933834', 
#     'v_f': '2', 
#     'v_p': '86', 
#     'from': '10AC195010', 
#     'gsid': '_2AkMU-6zEf8NhqwFRmPgSzWjrb45_yQzEieKip10fJRM3HRl-wT9jqndYtRV6XNyh2E1K7STxtCnUwactg1J0sl3GR4mk', 
#     'imsi': '', 
#     'lang': 'zh_CN', 
#     'lfid': '100303type%%3D1%%26q%%3D%%E6%%AD%%A6%%E6%%B1%%89%%E5%%B8%%82%%26t%%3D0', 
#     'page': '1', 
#     'skin': 'default', 
#     'count': '20', 
#     'oldwm': '5311_4002', 
#     'sflag': '1', 
#     'oriuicode': '10000512_10000003', 
#     'containerid': '100808ad9efa2f14d42f7d14ef876725909e27_-_lbs', 
#     'ignore_inturrpted_error': 'true', 
#     'no_location_permission': '1', 
#     'luicode': '10000003', 
#     'android_id': '15e7fbb18a3e8ef0', 
#     'header_skin_enable': '0', 
#     'ul_ctime': str(int(time.time() * 1000)),   #str(int(time.time() * 1000))
#     'cum': '0A7E432B'
# }

# {'s': '00000000', 'did': '0f607264fc6318a92b9e13c65db7cd3c4d8b06c0', 'fid': '100808ad9efa2f14d42f7d14ef876725909e27_-_lbs', 'uid': '2009189104813', 'v_f': '2', 'v_p': '86', 'from': '10AC195010', 'gsid': '_2AkMU-6Zcf8NhqwFRmPEUxGLjbIl_ywvEieKip1eHJRM3HRl-wT9jqmkctRV6XNyh2Gfhaexm6okCksCz01rx_3F5H0ls', 'lang': 'zh_CN', 'lfid': '100303type%%3D1%%26q%%3D%%E6%%AD%%A6%%E6%%B1%%89%%E5%%B8%%82%%26t%%3D2', 'page': '1', 'skin': 'default', 'count': '20', 'oldwm': '5311_4002', 'sflag': '1', 'oriuicode': '10000512_10000003_10000003', 'containerid': '100808ad9efa2f14d42f7d14ef876725909e27_-_lbs', 'ignore_inturrpted_error': 'true', 'no_location_permission': '1', 'luicode': '10000003', 'android_id': '78f2f98e9a85cd6b', 'header_skin_enable': '0', 'ul_ctime': '1671899588911', 'cum': 'F90E6256'}

# response = requests.get(
#     'https://api.weibo.cn/2/guest/page',
#     headers=headers,
#     params=params
# )



# headers = {
#     'host': 'api.weibo.cn',
#     'user-agent': device,
#     'x-sessionid': x_sessionid,
#     'content-type': 'application/x-www-form-urlencoded',
# }

# params = {
#     'networktype': 'wifi',
#     'launchid': '10000365--x',
#     'moduleID': '700',
#     'wb_version': '4764',
#     'c': 'android',
#     'ft': '0',
#     'ua': device_all,
#     'wm': '5311_4002',
#     'v_f': '2',
#     'v_p': '86',
#     'from': '10AC195010',
#     'lang': 'zh_CN',
#     'skin': 'default',
#     'oldwm': '5311_4002',
#     'sflag': '1',
#     'android_id': '15e7fbb18a3e8ef0',
#     'ul_ctime': '1671901239883',
#     'cum': '1040542B',
# }

# data = 'device_name=Xiaomi-M2007J22C&appkey=7501641714&checktoken=aafac66844f03cb06013d76349d71939&preload_ab=1&ds=00000000&did=49113ca554fa9fcb9282e9b033984ed1&mfp=01IU2MB8Gp%%2BtPU3ZT3fA0nrWzpXmJynr3HJKmUge1EX%%2FvnmbS6y6mnnwzj8CYrVe%%2FSk3aNjhzKRmy2G4fT0PEliO0cI4ZcnMk6HE%%2F4ogLIoWYdFiazvNOj9uYmlrPAo8ClFG%%2BsB6PDkqaiCpmE9AR7AtTLLL3yLoOrUJ1Lzbkjoe48%%2FdEIzH881tok6Z%%2BSIq2HvmAv%%2Fq4AGDEiH58T7jRGCVljpjyDwGuoX39sI55ABgKNIIKD1KfA1QEmEw44aUVbh3PX6gQi896Fhask4qxpdlToAdgIRmn3vCw9qI9yJgQdSgObkLO97340SVyVpTr1b%%2BArQkZg7RzmcoknIuX1frEmK5Yrk7ViddikR3fnCB6g3ylNrhdcuqsOZyJ%%2FnayohYlrX1TOvZfcSO7huBhDNfuUGt2fKmFULtanl7Kj8GdirHL70K%%2Fp%%2B4ZrT64CigxSaK6PiZRZpi%%2B%%2FL%%2Bxf51umcU66OoZMVW3AJewscDGA2KwNF0YJtIQ97058b2SNKpnO&imei=&device_id=49113ca554fa9fcb9282e9b033984ed105545053&request_ab=1&key_hash=18da2bf10352443a00a5e046d9fca6bd&android_id=15e7fbb18a3e8ef0&permission_status=00&packagename=com.sina.weibo'

# response = requests.post('https://api.weibo.cn/2/guest/login', params=params, headers=headers, data=data, verify=False)