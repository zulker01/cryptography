# -*- coding: utf-8 -*-
"""
Created on Sun Jan 30 22:13:44 2022

@author: User
"""
import re

inputFileName = 'plaintext.txt'
outputFileName = 'cyphertext.txt'
keyFileName = 'key.txt'

# mapping characters
chara = 'B'
i = 0
dicti = {'A':i}
alphlist = ['A']
for i in range(25):
    dicti.update({chr(ord(chara)+i):i+1})
    alphlist.append(chr(ord(chara)+i))
chara = 'a'
for i in range(26):
    dicti.update({chr(ord(chara)+i):i+26})
    alphlist.append(chr(ord(chara)+i))
print(dicti)
print(alphlist)
# open file 

inputFile = open(inputFileName,'r+')
outputFile = open(outputFileName,'w+')
keyFile = open(keyFileName,'r+')

#" ".join(re.split("[^a-zA-Z]*", ini_string))

plaintext = inputFile.read()
key = keyFile.read()

print(plaintext)

plaintextClean = "".join(re.split("[^a-zA-Z]*", plaintext))

print(plaintextClean)

def litering_by_three(a):
    return ' '.join([a[i:i + 5] for i in range(0, len(a), 5)])
#clean plaintext
#print(inputFile.read())
#outputFile.write(" ami banglay hashi , banglay vashi")

def cypherConvert(plaintextClean, key):
    
    plaintextLen = len(plaintextClean)
    j = 0
    cyphertext = ""
    chara = ""
    charcipher = 0
    keyLen = len(key)
    for i in range(plaintextLen):
       #print(plaintextClean[i])
       if(j==keyLen):
           j=0
       chara = plaintextClean[i]    
       charcipher = ((dicti[plaintextClean[i]]+dicti[key[j]])%52)
       """
       if(chara.isupper()):
           charcipher = ((ord(plaintextClean[i])+ord(key[j])-65-65)%52)
           #charcipher+=ord('A')
           chara = chr(charcipher+65) 
       else :
           charcipher = ((ord(plaintextClean[i])+ord(key[j])-97-97)%52)
           #charcipher+=ord('a')
       """ 
       chara = alphlist[charcipher]
       cyphertext+=chara
       
       j+=1
    temp = ""
    lenth = len(cyphertext)-5
    print(len(cyphertext))
    """
    for i in range(lenth):
        if (i+1)%6 == 0:
            print(i+1)
            temp = cyphertext[0:i] + ' ' + cyphertext[i:]
            cyphertext = temp
    """
    cyphertext = litering_by_three(cyphertext)
    return cyphertext

def cypherToPlain(cipherText,key):
    ciphertextLen = len(cipherText)
    j = 0
    convertedplaintext = ""
    chara = ""
    charplain = 0
    keyLen = len(key)
    for i in range(ciphertextLen):
       #print(plaintextClean[i])
       
       if(j==keyLen):
           j=0
       chara = cipherText[i]    
       if chara==" ":
           continue
       charplain = ((dicti[cipherText[i]]-dicti[key[j]])%52)
       """
       if(chara.isupper()):
           charplain+=ord('A')
       else :
           charplain+=ord('a')
    """
       chara = alphlist[charplain]    
       convertedplaintext+=chara
       
       j+=1
    return convertedplaintext

cyphertext = cypherConvert(plaintextClean, key)
print(cyphertext)
outputFile.write(cyphertext)
convertedplaintext = cypherToPlain(cyphertext, key)
print(convertedplaintext)

# close file

inputFile.close()
outputFile.close()
keyFile.close()
