from hashlib import md5

salt = b"whatyuwantjustwrite"

obj = md5(salt)
pwd = "cheng"

obj.update(pwd.encode("utf-8"))
print(obj.hexdigest())


