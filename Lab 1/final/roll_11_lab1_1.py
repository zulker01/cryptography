# -*- coding: utf-8 -*-
"""


@author: 

Zulker Nayeen

Roll- FH-11
4th year 1st Semester

Course : Cryptography & Security Lab

Labwork : Cryptoanalysis & Cracking Vigenere cipher 

Brief discussion : 
    After finding an easy way to break ceaser cipher, Vignere cipher was 
    introduced. 
    
    Vignere cipher dont necessarily need long key, rather 
    it uses same key repeatedly to creat e long key of size of the plain text
    so even if plain text has repeated word, it faces different key to encrypt
    itself, thus makes it quit impossible to guess by frequency analysis
    
"""
import re

# function to add space
def litering_by_three(a):
    return ' '.join([a[i:i + 5] for i in range(0, len(a), 5)])


# function to convert plaintext to ciphertext
def cypherConvert(plaintextClean, key):
    
    plaintextLen = len(plaintextClean) #get lenth of text
    j = 0
    cyphertext = ""
    chara = ""
    charcipher = 0
    keyLen = len(key)                 # get len of key      
    for i in range(plaintextLen):
       # if key limit has been reached, start from starting of key string
       if(j==keyLen):
           j=0
       
       chara = plaintextClean[i]  # get plaintext character    
       # cipher the character & get e int value
       charcipher = ((dicti[plaintextClean[i]]+dicti[key[j]])%52)
       
       # get the cipher char
       chara = alphlist[charcipher]
       cyphertext+=chara       # add it to cipher text
       
       j+=1 # proceed to next key
    
    # get spaces after each 5 char
    cyphertext = litering_by_three(cyphertext)
    return cyphertext



# function to cipher to plain text
def cypherToPlain(cipherText,key):
    ciphertextLen = len(cipherText)
    j = 0
    convertedplaintext = ""
    chara = ""
    charplain = 0
    keyLen = len(key)
    for i in range(ciphertextLen):
       
       # if key limit has been reached, start from starting of key string
       
       if(j==keyLen):
           j=0
       chara = cipherText[i]  # ciphertext char   
       if chara==" ":         # if it is space, do nothing
           continue
       # convert from cipher text to plaintext int value
       charplain = ((dicti[cipherText[i]]-dicti[key[j]])%52)
       
       # get int to plain text
       chara = alphlist[charplain]    
       convertedplaintext+=chara
       
       # proceed to next key
       j+=1
    convertedplaintext=litering_by_three(convertedplaintext)
    return convertedplaintext

# file name
inputFileName = 'input.txt'
outputFileName = 'output.txt'
keyFileName = 'key.txt'

# mapping characters
# dictionary will map as : {A:0, B:1, C:2....., Z:25, a:26,b:27 ...}
# alphlist will map : [A,B,C......Z,a,b,c,..z]
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
#print(dicti)
#print(alphlist)

# open file 

inputFile = open(inputFileName,'r+')
outputFile = open(outputFileName,'w+')
keyFile = open(keyFileName,'r+')

#" ".join(re.split("[^a-zA-Z]*", ini_string))

# read input file & key
plaintext = inputFile.read()
key = keyFile.read()

#print(plaintext)

# clean the plaintext , clean spaces or any other non alphabtic char
plaintextClean = "".join(re.split("[^a-zA-Z]*", plaintext))

#print(plaintextClean)

#clean plaintext


#convert plaintext to cipher text
cyphertext = cypherConvert(plaintextClean, key)
print("cipher text : ")
print(cyphertext)  # print the ciphertext
print()
outputFile.write(cyphertext)  # write cipher text to file
convertedplaintext = cypherToPlain(cyphertext, key) # convert cipher to plain
print("plain text : ")
print(convertedplaintext)

# close file

inputFile.close()
outputFile.close()
keyFile.close()
