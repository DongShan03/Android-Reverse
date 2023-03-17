# import frida, sys, uuid
# import random


# session = frida.get_remote_device().attach("车智赢+")


# scr = """

# Java.perform(function() {
#     var AHAPIHelper = Java.use("com.autohome.ahkit.AHAPIHelper");
#     var SecurityUtil = Java.use("com.autohome.ahkit.utils.SecurityUtil");
#     var PushModel = Java.use("com.che168.autotradercloud.base.push.model.PushModel");

#     SecurityUtil.encode3Des.implementation = function(context, str) {
#         console.log("输入了参数str=", str);

#         var res = this.encode3Des(context, str);
#         console.log("输出了：", res);
#         return res;
#     }
#     PushModel.regDevice.implementation = function(str) {
#         console.log("str参数=", str);
#         str = "";
#         this.regDevice(str);
#     }
#     AHAPIHelper.getDesKey.implementation = function(context) {
#         var res = this.getDesKey(context);
#         console.log("Key=", res);
#         return res;
#     }
# });

# """
# script = session.create_script(scr)

# script.load()
# sys.stdin.read()

import base64, uuid, random





if __name__ == "__main__":
    udid = get_udid()
    print(udid)