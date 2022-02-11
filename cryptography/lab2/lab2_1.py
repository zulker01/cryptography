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

hex_string = "0x616263"[2:]

Slice string to remove leading `0x`


bytes_object = bytes.fromhex(hex_string)

Convert to bytes object


ascii_string = bytes_object.decode("ASCII")

Convert to ASCII representation

print(ascii_string)



"""
import re
cipher1 = "e9 3a e9 c5 fc 73 55 d5"
cipher2 = "f4 3a fe c7 e1 68 4a df"
tmpstr = ""
wordFileName = "word_from_ubuntu.txt"
#wordFileName = "words.txt"
wordFile = open(wordFileName,"r")


cribs=[" the "," and "]

"""
# akam
def str_2_hexstr(str1):
    hexstr = "0x"
    
    for i in range(len(str1)):
        hexstr+= (hex(ord(str[i])))
        
    #print(hexstr)
    aInt = int(hexstr, 16)
    return     hex(aInt)
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

# xor 2 string char by char
#def xor_string_charbychar(str1,str2):
"""    
  #akam  
def xor_string(str1,str2):
    # ord returns an integer of the ascii code of a given one char string
    # chr returns a one char string from a given ascii code value
    # hexlify turns the given string into a hex string
    
    return (''.join(chr(ord(a)^ord(b)) for a, b in zip(str1, str2)))
"""
def xor_charbychar(str1,str2):
    both_xor_string=""
    
    #if both strs are not same len copy the extra string to smaller one 
    
    if (len(str1))>(len(str2)):
        #print("word1 is bigger"+str(len(str1))+" "+str(len(str1)) )
        str2+=str1[len(str2):]
    elif len(str1)<len(str2):
        #print("word2 is bigger")
        str1+=str2[len(str1):]
         
    for i in range(len(str1)):
        
        hex_string1 = str_2_hex_string(str1[i])
        hex_string2 = str_2_hex_string(str2[i])
        hex_int1 = hex_str_2_int_val(hex_string1)
        hex_int2 = hex_str_2_int_val(hex_string2)
        #print("xoring "+str1[i]+" and "+str2[i])
        xor_int = hex_int1^hex_int2
        #print(hex(xor_int))
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

#for xor the cipher text which is in hex string
def xor_charbychar_hex_text(str1,str2):
    both_xor_string=""
    for i in range(2,len(str1)+1,2):
        hex_string1 = (str1[i-2:i])
        hex_string2 = (str2[i-2:i])
        
        
        hex_int1 = hex_str_2_int_val(hex_string1)
        hex_int2 = hex_str_2_int_val(hex_string2)
       # print("for i="+str(i)+" strings : "+str1[i-2:i]+" "+str2[i-2:i]+" int "+str(hex_int1)+" "+str(hex_int2))
        #print("xoring "+str1[i]+" and "+str2[i])
        xor_int = hex_int1^hex_int2
        #print(hex(xor_int))
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
 
str4 = str_2_hex_string("networks")
print(str_2_hex_string("networks"))
print(hex_str_2_hex_val(str4))    
print(cipher1)
print(words[99])
print(len(words)) 

 """ 
#clean cipher text hex
print(cipher1)
cipher1 = "".join(re.split("[^a-fA-F0-9]*", cipher1)) 
cipher2 = "".join(re.split("[^a-fA-F0-9]*", cipher2))

# decode cipher text hex to ascii string
def decode_hexstr_to_ascii(str1):
    for i in range(2,len(str1)+1,2):
        hex_string1 = (str1[i-2:i])
        
        intval = int("0x"+hex_string1,16)
        #print(hex_string1+" int "+str(intval))
        #if intval>128:
            #return " "
    bytes_object = bytes.fromhex(str1)
    cipher1text = bytes_object.decode("ASCII")
    return cipher1text



print(type(hex_str_2_int_val(cipher1)))
both_cipher_xor_int = (hex_str_2_int_val(cipher1)^hex_str_2_int_val(cipher2))
both_cipher_xor_hex = hex(both_cipher_xor_int)
both_cipher_xor = str(both_cipher_xor_hex)
both_cipher_xor2 = xor_charbychar_hex_text(cipher1,cipher2)
print(both_cipher_xor_int)
print(both_cipher_xor)
print(both_cipher_xor2)
breakFlag = 0
print(decode_hexstr_to_ascii(str_2_hex_string("nescafe")))
print(decode_hexstr_to_ascii(both_cipher_xor[2:]))
ascii_cipher_xor =decode_hexstr_to_ascii(both_cipher_xor[2:])
msgwordlen = int(len(cipher1)/2)
print(msgwordlen)


#retrieve the words
words=[]
i=0
for line in wordFile:
    tmpstr = wordFile.readline()
    if tmpstr.find("networks")!=-1:
        print(len(words))
        print(tmpstr)
    #print(tmpstr)
    # readline adds an extra newline end of the word, so cut it
    tmpstr = tmpstr[0:-1]
    if tmpstr=="networks" or tmpstr=="security":
        print("found")
    if len(tmpstr)!=msgwordlen or (not tmpstr.isalpha()):
        continue
    words.append(tmpstr)
    
        
wordlen =len(words)
print("last word "+words[wordlen-2])
#words = [x for x in words if x not in words]
"""
for i in range(wordlen):
    print(str(i)+" prt1 "+words[i])
    if i>10:
        break
    if msgwordlen!=len(words[i]):
        print(words[i])
        words.remove(words[i])
        i-=1
        wordlen-=1
    elif not words[i].isalpha():
        print(words[i])
        words.remove(words[i])
        i-=1
        wordlen-=1
    print(str(i)+" prt2 "+words[i])
    """
print("networks" in words)
"""
words = [x for x in words if len(x)==msgwordlen]
words = [x for x in words if x.isalpha()]
"""
print(len(words))
print(words[1])


"""
for i in range(len(words)):
    for j in range(len(words)):
        #print(words[j])
        word1int= hex_str_2_int_val(str_2_hex_string(words[i]))
        word2int = hex_str_2_int_val(str_2_hex_string(words[j]))
        both_words_xor_int = word1int^word2int
        both_words_xor = xor_charbychar(words[i],words[j])
        
        #if (both_cipher_xor==both_words_xor) or (both_words_xor_int==both_cipher_xor_int):
        if (both_cipher_xor==both_words_xor):    
            print("possible words : ")
            print(words[i])
            print(words[j])
            print(both_cipher_xor)
            print(both_words_xor)
            breakFlag = 1
    if breakFlag==1:
        break
    """
#words[0] = "networks"
for i in range(len(words)):
    """
    wordhex  = str_2_hex_string(words[i])
    wordhex =  xor_charbychar_hex_text(wordhex, both_cipher_xor[2:])
    if len(wordhex[2:])>msgwordlen:
        continue
    wordguess = decode_hexstr_to_ascii(wordhex[2:])
    """
    wordguesshex = xor_charbychar(ascii_cipher_xor,words[i])
    wordguess = decode_hexstr_to_ascii(wordguesshex[2:])
    #print(wordguess)
    #break
    #print(wordguess)
    """
    if i>433:
        print(str(wordhex)+" "+wordguess)
    #print(str(i),end=" ")
    """
    if wordguess in words:  
        print("possible words : ")
        print(words[i])
        print(wordguess)
        #break
        
wordFile.close()