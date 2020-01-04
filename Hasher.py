#! /usr/bin/python3

import hashlib

hashvalue = input("- Enter a string to hash: ")

hashobj1 = hashlib.md5()
hashobj1.update(hashvalue.encode())
print("Md5   : {}".format(hashobj1.hexdigest()))

hashobj2 = hashlib.sha1()
hashobj2.update(hashvalue.encode())
print("Sha1  : {}".format(hashobj2.hexdigest()))

hashobj3 = hashlib.sha224()
hashobj3.update(hashvalue.encode())
print("Sha224: {}".format(hashobj3.hexdigest()))

hashobj4 = hashlib.sha256()
hashobj4.update(hashvalue.encode())
print("Sha256: {}".format(hashobj4.hexdigest()))

hashobj5 = hashlib.sha512()
hashobj5.update(hashvalue.encode())
print("Sha512: {}".format(hashobj5.hexdigest()))