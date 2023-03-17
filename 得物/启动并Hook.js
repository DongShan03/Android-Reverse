function hook_RegisterNatives() {
    Java.perform(function() {
        var Builder = Java.use("okhttp3.OkHttpClient$Builder");

        Builder.proxy.implementation = function (proxy) {
            var res = this.proxy(null);
            return res;
        }
    });
}

setImmediate(hook_RegisterNatives);