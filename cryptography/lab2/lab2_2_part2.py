# -*- coding: utf-8 -*-
"""
Created on Sat Feb 12 19:19:27 2022

@author: User
"""
import json,numpy as np,re,itertools,heapq




# open the cipher text file
cipherTextFileName = "Ciphertext_Assignment_2.txt"
cipherTextFile = open(cipherTextFileName,"r+")
wordFileName = "word_from_ubuntu.txt"
#wordFileName = "words.txt"
wordFile = open(wordFileName,"r")




#retrieve the words
words=set()
i=0
for line in wordFile:
    tmpstr = line
    
    #print(tmpstr)
    # readline adds an extra newline end of the word, so cut it
    tmpstr = tmpstr[0:-1]
    if len(tmpstr)<=1:
        continue
    tmpstr.lower() # get lowercase for max match
    #if len(tmpstr)!=msgwordlen or (not tmpstr.isalpha()):
        #continue
    words.add(tmpstr)
#print("word len "+str(len(words)))
words.add("a")
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
#print(cipherList[0][0])
#print(cipherList[1][0])
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
possiblePad2 = [] # list of all possible pad list for each position
possibleMsg2 = [] # list of all possible msg list for each position
# possible pad for 0th position
possibleMsg=""
possiblePad=""
# possible pad for 0 th position
for j in range(256):
    wrongPadFlag=False
    for i in range(cipherCount):
        cipherInt = cipherList[i][0]^j
        if chr(cipherInt) in alphSet:
            possibleMsg+=chr(cipherInt)
            continue
        else:
            wrongPadFlag=True
            possibleMsg=""
            break
    if wrongPadFlag==False:
        possiblePad+=chr(j)
#peinr(possiblePad)
#print(len(possiblePad))
possiblePad2.append(possiblePad)

"""
ci = mi ^ (c[i-1]+pi)%256
ci^mi =  (c[i-1]+pi)%256 ; xor both side with mi
pi%256  = (ci^mi-c[i-1])%256

mi = (c[i-1]+pi)%256) ^ ci
    

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
"""
"""
possiblePad2 = []
tmpstr = ""    
for j in range(256): # j is the possible pad
    wrongPadFlag=False
    for i in range(cipherCount):
        possPadInt = cipherList[i][1]^((cipherList[i][0]+j)%256)
        if chr(possPadInt) in alphSet:
            continue
        else:
            wrongPadFlag=True
            break
    if wrongPadFlag==False:
        tmpstr+=chr(j)
        possiblePad2.append(chr(j))
print(possiblePad2)
#possiblePad2.append(tmpstr)
for k in range(1,len(cipherList[0])): # k is the k'th char of i'th cipher
    #print( " traversing for "+str(k),end=" ")
    possiblePad = "" 
    for j in range(256): # j is the possible pad
        wrongPadFlag=False
        for i in range(cipherCount):
            possPadInt = cipherList[i][k]^((cipherList[i][k-1]+j)%256)
            if chr(possPadInt) in alphSet:
                continue
            else:
                wrongPadFlag=True
                break
        if wrongPadFlag==False:
            tmpstr+=chr(j)
            possiblePad2.append(chr(j))

"""

for k in range(1,len(cipherList[0])): # k is the k'th char of i'th cipher
    #print( " traversing for "+str(k),end=" ")
    possiblePad = "" 
    possibleMsg =""
    for j in range(256): # j is the possible pad
        wrongPadFlag=False
        for i in range(cipherCount):
            possPadInt = cipherList[i][k]^((cipherList[i][k-1]+j)%256)
            
            if chr(possPadInt) in alphSet:
                possibleMsg+=chr(possPadInt)
                continue
            else:
                wrongPadFlag=True
                possibleMsg=""
                break
        if wrongPadFlag==False:
            possiblePad+=chr(j)
            #print(possiblePad)
            #print(" msg for "+chr(possPadInt)+" is "+possibleMsg)
            #print(len(possiblePad),end=" ")
    #print(" for position "+str(k)+" possble pad : "+possiblePad)
    
    possiblePad2.append(possiblePad)
   
print(possiblePad2)
#print(len(possiblePad2))

# get the ciphertext from the cipher list int value

def getCipherText():
    cipherListText=[]
    for i in range(cipherCount):
        tmpstr = ""
        for j in cipherList[i]:
            tmpstr+=chr(j)
        #print(tmpstr,end=" ")
        cipherListText.append(tmpstr)
    return cipherListText 
#def recursion(iNoPad,possiblePad2)

#get plaintext
def convert_2_plain(cipherNo,cipherStartIndex,cipherEndIndex,pad):
    plaintxt=""
    j=0
    #print("called for "+str(cipherNo)+" "+str(cipherNo)+" "+str(cipherStartIndex)+" "+str(cipherEndIndex)+" "+pad)
    for i in range(cipherStartIndex,cipherEndIndex):
        #print("for cipher no "+str(cipherNo)+" position i="+str(i)+" pad is "+str(ord(pad[j])))
        if i==0:  # 0th position decrytpion
            plaintxt+=chr(cipherList[cipherNo][i]^ord(pad[j]))
        else:
            possPadInt = cipherList[cipherNo][i]^(((cipherList[cipherNo][i-1]+ord(pad[j]))%256))
            #plaintxt+=chr(((cipherList[cipherNo][i-1]+ord(pad[j]))%256)^cipherList[cipherNo][i])
            plaintxt+=chr(possPadInt)
        j+=1    
    return plaintxt



cipherListText= getCipherText()
#print(cipherListText[0])
#msg from 5 padlen
# dictionary to count which pad has how many good words
"""
goodWordCount={}
def checkMsgWithDictionary(pad):
    maxLenLastWord=0    # the last word which might be spilited , i.e : "develo" so have to check along with prev 6 msg in next iter
    goodwrd=0
    for i in range(cipherCount):
        plaintxt = convert_2_plain(i,0,len(pad), pad)
        #print(plaintxt)
        words_of_msg = re.split(r"[-!,.?()\s]\s*", plaintxt)
       # print(words_of_msg)
        #print("\n**********\n")
        if(len(words_of_msg[len(words_of_msg)-1]))>maxLenLastWord:
            maxLenLastWord = (len(words_of_msg[len(words_of_msg)-1]))
        # check every word before the last one as that might be splited
        for j in range(len(words_of_msg)-1):
            #check if the word is found in dict 
            if words_of_msg[j].lower() in words:
                goodwrd+=1
                #print(words_of_msg[j])
    if goodwrd>0:
        goodWordCount[pad]=goodwrd
    #print(goodWordCount)
    #print("max len of last msg wrd"+str(maxLenLastWord))

cipherTextFile.close()
# code to get all possible pads for 0 to 10th position
somelists= possiblePad2[0:10]
allprobablePad=[]
for element in itertools.product(*somelists):
    allprobablePad.append("".join(element))
print(len(allprobablePad))

for i in range(len(allprobablePad)):
    checkMsgWithDictionary(allprobablePad[i])
# get the top pad who have highest msg word 
# corner case : check if top 4-5 values has same count. if no pad has highest
topPad =  sorted(goodWordCount, key=goodWordCount.get, reverse=True)[:1]
print(topPad)
"""
# valid pad which is the ans 
validPad =""


def checkMsgWithDictionary(pad,cipherStartIndex):
    maxLenLastWord=0    # the last word which might be spilited , i.e : "develo" so have to check along with prev 6 msg in next iter
    goodwrd=0
    
    for i in range(cipherCount):
        plaintxt = convert_2_plain(i,cipherStartIndex,cipherStartIndex+len(pad), pad)
        #print(plaintxt)
        words_of_msg = re.split(r"[-!,.?()\s]\s*", plaintxt)
       # print(words_of_msg)
        #print("\n**********\n")
        if(len(words_of_msg[len(words_of_msg)-1]))>maxLenLastWord:
            maxLenLastWord = (len(words_of_msg[len(words_of_msg)-1]))
        # check every word before the last one as that might be splited
        for j in range(len(words_of_msg)-1):
            #check if the word is found in dict 
            if words_of_msg[j].lower() in words:
                goodwrd+=1
                #print(words_of_msg[j],end=" * ")
    #if goodwrd>0:
        #goodWordCount[pad]=goodwrd
    return goodwrd
    #print(goodWordCount)
    #print("max len of last msg wrd"+str(maxLenLastWord))

cipherTextFile.close()
# code to get all possible pads for 0 to 10th position

for padStart in range(0,len(cipherList[0]),10):
    goodWordCount={}
    somelists= possiblePad2[padStart:padStart+10]
    allprobablePad=[]
    for element in itertools.product(*somelists):
        allprobablePad.append("".join(element))
    
    print(str(len(allprobablePad))+" for loop pad start "+str(padStart))
    #checkMsgWithDictionary("rOT1GaGXtN")
    for i in range(len(allprobablePad)):
        goodwrd=checkMsgWithDictionary(allprobablePad[i],padStart)
        goodWordCount[allprobablePad[i]] = goodwrd
        
    # get the top pad who have highest msg word 
    # corner case : check if top 4-5 values has same count. if no pad has highest
    topPad =  sorted(goodWordCount, key=goodWordCount.get, reverse=True)[:8]
    for pad in topPad:
        print(pad+" "+str(goodWordCount[pad]))
    validPad+=topPad[0]

    
print("succss : ")
print("wKt3UqHiLNrOT1GaGXtNqfqWTA37c8kEtinm`nOfyDBbMHpH75h6cGWaDap1")
print(validPad)

print(" retrieved msgs : **********\n\n")
for i in range(cipherCount):
    plaintxt = convert_2_plain(i, 0, len(cipherList[i]), validPad)
    print(plaintxt)
    print("")
"""
***** cheat shit ***

wKt3UqHiLNrOT1GaGXtNqfqWTA37c8kEtinm`nOfyDBbMHpH75h6cGWaDap1


# ***************Tough Part****************
# ******************************************
# ***********Check words in dictionary*****

dict = enchant.Dict("en_US")


def decryption(p, c1, c0):
    message_ascii = c1 ^ ((p + c0) % 256)
    return message_ascii


def checkPadIsOkay(pad):
    goodSentence = 0
    for i in range(10):
        totWord = 0
        goodWord = 0
        message = ""
        for j in range(len(pad)):
            if j == 0:
                char_ascii = decryption(pad[j], cipherTexts[i][j], 0)
            else:
                char_ascii = decryption(
                    pad[j], cipherTexts[i][j], cipherTexts[i][j - 1]
                )
            message += chr(char_ascii)
        splited_msg = re.split(r"[-!,.?()\s]\s*", message)

        # If length of splitted message is one then it is a good word
        # Else we need to check except the last splitted message

        if len(splited_msg) == 1:
            totWord += 1
            goodWord += 1
        else:
            for k in range(len(splited_msg)):
                if splited_msg[k] != "" and k < len(splited_msg) - 1:
                    totWord += 1
                    if dict.check(splited_msg[k]):
                        goodWord += 1

        if (goodWord / totWord) > 0.66:
            goodSentence += 1

    if (goodSentence / 10) < 0.8:
        return False
    # if goodWord / totWord < 0.78:
    #     return False

    return True


# ***********Recursive Backtracking*************
keylist = cipherList[0]
row = i'th  cipher / cipherList[0][i]
def checkValidWords(keyList, row, pad):

    if len(pad) >= len(
        keyList
    ):  # if pad length is greater than 60 that means valid pad is found!
        global key_pad
        key_pad = pad.copy()
        return True

    if row >= len(keyList):  # if row > 60
        return False

    if len(pad) < len(keyList):
        for i in keyList[row]:
            pad.append(i)
            if checkPadIsOkay(pad):
                if checkValidWords(keyList, row + 1, pad):
                    return True
            pad.pop()
    return False
"""