import execjs

js = """
function fn(a, b) {
    return a + b;
}
"""

a = execjs.compile(js)
ret = a.call("fn", 10, 20)
print(ret)




