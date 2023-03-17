from Crypto.PublicKey import RSA

rsa_key = RSA.generate(2048)

private_key = rsa_key.exportKey()

public_key = rsa_key.publickey().exportKey()



