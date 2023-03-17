# import hashlib
# import time
# import random
# import json

# timestamp = str(int(time.time()))
# random_num = str(random.randint(0, 999999))

# input = timestamp + random_num
# sha1 = hashlib.sha1()
# sha1.update(input.encode("utf-8"))

# print(sha1.hexdigest())

# # hashMap.put("statistics", new w0(1, 3, "6.24.0", ABTesting.b()).a());

# # public final String a() {
# #     String jSONObject = new JSONObject().put("appId", this.a).put("platform", this.b).put("version", this.f24146c).put("abtest", this.d).toString();
# #     x.h(jSONObject, "JSONObject()\n           …)\n            .toString()");
# #     return jSONObject;
# # }

# res = json.dumps({"appId": 1, "platform": 3, "version": "6.24.0", "abtest": ""}, separators=(",", ":"))
# print(res)
# {
# 	'code': 0,
# 	'message': '0',
# 	'ttl': 1,
# 	'data': {
# 		'bvid': 'BV1pG411F7b1',
# 		'aid': 432542087,
# 		'videos': 1,
# 		'tid': 201,
# 		'tname': '科学科普',
# 		'copyright': 1,
# 		'pic': 'http://i0.hdslb.com/bfs/archive/f37cc928a528e79909a08099808fd80866b54645.jpg',
# 		'title': '【深度缓冲】游戏开发者绝对不会教你的布料模拟',
# 		'pubdate': 1668151255,
# 		'ctime': 1668151255,
# 		'desc': "",
#          'desc_v2': [{'raw_text': '', 'type': 1, 'biz_id': 0}], 'state': 0, 'duration': 736, 'mission_id': 1080166, 'rights': {'bp': 0, 'elec': 0, 'download': 1, 'movie': 0, 'pay': 0, 'hd5': 0, 'no_reprint': 1, 'autoplay': 1, 'ugc_pay': 0, 'is_cooperation': 0, 'ugc_pay_preview': 0, 'no_background': 0, 'clean_mode': 0, 'is_stein_gate': 0, 'is_360': 0, 'no_share': 
# 			0,
# 		'arc_pay': 0,
# 		'free_watch': 0
# 	},
# 	'owner': {
# 		'mid': 385041959,
# 		'name': 'DepthBuffer',
# 		'face': 'https://i2.hdslb.com/bfs/face/fc468f21a8c918c3381d4a6c4e28be2d50624257.jpg'
# 	},
# 	'stat': {
# 		'aid': 432542087,
# 		'view': 54683,
# 		'danmaku': 50,
# 		'reply': 152,
# 		'favorite': 6909,
# 		'coin': 2208,
# 		'share': 283,
# 		'now_rank': 0,
# 		'his_rank': 0,
# 		'like': 3865,
# 		'dislike': 0,
# 		'evaluation': '',
# 		'argue_msg': ''
# 	},
# 	'dynamic': '这期视频制作了整整两个星期，从前期学习布料模拟算法到在自己的引擎内实现。已经后期的可视化制作。如果看的开心希望给个三连QAQ',
# 	'cid': 888082872,
# 	'dimension': {
# 		'width': 2560,
# 		'height': 1080,
# 		'rotate': 0
# 	},
# 	'premiere': None,
# 	'teenage_mode': 0,
# 	'is_chargeable_season': False,
# 	'is_story': False,
# 	'no_cache': False,
# 	'pages': [{
# 		'cid': 888082872,
# 		'page': 1,
# 		'from': 'vupload',
# 		'part': '【深度缓冲】游戏开发者绝对不会教你的布料模拟',
# 		'duration': 736,
# 		'vid': '',
# 		'weblink': '',
# 		'dimension': {
# 			'width': 2560,
# 			'height': 1080,
# 			'rotate': 0
# 		},
# 		'first_frame': 'http://i0.hdslb.com/bfs/storyff/n221111qn1s53sc7jka9z63bj83xuno1_firsti.jpg'
# 	}],
# 	'subtitle': {
# 		'allow_submit': False,
# 		'list': []
# 	},
# 	'is_season_display': False,
# 	'user_garb': {
# 		'url_image_ani_cut': ''
# 	},
# 	'honor_reply': {},
# 	'like_icon': '',
# 	'need_jump_bv': False
# }
# }

from urllib.parse import unquote_plus
data = "vivo-VIVO%%20X20%%20Plus__weibo__10.12.1__android__android12"

res = unquote_plus(data)

print(res)
# dic = {}
# for item in data.split("&"):
#     key = item.split("=")[0]
#     value = "".join(item.split("=")[1:])
#     dic.update({key: value})

# print(dic)

import time
import uuid
print(uuid.uuid4())
