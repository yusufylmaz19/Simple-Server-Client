import socket
from base64 import b64encode
from Crypto.Cipher import AES

input1="rnop3TnHwJ7P9zzLb0Z3qUjfhu1Cx9bW" # 32 byt key_size
key=str.encode(input1)
input2="YsiebTh0Sjr8dZKo"
iv=str.encode(input2)  #16 byte iv_s

def encrypt(text):
    aes = AES.new(key, AES.MODE_CFB, iv)
    encrypted = aes.encrypt(text)
    return b64encode(encrypted)

input3 = input("enter your messsage: ")
message=str.encode(input3)

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((socket.gethostname(),1234))

s.listen(5)


while True:
    clintsocket , address= s.accept()
    print(f"Connection from{address} has been established")
    clintsocket.send(encrypt(message))
    clintsocket.close()


