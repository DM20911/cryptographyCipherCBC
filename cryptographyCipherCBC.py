#!/usr/bin/python 
#https://twitter.com/DM20911


import sys
import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend


backend = default_backend()
key = (12345678901234567890123456789012).to_bytes(32, sys.byteorder)
iv = os.urandom(16)
cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=backend)

encryptor = cipher.encryptor()
encrip = encryptor.update(b"a secret message") + encryptor.finalize()
print('\nMensaje encriptado:\n')
print(encrip)
decryptor = cipher.decryptor()
decrip =decryptor.update(encrip) + decryptor.finalize()
print('\nMensaje desencriptado:\n')
print (decrip)