import base64
from Crypto.Cipher import AES
from sys import stdin

"""
encode.py
By: David Huie

bother_encoded.py was generated as follows:
   cat bother.py | python encode.py > bother_encoded.py

secret_key below was created by taking the sha1 sum of a two character string
using the shasum utility. In other words,
   SECRET_KEY=$(echo 'XX' | shasum)
where 'XX' is my 2 character secret key.

If you can't decode bother_encoded.py, I don't know
even know what to say...
"""
program_text = stdin.read()

secret_key = 'you will have to guess the key!'[:16]
cipher = AES.new(secret_key, AES.MODE_ECB)
encoded = base64.b64encode(cipher.encrypt(program_text + ' ' *  (16 - len(program_text) % 16)))

print encoded
