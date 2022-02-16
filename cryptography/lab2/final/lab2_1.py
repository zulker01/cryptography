# -*- coding: utf-8 -*-
"""


@author: Zulker Nayeen
Roll : FH -11

this code shows vulnerability of One time pad reused

if otp is reused : 
    cipher1  = msg1^pad
    cipher2 = msg2^pad
    
    cipher1^cipher2 = msg1^pad ^msg2^pad
                    = msg1 ^ msg2
so if we calculate , ciph1 ^ ciph2 ^ msg1 = msg2

if we can get all possible msg1 to xor, then we
predict msg 2 easily


"""
import re
cipher1 = "e9 3a e9 c5 fc 73 55 d5"  # cipher 1
cipher2 = "f4 3a fe c7 e1 68 4a df"
tmpstr = ""
wordFileName = "word_from_ubuntu.txt"
#wordFileName = "words.txt"
wordFile = open(wordFileName,"r")


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
    return     aInt

# xor 2 strings char by char

def xor_charbychar(str1,str2):
    both_xor_string=""
    
    #if both strs are not same len copy the extra string to smaller one 
    
    if (len(str1))>(len(str2)):
        
        str2+=str1[len(str2):]
    elif len(str1)<len(str2):
        str1+=str2[len(str1):]
         
    for i in range(len(str1)):
        
        # get hext string and int string 
        hex_string1 = str_2_hex_string(str1[i])
        hex_string2 = str_2_hex_string(str2[i])
        hex_int1 = hex_str_2_int_val(hex_string1)
        hex_int2 = hex_str_2_int_val(hex_string2)
        # xor 2 int i.e 2 string's char
        xor_int = hex_int1^hex_int2
        # get string val of the int
        tmp = str(hex(xor_int))
        #get rid of 0x
        tmp=tmp[2:]
        # if the xor ans is 1 char
        if len(tmp)<2:
            tmp='0'+tmp
        both_xor_string+=tmp
        
    
    both_xor_string = "0x"+both_xor_string    
    return both_xor_string 

#for xor the cipher text which is in hex string
def xor_charbychar_hex_text(str1,str2):
    both_xor_string=""
    for i in range(2,len(str1)+1,2):
        
        # get hext string and int string 
        hex_string1 = (str1[i-2:i])
        hex_string2 = (str2[i-2:i])
        
        
        hex_int1 = hex_str_2_int_val(hex_string1)
        hex_int2 = hex_str_2_int_val(hex_string2)
        # xor 2 int i.e 2 string's char
        
        xor_int = hex_int1^hex_int2
        tmp = str(hex(xor_int))
        #get rid of 0x
        tmp=tmp[2:]
        # if the xor ans is 1 char
        if len(tmp)<2:
            tmp='0'+tmp
        both_xor_string+=tmp
        
    #print(both_xor_string)
    both_xor_string = "0x"+both_xor_string    
    return both_xor_string

#clean cipher text hex
print(cipher1)
cipher1 = "".join(re.split("[^a-fA-F0-9]*", cipher1)) 
cipher2 = "".join(re.split("[^a-fA-F0-9]*", cipher2))

# decode cipher text hex to ascii string
def decode_hexstr_to_ascii(str1):
    for i in range(2,len(str1)+1,2):
        hex_string1 = (str1[i-2:i])
        
        intval = int("0x"+hex_string1,16)
        
    bytes_object = bytes.fromhex(str1)  # get the bytes of string
    cipher1text = bytes_object.decode("ASCII") # convert bytes to string
    return cipher1text



# xor both cipher & get int
both_cipher_xor_int = (hex_str_2_int_val(cipher1)^hex_str_2_int_val(cipher2))
# xor both cipher & get hex
both_cipher_xor_hex = hex(both_cipher_xor_int)
#string value of both ciphers
both_cipher_xor = str(both_cipher_xor_hex)
# xor both cipher char by char
both_cipher_xor2 = xor_charbychar_hex_text(cipher1,cipher2)
print("xor of both cipers : ")
print(both_cipher_xor2)
breakFlag = 0
# get ascii from hext string 
ascii_cipher_xor =decode_hexstr_to_ascii(both_cipher_xor[2:])
# as each char is 1 byte in ascii, so 2 digit in hex, so msg len in cipherhex/2
msgwordlen = int(len(cipher1)/2)



#retrieve the words
words=[]
i=0
for line in wordFile:
    tmpstr = line
    # readline adds an extra newline end of the word, so cut it
    tmpstr = tmpstr[0:-1]
    
    if len(tmpstr)!=msgwordlen or (not tmpstr.isalpha()):
        continue
    words.append(tmpstr)
    
# loop through all possible words
for i in range(len(words)):
    
    # get a guessed word, from msg1^msg2 
    # it will be retrieved by 
    #  msg1 = (msg1^msg2)^word[i]
    wordguesshex = xor_charbychar(ascii_cipher_xor,words[i])
    wordguess = decode_hexstr_to_ascii(wordguesshex[2:])
    
    # if the guessed word is a valid word, then print it 
    if wordguess in words:  
        print("possible words : ")
        print(words[i])
        print(wordguess)
        
# close the word file        
wordFile.close()