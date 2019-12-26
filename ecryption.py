import random

def encrypt(k, m):
    string = ''
    for i in m:
        string += chr(ord(i) + k)
    return string

def decrypt(k,m):
    string = ''
    for i in m:
        string += chr(ord(i) - k)
    return string

def hack(msg):
    s = {i: msg.count(i) for i in msg}
    string = ''
    k = ord(max(s, key=s.get)) - 108
    for i in msg:
        string += chr(ord(i) - k)
    return string


k = random.randint(1, 33)    
msg = 'Hello, World.'
msg1= encrypt(k, msg)
print(msg1)
msg2 = hack(msg1)
print('\n')
print(msg2)