# -*- coding: utf-8 -*-
"""
Created on Sat Feb 12 19:19:27 2022

@author: User
"""
import json,numpy as np,re,itertools,heapq



# get the possible pad for 2nd to last position 
def getPossiblePadForEveryPosition():
    for k in range(1,len(cipherList[0])): # k is the k'th char of i'th cipher
        possiblePad = "" 
        possibleMsg =""
        for j in range(256): # j is the possible pad
            wrongPadFlag=False  #flag will indicate if the pad is wrong 
            for i in range(cipherCount):# loop through all 10 ciphertexts
                possPadInt = cipherList[i][k]^((cipherList[i][k-1]+j)%256)  #  get first msg int value
                
                if chr(possPadInt) in alphSet: # if first msg character is valid alphabet
                    possibleMsg+=chr(possPadInt) # add it to possible messsage
                    continue                    # continue to next ciphertext list
                else:
                    wrongPadFlag=True  # if invalid char
                    possibleMsg="" # no possible msg
                    break #break loop
            if wrongPadFlag==False: # if it is not wrong pad, not invalid character in any first position 
                                    # of the list of ciphertexts
                possiblePad+=chr(j) # add this as a possible pad
        
        # append the possible pad for k'th position
        possiblePad2.append(possiblePad)
  
#get plaintext
def convert_2_plain(cipherNo,cipherStartIndex,cipherEndIndex,pad):
    plaintxt=""
    j=0
    for i in range(cipherStartIndex,cipherEndIndex):  # loop from start posi to end posit
        
        if i==0:  # 0th position decrytpion
            plaintxt+=chr(cipherList[cipherNo][i]^ord(pad[j]))
        else:
            #other than zeroth position decryption
            possPadInt = cipherList[cipherNo][i]^(((cipherList[cipherNo][i-1]+ord(pad[j]))%256))
            # get the plain text
            plaintxt+=chr(possPadInt)
        j+=1    
    return plaintxt


# get the plain text & get the word from it, then check for valid word set
# maximum valid word set provider is the probable pad
def checkMsgWithDictionary(pad,cipherStartIndex):
    maxLenLastWord=0    # the last word which might be spilited , i.e : "develo" so have to check along with prev 6 msg in next iter
    goodwrd=0
    
    for i in range(cipherCount):
        # get the plain text
        plaintxt = convert_2_plain(i,cipherStartIndex,cipherStartIndex+len(pad), pad)
        # get list of words, splited by , space , ? or ther non alphabetic char
        words_of_msg = re.split(r"[-!,.?()\s]\s*", plaintxt)
        if(len(words_of_msg[len(words_of_msg)-1]))>maxLenLastWord:
            maxLenLastWord = (len(words_of_msg[len(words_of_msg)-1]))
        
        # check every word before the last one as that might be splited
        for j in range(len(words_of_msg)-1):
            #check if the word is found in dict 
            if words_of_msg[j].lower() in words:
                goodwrd+=1
                # found a good word , adding it to count
    """
    # if no good word found, we should not add this as a pad
    if goodwrd>0:
        goodWordCount[pad]=goodwrd
        """
        # return the count of good words
    return goodwrd
# check if a character is valid, i .e belong to the english dictionary
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
#

# possible pad for 0 th position
def possiblePadForZerothPosi():
    # possible pad for 0th position
    possibleMsg=""
    possiblePad=""
    for j in range(256):
        wrongPadFlag=False #flag will indicate if the pad is wrong 
        for i in range(cipherCount):    # loop through all 10 ciphertexts
            cipherInt = cipherList[i][0]^j  # xor & get first msg int value
            if chr(cipherInt) in alphSet:  # if first msg character is valid alphabet
                possibleMsg+=chr(cipherInt) # add it to possible messsage
                continue                    # continue to next ciphertext list
            else:
                wrongPadFlag=True  # if invalid char
                possibleMsg=""      # no possible msg
                break             #break loop
        if wrongPadFlag==False:  # if it is not wrong pad, not invalid character in any first position 
                                # of the list of ciphertexts
            possiblePad+=chr(j) # add this as a possible pad
    possiblePad2.append(possiblePad)  # we get the possible pad list for first possition
 
# open the cipher text file & word file
cipherTextFileName = "Ciphertext_Assignment_2.txt"
cipherTextFile = open(cipherTextFileName,"r+")
wordFileName = "word_from_ubuntu.txt"

wordFile = open(wordFileName,"r")
cipherList = []
#retrieve the words
words=set()
cipherCount = 0
i=0

tmpstr = ""
#valid characterlist
validChar = [" ",",","(",")"]
alphlist = ['A']
alphSet  = {'A'}

#read & get words :
def getWordsFromFile():
    for line in wordFile:
        tmpstr = line       #get the line from txt
        
        
        # readline adds an extra newline end of the word, so cut it
        tmpstr = tmpstr[0:-1]
        # if it is one char word, then ignore it, it;s just a char
        if len(tmpstr)<=1:
            continue
        tmpstr.lower() # get lowercase for max match
        
        # add word to dictionary
        words.add(tmpstr)
    # add ' a' as a word
    words.add("a")

def readCipherFile():
    cipherCount = 0
    for lines in cipherTextFile:
        tmpstr = lines           #load the line
        tmpstr = lines[0:-1]     # delete newline from end
        cipherCount+=1
        # make the list string to list obj
        cipherList.append(json.loads(tmpstr))
    return cipherCount 

def getValidAlphSet():
    alphSet.add(" ")
    alphSet.add(",")
    alphSet.add("(")
    alphSet.add(")")
    alphSet.add(".")
    alphSet.add("?")
    alphSet.add("-")
    alphSet.add("!")

    # alphset contains all valid char list
    # filling the alphset with capital letter
    chara = 'A'
    for i in range(26):
        alphlist.append(chr(ord(chara)+i))
        alphSet.add(chr(ord(chara)+i))
        
    #filling alphset with small letter
    chara = 'a'
    alphSet.add('a')
    for i in range(26):
        alphlist.append(chr(ord(chara)+i))
        alphSet.add(chr(ord(chara)+i))

        
"""
A-Z : 65-90
a-z : 97-122
space : 32
comma : 44
(   : 41
) : 42

"""

# get the valid alphabet sets
getValidAlphSet()

# read the cipher text file & store in a list 

cipherCount = readCipherFile()  # counts how many cipher texts
# get words from file
getWordsFromFile()
# valid char lists



possiblePad2 = [] # list of all possible pad list for each position
possibleMsg2 = [] # list of all possible msg list for each position

#get possible pad for zeroth positon
possiblePadForZerothPosi()
"""
calculation to get the pad :

ci = mi ^ (c[i-1]+pi)%256
ci^mi =  (c[i-1]+pi)%256 ; xor both side with mi
pi%256  = (ci^mi-c[i-1])%256

mi = (c[i-1]+pi)%256) ^ ci
    



"""
      
# function call to get probable pad list
getPossiblePadForEveryPosition()   

print(possiblePad2)

# get the ciphertext from the cipher list int value



# valid pad which is the ans 
validPad =""
    
# close the cipher text file
cipherTextFile.close()
# code to get all possible pads for 0 to 15th position

for padStart in range(0,len(cipherList[0]),15):
    goodWordCount={}  # dictionary to store probable pad with good word count: {"waserwaqet":10}
    # get 15 pads
    somelists= possiblePad2[padStart:padStart+15]
    allprobablePad=[]
    # get all possible pad list
    for element in itertools.product(*somelists):
        allprobablePad.append("".join(element))
    
    print(str(len(allprobablePad))+" for loop pad start "+str(padStart))
    # get plaintext & check which pad is most probable, chekc of all possible pads
    for i in range(len(allprobablePad)):
        goodwrd=checkMsgWithDictionary(allprobablePad[i],padStart)
        goodWordCount[allprobablePad[i]] = goodwrd  # store in dictionary
        
    # get the top pad who have highest msg word 
    topPad =  sorted(goodWordCount, key=goodWordCount.get, reverse=True)[:8]
    for pad in topPad:
        print(pad+" "+str(goodWordCount[pad]))
    # get the valid pad
    validPad+=topPad[0]

# pad found success    
print("succss : ")
print("wKt3UqHiLNrOT1GaGXtNqfqWTA37c8kEtinm`nOfyDBbMHpH75h6cGWaDap1")
print(validPad)

# retrieve the msg text
print(" retrieved msgs : **********\n\n")
for i in range(cipherCount):
    plaintxt = convert_2_plain(i, 0, len(cipherList[i]), validPad)
    print(plaintxt)
    print("")
