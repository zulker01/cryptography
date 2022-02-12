# -*- coding: utf-8 -*-
"""
Created on Sat Feb 12 11:28:13 2022

@author: User
"""

def str_2_hex_string(str1):
    # convert to byte by encode :
    bite = str1.encode("utf-8")
    # covert the byte to hex
    hex_string = bite.hex()
    # return the hex string
    return hex_string

def hex_str_2_int_val(str1):
    #insert 0x if not inserted
    if len(str1)==0:
        return 0
    if str1[0:1]!="0x":
        str1 = "0x"+str1
    
    #hex string to int
    aInt = int(str1, 16)
    #return int of the hex string
    #print(str(str1)+" "+str(aInt))
    return     aInt

def xor_2_hex_string(str1,str2):
    hexint1 = hex_str_2_int_val(str1)
    hexint2 = hex_str_2_int_val(str2)
    
    hexored = hexint1^hexint2
    return hexored.to_bytes(1, "big")

def xor_2_string(str1,str2):
    return str1^str2
"""
def convert_2_cipher(msg,pad):
    cipher=[]
    #cipher.append(str_2_hex_string(msg[0]),str_2_hex_string(pad[0]))
    cipher.append(xor_2_hex_string(str_2_hex_string(msg[0]),str_2_hex_string(pad[0])))
    
    padbyte =bytearray(pad,"ascii")
    for i in range(1,len(msg)):
        tmp = (cipher[i-1] + padbyte[i]) % 256
        cipher.append(xor_2_hex_string(str_2_hex_string(msg[0]),tmp))
"""
def convert_2_cipher(msg,pad):
    cipher=bytearray()
    msgbytes = (bytearray(msg,"ascii"))
    padbytes = (bytearray(pad,"ascii"))
    print(type(msgbytes[0]))
    print(bytearray(msg[0],"ascii"))
    cipher.append((msgbytes[0]^padbytes[0]))
    
    for i in range(1,len(msgbytes)):
        #print(str(i)+" len msg "+str(len(msgbytes)))
        tmp = (cipher[i-1]+padbytes[i])%256
        cipher.append(msgbytes[i]^tmp)
        
    print(type(cipher[0]))
    print(cipher.hex())
    return cipher.hex()
    
def convert_2_plain(cipher,pad):
    plaintxt= bytearray()
    cipherbytes = bytearray.fromhex(cipher)
    padbytes = (bytearray(pad,"ascii"))
   
    plaintxt.append((cipherbytes[0]^padbytes[0]))
    
    for i in range(1,len(cipherbytes)):
        tmp = (cipherbytes[i-1]+padbytes[i])%256
        plaintxt.append(cipherbytes[i]^tmp)
        
    print(type(cipher[0]))

    return plaintxt.decode("utf-8")







msg1 = "iamagoodboy"
pad1 = "deceiptives"

cipher = convert_2_cipher(msg1, pad1)
print("Encrypting (ans is in hex) :\n "+ msg1+" -> "+cipher)
plain = convert_2_plain(cipher, pad1)
print("decrypting (hex cipher to plain) " +cipher+" -> "+plain)
