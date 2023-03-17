import hashlib

password = "123456"
obj = hashlib.md5()
obj.update(password.encode("utf-8"))
pwd = obj.hexdigest()

print(pwd)


