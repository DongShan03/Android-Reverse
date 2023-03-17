



import frida
import sys

# 连接手机设备
rdev = frida.get_remote_device()

# Hook手机上的那个APP（app的包名字）
# 注意事项：在运行这个代码之前，一定要先在手机上启动app
session = rdev.attach("微博")  # 车智赢+

scr = """
Java.perform(function () {

// 包.类
    var UserModel = Java.use("com.sina.weibo.net.engine.d");

// Hook，替换
    UserModel.a.implementation = function(str){

        var res = this.a(str);
        console.log(res);
        console.log(Java.use("android.util.Log").getStackTraceString(Java.use("java.lang.Throwable").$new()));

        return res;
// 获取调用栈
    }

});
"""

script = session.create_script(scr)

def on_message(message, data):
    print(message, data)

script.on("message", on_message)

script.load()
sys.stdin.read()