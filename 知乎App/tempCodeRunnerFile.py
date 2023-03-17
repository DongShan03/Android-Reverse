import frida
import sys

# 连接手机设备
rdev = frida.get_remote_device()

# Hook手机上的那个APP（app的包名字）
# 注意事项：在运行这个代码之前，一定要先在手机上启动app
session = rdev.attach("知乎")  # 车智赢+

scr = """
Java.perform(function () {

// 包.类
    var CloudIDHelper = Java.use("com.zhihu.android.cloudid.CloudIDHelper");

// Hook，替换
    CloudIDHelper.encrypt.implementation = function(str,str2,str3,str4,str5,str6,str7){
        console.log('str=', str);
        console.log('str2=', str2);
        console.log('str3=', str3);
        console.log('str4=', str4);
        console.log('str5=', str5);
        console.log('str6=', str6);
        console.log('str7=', str7);

// 执行原来的方法
        this.encrypt(str,str2,str3,str4,str5,str6,str7);
// 获取调用栈
console.log(Java.use("android.util.Log").getStackTraceString(Java.use("java.lang.Throwable").$new()));
    }

});
"""

script = session.create_script(scr)

def on_message(message, data):
    print(message, data)

script.on("message", on_message)

script.load()
sys.stdin.read()