# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 00:26:00 2022

@author: User
"""
import re,math 

# FILE NAME
plaintextFileName = 'plaintext2.txt'
cipherFileName = 'cyphertext2.txt'
keyFileName = 'key2.txt'

# open files
cipherFile = open(cipherFileName,'r+')
plainFile = open(plaintextFileName,'w+')
keyFile = open(keyFileName ,'r+')

# read cipher text
cipherText = cipherFile.read()

# clean the cipher text & also make it uppercase
cipherTextClean = "".join(re.split("[^a-zA-Z]*", cipherText))
cipherTextClean = cipherTextClean.upper()
print(cipherTextClean)

# get factors of the numbers
def get_factors(x):
   factorList = []
   for i in range(2, x + 1):
       if x % i == 0:
           factorList.append(i)
   return factorList

# get repeated sequances & also their repeat distance
seqDistance  = {} # dictionary of seq's distance
repeatedSeq = []  #which seq"s were repeated
repeatLenNumbers = [] # values of distance
numofrepeatation = {} # num of time a seq is repeated
for repeatLen in range(5,8):
    for strStart in range(len(cipherTextClean)-repeatLen):
        #get the targetted sequence
        targetSeq = cipherTextClean[strStart:strStart+repeatLen]
        
        # search for the sequence if repeated
        for i in range(strStart+repeatLen,len(cipherTextClean)-repeatLen):
            
            testSeq = cipherTextClean[i:i+repeatLen]
            # if repeat found
            if testSeq == targetSeq :
                # if no entry for targetseq
                if testSeq not in seqDistance:
                    seqDistance[testSeq] = []
                    repeatedSeq.append(testSeq)
                #save the distance of the target seq    
                seqDistance[testSeq].append(i-strStart)
                # save the distance value for factor calculation
                repeatLenNumbers.append(i-strStart)
        # get number of repeatations of any sequances
        if targetSeq in seqDistance:
             numofrepeatation[targetSeq]=len(seqDistance[targetSeq])
# print the sequences with their repeat distance             
for i in range(len(repeatedSeq)):
    print(str(repeatedSeq[i])+" = "+str(seqDistance[repeatedSeq[i]]))
print()   
#print(str(seqDistance))

# sort the repeat seqs based on how many times they were repeated
a = sorted(numofrepeatation.items(), key=lambda x: x[1])
print(str(a[len(numofrepeatation)-1]))
print(str(a[len(numofrepeatation)-2]))
print(a[len(numofrepeatation)-1][0])
# get the highest repeated seq
targetSeq = a[len(numofrepeatation)-1][0]
# print the gcd of highest repeated seq which is the predicted key
print(math.gcd(*seqDistance[targetSeq]))



# predicted length : 
    
cipherFile.close()
plainFile.close()
keyFile.close()
    