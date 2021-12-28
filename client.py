import socket
from base64 import b64decode
from Crypto.Cipher import AES


input1="rnop3TnHwJ7P9zzLb0Z3qUjfhu1Cx9bW" # 32 byt key_size
key=str.encode(input1)
input2="YsiebTh0Sjr8dZKo"
iv=str.encode(input2)  #16 byte iv_s

def decrypt(data):
    aes = AES.new(key, AES.MODE_CFB, iv)
    encrypted = b64decode(data)
    decrypted = aes.decrypt(encrypted)
    return decrypted


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1234))

full_msg=''

while True:
    msg=s.recv(8)
    if len(msg)<=0:
        break
    full_msg+=msg.decode("utf-8")
    encrypted_msg=str.encode(full_msg)
    
print(decrypt(encrypted_msg))

