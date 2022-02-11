# -*- coding: utf-8 -*-
"""
Created on Fri Feb 11 15:10:44 2022

@author: User
hex_string = "0xAA"

"0x" also required

an_integer = int(hex_string, 16)

an_integer is a decimal value

hex_value = hex(an_integer)

print(hex_value)

Hex value from hex_string
Output

"""

cipher1 = "e9 3a e9 c5 fc 73 55 d5"
cipher2 = "f4 3a fe c7 e1 68 4a df"

wordFileName = "words.txt"
wordFile = open("words.txt","r+")
cribs=[" the "," and "]
# akam
def str_2_hexstr(str1):
    hexstr = "0x"
    
    for i in range(len(str1)):
        hexstr+= (hex(ord(str[i])))
        
    print(hexstr)
    aInt = int(hexstr, 16)
    return     hex(aInt)

def str_2_hex_string(str1):
    # convert to byte by encode :
    bite = str1.encode("utf-8")
    # covert the byte to hex
    hex_string = bite.hex()
    # return the hex string
    return hex_string

def hex_str_2_hex_val(str1):
    #insert 0x if not inserted
    if str1[0:1]!="0x":
        str1 = "0x"+str1
    print(str1)
    #hex string to int
    aInt = int(str1, 16)
    #return int to hex
    return     hex(aInt)
  #akam  
def xor_string(str1,str2):
    # ord returns an integer of the ascii code of a given one char string
    # chr returns a one char string from a given ascii code value
    # hexlify turns the given string into a hex string
    
    return (''.join(chr(ord(a)^ord(b)) for a, b in zip(str1, str2)))
"""
ciphertmp1 = xor_string("muri", "khao")
ciphertmp2 = xor_string("vaat", "khao")
ciphertmp12xor = xor_string(ciphertmp1,ciphertmp2)
print(xor_string("muri", "khao"))
print(xor_string(ciphertmp1, "khao"))
print(xor_string(cipher1, cipher2))

def crib(text, c):
    for i in range(0, len(text) - len(c) + 1):
        Pt = text[i:(i+len(c))]
        print("\t{0}: {1}".format(i,xor_string(Pt,c)))
        
crib(ciphertmp12xor,"ax")
  """
str4 = str_2_hex_string("networks")
print(str_2_hex_string("networks"))
print(hex_str_2_hex_val(str4))    

  
        