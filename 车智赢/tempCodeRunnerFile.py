, sys, uuid
# import random


# session = frida.get_remote_device().attach("车智赢+")


# scr = """
# Java.perform(function() {
#     var LaunchModel = Java.use("com.che168.autotradercloud.launch.model.LaunchModel");

#     LaunchModel.lambda$initRequestCommonParams$0.implementation = function(i, treeMap) {
#         console.log("输入了：", treeMap);

#         var res = this.lambda$initRequestCommonParams$0(i, treeMap);
#         console.log("输出了：", res);
#         return res;
#     }
# });
# """

# script = session.create_script(scr)

# script.load()
# sys.stdin.read()