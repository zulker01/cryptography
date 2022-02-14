# -*- coding: utf-8 -*-
"""
Created on Sat Feb 12 19:19:27 2022

@author: User
"""
import json,numpy as np




# open the cipher text file
cipherTextFileName = "Ciphertext_Assignment_2.txt"
cipherTextFile = open(cipherTextFileName,"r+")


tmpstr = ""
# read the cipher text file & store in a list 
cipherList = []
for lines in cipherTextFile:
    tmpstr = lines           #load the line
    tmpstr = lines[0:-1]     # delete newline from end
    
    # make the list string to list obj
    cipherList.append(json.loads(tmpstr))
    

# valid char lists
"""
A-Z : 65-90
a-z : 97-122
space : 32
comma : 44
(   : 41
) : 42

"""

def check_if_char_valid(ch):
    if ord(ch) in range(65,90):
        #print(ch)
        return True
    if ord(ch) in range(97,122):
        #print(ch)
        return True
    if ch in validChar:
        return True
    return False

validChar = [" ",",","(",")"]
alphlist = ['A']
alphSet  = {'A'}
alphSet.add(" ")
alphSet.add(",")
alphSet.add("(")
alphSet.add(")")
alphSet.add(".")
alphSet.add("?")
alphSet.add("-")
alphSet.add("!")


chara = 'A'
for i in range(26):
    alphlist.append(chr(ord(chara)+i))
    alphSet.add(chr(ord(chara)+i))
chara = 'a'
alphSet.add('a')
for i in range(26):
    alphlist.append(chr(ord(chara)+i))
    alphSet.add(chr(ord(chara)+i))
#print(len(alphSet))
cipherCount = 10

#3d list for possible char of the position
#possibleMsg=np.array([[[], []], [[], []]])
#3d list for possible pad of the position
#possiblePad=np.array([[[], []], [[], []]])
"""
possibleMsg=[]
possiblePad=[]
for i in range(cipherCount):
    possibleMsg.append([])
   # possibleMsg[0].append([])
    possiblePad.append([])
    #possiblePad[0].append([])
"""
print(cipherList[0][0])
print(cipherList[1][0])
"""
for i in range(cipherCount):  # for all 10 ciphers
    tmpstrMsg = ""
    tmpstrPad = ""
    for j in range(255):      # for every possible char ascii values
        
        cipherInt = cipherList[i][0]^j    # calculate ist cipher
       
        if check_if_char_valid(chr(cipherInt)):  # if cipher is a validc char
            tmpstrPad+=chr(j) 
            tmpstrMsg+=chr(cipherInt)    
            
            #if possibleMsg[i]:                      # if for i'th ciphertext, no possibole value for 0th position
                #print("empty possible msg")    
                #possibleMsg[i].append([])  # append a list for possible position
                #print("empty possible msg "+str(i)+" "+str(j),end=" ") 
            #print(chr(cipherInt))
            #possibleMsg[i][0].append(chr(cipherInt))  # append for ith ciphertext's first/0th position, possible msg append
            
            if possiblePad[i]:                      # if for i'th ciphertext, no possibole value for 0th position
                possiblePad[i].append([])  # append a list for possible position
            possiblePad[i][0].append(chr(j))  # append for ith ciphertext's first/0th position, possible msg append
           
                       
    possibleMsg[i].append(tmpstrMsg)
    possiblePad[i].append(tmpstrPad)
print(possibleMsg)
#print(possiblePad)   
possiblePad = ""
for j in range(255):
    wrongPadFlag = False
    for i in range(cipherCount):
        cipherInt = cipherList[i][0]^j
        if check_if_char_valid(chr(cipherInt)):  # if cipher is a validc char
            continue    
        else:
            wrongPadFlag=True
            break
    if wrongPadFlag==False:
        possiblePad+=chr(j)
"""
possiblePad=""
# possible pad for 0 th position
for j in range(256):
    wrongPadFlag=False
    for i in range(cipherCount):
        cipherInt = cipherList[i][0]^j
        if chr(cipherInt) in alphSet:
            continue
        else:
            wrongPadFlag=True
            break
    if wrongPadFlag==False:
        possiblePad+=chr(j)
print(possiblePad)
print(len(possiblePad))

"""
ci = mi ^ (c[i-1]+pi)%256
ci^mi =  (c[i-1]+pi)%256 ; xor both side with mi
pi%256  = (ci^mi-c[i-1])%256

mi = (c[i-1]+pi)%256) ^ ci
    
""" 
# possible pad for 1 th position
possiblePad1 = ""
for j in alphSet:
    wrongPadFlag=False
    for i in range(cipherCount):
        possPadInt = ((cipherList[i][1]^ord(j))-cipherList[i][0])%256
        if possPadInt in range(256):
            continue
        else:
            wrongPadFlag=True
            break
    if wrongPadFlag==False:
        possiblePad1+=chr(possPadInt)
print(len(possiblePad1))

possiblePad2 = []
for k in range(1,len(cipherList[0])): # k is the k'th char of i'th cipher
    tmpstr = ""    
    for j in range(256): # j is the possible pad
        wrongPadFlag=False
        for i in range(cipherCount):
            possPadInt = ((cipherList[i][k-1]+j)%256)^cipherList[i][k]
            if chr(possPadInt) in alphSet:
                continue
            else:
                wrongPadFlag=True
                break
        if wrongPadFlag==False:
            tmpstr+=chr(possPadInt)
    print(len(tmpstr))
    possiblePad2.append(tmpstr)
    
print(possiblePad2)
print(len(possiblePad2))
    
          