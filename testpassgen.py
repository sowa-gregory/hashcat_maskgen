import hashlib, binascii

p = "blek"
hash = hashlib.new('md4',p.encode('utf-16le')).digest()
print (binascii.hexlify(hash).decode('ascii').upper())
