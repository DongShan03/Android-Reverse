# import frida
# import sys

# rdev = frida.get_remote_device()
# print(rdev)

# processes = rdev.enumerate_processes()
# for process in processes:
#     print(process)

# front_app = rdev.get_frontmost_application()
# print(front_app)

import frida
import sys

# 连接手机设备
rdev = frida.get_remote_device()

# Hook手机上的那个APP（app的包名字）
# 注意事项：在运行这个代码之前，一定要先在手机上启动app
session = rdev.attach("车智赢+")  # 车智赢+

scr = """
Java.perform(function () {

// 包.类
    var UserModel = Java.use("com.che168.autotradercloud.user.model.UserModel");
    var SU = Java.use("com.autohome.ahkit.utils.SecurityUtil");

    UserModel.loginByPassword.implementation = function(str,str2,str3,callback){
        console.log(str,str2,str3);

// 执行原来的方法
        this.loginByPassword(str,str2,str3,callback);
    }

    SU.encodeMD5.implementation = function(str){
        console.log("明文=", str);
        var res = this.encodeMD5(str);
        console.log("密文=", res);
        return res;
    }

});
"""

script = session.create_script(scr)

# def on_message(message, data):
#     print(message, data)

# script.on("message", on_message)

script.load()
sys.stdin.read()