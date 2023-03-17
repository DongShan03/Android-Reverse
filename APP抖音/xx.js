Java.perform(function () {

    // 包.类
        var UUID = Java.use("java.util.UUID");
    
    // Hook，替换
        UUID.randomUUID.implementation = function(){
            var res = this.randomUUID();
            console.log("uuid=", res);
    // 获取调用栈
    console.log(Java.use("android.util.Log").getStackTraceString(Java.use("java.lang.Throwable").$new()));
            return res;
        }
    
    });