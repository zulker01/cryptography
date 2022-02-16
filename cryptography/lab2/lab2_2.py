# -*- coding: utf-8 -*-
"""
Created on Sat Feb 12 11:28:13 2022

@author: User
"""
# convert string to hexadecimal string
def str_2_hex_string(str1):
    # convert to byte by encode :
    bite = str1.encode("utf-8")
    # covert the byte to hex
    hex_string = bite.hex()
    # return the hex string
    return hex_string
# convert hexa string to int value
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


# convert msg to cipher
def convert_2_cipher(msg,pad):
    cipher=bytearray()  # bytearrray type var
    msgbytes = (bytearray(msg,"ascii"))  # convert msg ascii to bytearrya
    padbytes = (bytearray(pad,"ascii"))  # convert pad ascii to bytearray
    # get zeroth cipher
    cipher.append((msgbytes[0]^((0+padbytes[0])%256)))
    
    # loop through 1 to last cipher
    for i in range(1,len(msgbytes)):
        
        tmp = msgbytes[i]^((cipher[i-1]+padbytes[i])%256) # ci = (mi xor (pi+ci-1)%256)
        cipher.append(tmp)
        
    return cipher.hex()  # conveert bytearrya to hex cipher text

# function converts cipiher to plain text
def convert_2_plain(cipher,pad):
    plaintxt= bytearray()  # get byte arry, which is byte from of the string
    cipherbytes = bytearray.fromhex(cipher)    # cipiher text bytes
    padbytes = (bytearray(pad,"ascii"))     # convert pad bytes to from ascii to bytearry
   
    plaintxt.append(((0+padbytes[0])%256)^cipherbytes[0])  # get first char of plaintxt
    
    # loop through 2nd  to last positoin to get ciphertext
    for i in range(1,len(cipherbytes)):
        tmp = cipherbytes[i]^((cipherbytes[i-1]+padbytes[i])%256)  # mi = (ci xor (pi+ci-1)%256)
        plaintxt.append(tmp)
        
    

    return plaintxt.decode("utf-8")   # decode bytearray to ascii string







msg1 = "iamagoodboy"
pad1 = "deceiptives"

# convert the message to cipher
print("\n")
cipher = convert_2_cipher(msg1, pad1)
print("Encrypting (ans is in hex) :\n \n"+ msg1+" -> "+cipher)
print("\n")
# convert cipher to plain
plain = convert_2_plain(cipher, pad1)
print("decrypting (hex cipher to plain)\n\n " +cipher+" -> "+plain)
