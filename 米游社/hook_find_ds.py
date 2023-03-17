import frida
import sys

# 连接手机设备
rdev = frida.get_remote_device()

# Hook手机上的那个APP（app的包名字）
# 注意事项：在运行这个代码之前，一定要先在手机上启动app
session = rdev.attach("米游社")  # 车智赢+

scr = """
function hook_RegisterNatives() {
    Java.perform(function() {

        var HkdfPrfParams = Java.use("com.google.crypto.tink.proto.HkdfPrfParams");

        HkdfPrfParams.setSalt.implementation = function (value) {
            console.log("value=", value);
            var res = this.setSalt(value);
            console.log("输出=", res);
            return res;
        }
    });
}

"""

script = session.create_script(scr)


script.load()
sys.stdin.read()


#1671721166,n8h3d6,3b82c886517b3b8fc03293299737ce3f

import random
import time

def getRandomStr():
    randomStr = ""
    constants = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    for _ in range(6):
        random_index = random.randint(0, len(constants) - 1)
        randomStr += constants[random_index]
    return randomStr

def get_time():
    return str(int(time.time()))

get_time()