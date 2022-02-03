# -*- coding: utf-8 -*-
"""


@author: 

Zulker Nayeen

Roll- FH-11
4th year 1st Semester

Course : Cryptography & Security Lab

Labwork : Cryptoanalysis & Cracking Vigenere cipher 

Brief discussion : 
    
    Vigenre cipher was thought to be uncrackable. however, Kasiski showed a method to crack this.
    
    The kasiski method is as follows : 
        1. first find repeated
"""
import re,math ,collections,statistics,itertools

# FILE NAME
plaintextFileName = 'plaintext2.txt'
cipherFileName = 'cyphertext2.txt'
keyFileName = 'key2.txt'

# mapping characters
chara = 'B'
i = 0
dicti = {'A':i}
alphlist = ['A']
alphlist_lower = []
for i in range(25):
    dicti.update({chr(ord(chara)+i):i+1})
    alphlist.append(chr(ord(chara)+i))
chara = 'a'
for i in range(26):
    dicti.update({chr(ord(chara)+i):i+26})
    alphlist.append(chr(ord(chara)+i))
    alphlist_lower.append(chr(ord(chara)+i))
#print(dicti)
#print(alphlist)
"""
alphlist = ['a']
chara = 'a'
for i in range(25):
    alphlist.append(chr(ord(chara)+i+1))
print(alphlist)
"""
# open files
cipherFile = open(cipherFileName,'r+')
plainFile = open(plaintextFileName,'w+')
keyFile = open(keyFileName ,'r+')

# read cipher text
cipherText = cipherFile.read()

# clean the cipher text & also make it uppercase
cipherTextClean = "".join(re.split("[^a-zA-Z]*", cipherText))
#cipherTextClean = cipherTextClean.upper()
#print(cipherTextClean)

factorList = []
# get factors of the numbers
def get_factors(repeatLenNumbers):
    x=2
    for j in range(len(repeatLenNumbers)):
       x=repeatLenNumbers[j] 
       for i in range(2, x + 1):
           if x % i == 0:
               factorList.append(i)
    return factorList


def cypherToPlainLetter(cipherText,key):
    ciphertextLen = len(cipherText)
    j = 0
    convertedplaintext = ""
    chara = ""
    charplain = 0
    #keyLen = len(key)
    for i in range(ciphertextLen):
       #print(plaintextClean[i])
       
       chara = cipherText[i]    
       if chara==" ":
           continue
       charplain = ((dicti[cipherText[i]]-dicti[key])%52)
       """
       if(chara.isupper()):
           charplain+=ord('A')
       else :
           charplain+=ord('a')
    """
       chara = alphlist[charplain]    
       convertedplaintext+=chara
       
       
    return convertedplaintext

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
"""
for i in range(len(repeatedSeq)):
    print(str(repeatedSeq[i])+" = "+str(seqDistance[repeatedSeq[i]]))
print()   
"""
#print(str(seqDistance))

# sort the repeat seqs based on how many times they were repeated
"""
a = sorted(numofrepeatation.items(), key=lambda x: x[1])
print(str(a[len(numofrepeatation)-1]))
print(str(a[len(numofrepeatation)-2]))
print(a[len(numofrepeatation)-1][0])
# get the highest repeated seq
targetSeq = a[len(numofrepeatation)-1][0]
# print the gcd of highest repeated seq which is the predicted key
print(math.gcd(*seqDistance[targetSeq]))
"""
print()
get_factors(repeatLenNumbers)
"""

res = max(set(factorList), key = factorList.count)
res2 = statistics.mode(factorList)
print("\n\n"+str(res)+"\n\n")
"""
frequency = collections.Counter(factorList)

#print(frequency)
"""
# predicted length 
# first 4 items of the frequency dictionary
freq_items = frequency.items()
most_freq_four = list(freq_items)[:4] # get most frq 4 as list

most_freq_four_dict = dict(itertools.islice(frequency.items(), 5)) # get most freq 4 as dict
# sort the first 4 items based on their freq
most_freq_four_sorted = sorted(most_freq_four_dict.items(), key=lambda x: x[1],reverse=True)
most_freq_four_sorted2 = sorted(most_freq_four_dict.items(), key=lambda x: x[1],reverse=True)
print(most_freq_four_sorted)

print(" predicted key lens ( max 4 key lens):")
for i in range(len(most_freq_four_sorted)):
    print(most_freq_four_sorted[i][0])
    #print("loop for i = "+str(i))
    
most_freq_four_sorted_len = len(most_freq_four_sorted) 
#most_freq_four_sorted2 = most_freq_four_sorted
print(most_freq_four_sorted[3][1])
for i in range(most_freq_four_sorted_len):
    #print(most_freq_four_sorted[i][0])
    if i>0:
        # NOW if two factors has same frequency , we have to check if 
        # those two are each others factor
        print("lenght for "+str(len(most_freq_four_sorted)))
        print("checking "+str(most_freq_four_sorted[i][1])+" & "+str(most_freq_four_sorted[i-1][1]))
        if most_freq_four_sorted[i][1] == most_freq_four_sorted[i-1][1]:
            # check if two are each others factor
            if most_freq_four_sorted[i][0]%most_freq_four_sorted[i-1][0]==0:
                # ignore first one
                print("poppping")
                most_freq_four_sorted2.pop( most_freq_four_sorted[i-1][0])

print(most_freq_four_sorted2)
               
most_freq_two_dict = dict(itertools.islice(frequency.items(), 2)) # get most freq 4 as dict
print(most_freq_two_dict)
most_freq_two_list = [(k, v) for k, v in most_freq_two_dict.items()]
print(most_freq_two_list)
if most_freq_two_list[0][1] == most_freq_two_list[1][1]:
    # check if two are each others factor
    if most_freq_two_list[1][0]%most_freq_two_list[0][0]==0:
        # ignore first one
        print("poppping")
        most_freq_two_list.remove( most_freq_two_list[0]) 
           
print(most_freq_two_list)
"""
# get most frequent 4 items
most_freq_two_list = frequency.most_common(4)
most_freq_two_list2 = frequency.most_common(4)

# NOW if two factors has same frequency , we have to check if 
# those two are each others factor
for i in range(4):
   # print("checking "+str(most_freq_two_list[i][1])+" & "+str(most_freq_two_list[i-1][1]))
    
    if most_freq_two_list[i][1] == most_freq_two_list[i-1][1]:
        # check if two are each others factor
        if most_freq_two_list[i][0]%most_freq_two_list[i-1][0]==0:
            # ignore first one
            #print("poppping")
            most_freq_two_list2.remove( most_freq_two_list[i-1]) 


#print(most_freq_two_list2)
print(" predicted key lens ( max 4 key lens):")
for i in range(len(most_freq_two_list2)):
    print(most_freq_two_list2[i][0])     

# keylen prediction completed 

pred_keylen =   most_freq_two_list2[0][0]
fst_nth = ""

def get_nth_char_string(n):
    temp=""
    fst_nth=""
    for i in range(len(cipherTextClean)):
        if i%pred_keylen == n:
            #print(i)
            temp = cipherTextClean[i]
            fst_nth+= temp
    return fst_nth

def predicted_nth_letter(fst_nth):
    fstfreq = collections.Counter(fst_nth)
    most_commonn_letter = fstfreq.most_common(1)
    print(most_commonn_letter) 
    letter = most_commonn_letter[0][0]
    predicted_key = alphlist_lower[(dicti[letter.lower()]-dicti['e'])%52]
    return predicted_key
    
"""        
for keyLetter in alphlist_lower:
    decryptedmsg = cypherToPlainLetter(fst_nth, keyLetter)
"""
# get frequency of char in that string
"""
fstfreq = collections.Counter(fst_nth)
most_commonn_letter = fstfreq.most_common(1)
print(most_commonn_letter)
"""
predicted_key=""
for i in range(pred_keylen):
    checktxt = get_nth_char_string(i)
    check_key = predicted_nth_letter(checktxt)
    print(check_key) 
    predicted_key+=check_key
print(predicted_key)
cipherFile.close()
plainFile.close()
keyFile.close()
    