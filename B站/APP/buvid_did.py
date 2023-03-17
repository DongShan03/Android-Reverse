import random
import string
import base64
import hashlib
import datetime

def gen_random_mac(sep=":"):
    mac_part = []
    for _ in range(6):
        part = "".join(random.sample("0123456789ABCDEF", 2))
        mac_part.append(part)
    mac = sep.join(mac_part)
    return mac

def gen_random_sn():
    return "".join(random.sample("123456789" + string.ascii_lowercase, 10))

def get_session_id():
    return "".join([hex(random.randint(0, 255))[2:] for _ in range(4)])

def base64_self_encode(input):
    data_bytes = bytearray(input.encode('utf8'))
    data_bytes[0] = data_bytes[0] ^ (len(data_bytes) & 0xFF)
    for i in range(1, len(data_bytes)):
        data_bytes[i] = (data_bytes[i - 1] ^ data_bytes[i]) & 0xFF
    res = base64.encodebytes(bytes(data_bytes))
    return res.strip().strip(b"==").decode("utf8")

def get_buvid(mac):
    md5 = hashlib.md5()
    md5.update(mac.encode("utf8"))
    d2 = md5.hexdigest()
    e_d2 = f"{d2[2]}{d2[12]}{d2[22]}"
    return ("XY" + e_d2 + d2).upper()

mac = gen_random_mac("")
sn = gen_random_sn()

did = base64_self_encode(f"{mac}|||{sn}")
buvid = get_buvid(mac)

# print(buvid)

# print(did)

def gen_local_v1(buvid, phone_model, phone_band):
    def misc_helper_kt(data_bytes):
        data_list = []
        v7 = len(data_bytes)
        print(v7)
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
    arg3 = misc_helper_kt([random.randint(0, 255) for _ in range(8)])

    return f"{arg1}{arg2}{arg3}"

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

str2 = gen_local_v1(buvid, "Mate 10 Pro", "")
fp_local = str2 + a_b(str2)

print(fp_local)

#com.bilibili.lib.biliid.internal.fingerprint.Fingerprint

#(MiscHelperKt.a(f(buvidLegacy, data)) + h() + MiscHelperKt.a(g())) + b(str);
#f(buvidLegacy, data) = Md5(buvid + 手机型号 + "")
#h() 时间戳  System.currentTimeMillis
#g() 随机八个字节

#MiscHelperKt.a ???
#f.Oe(asHex, "", null, null, 0, null, MiscHelperKt$asHex$1.INSTANCE, 30, null)


# public static /* synthetic */ String Oe(byte[] bArr, CharSequence charSequence, CharSequence charSequence2, CharSequence charSequence3, int i2, CharSequence charSequence4, kotlin.jvm.c.l lVar, int i3, Object obj) {
#     CharSequence charSequence5 = "";
#     CharSequence charSequence6 = "";

#     int i4 = -1;

#     charSequence4 = "...";

#     CharSequence charSequence7 = "...";

#     return Fe(bArr, "", "", "", -1, "...", lVar);
# }
