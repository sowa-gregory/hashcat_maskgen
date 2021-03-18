import os,binascii

for i in range(1000):
    pwd=binascii.b2a_hex(os.urandom(16))
    print(pwd.decode('ascii').upper())
