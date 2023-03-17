import frida
import sys

rdev = frida.get_remote_device()
session = rdev.attach("哔哩哔哩")

scr = """
Java.perform(function () {    
    var LibBili = Java.use("com.bilibili.nativelibrary.LibBili");

    LibBili.h.implementation = function (map, i, i2) {

        console("i=", i);
        console("i2=", i2);

        var res = this.h(map, i, i2);
        return res;
    }
});
"""

script = session.create_script(scr)


def on_message(message, data):
    print(message)


script.on("message", on_message)
script.load()
sys.stdin.read()