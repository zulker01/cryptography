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
        1. first find repeated string pattern in the cipher text & note down their distance of 
        repeatation
        
        2. then factorize the distance number & store the factors
        3. the factors which has appeared most frequently might be the key length
        4. if we have found the key length, then we will try to decrypt
        6. for example if the key len is 4, we will collect every 4th character of the cipher,
        then predict the plain text with monoalphabatic cipher's cryptoanalysis. i.e replace 
        the most frequent letter with the most frequent alphabet in English. 
        7. we will then find the key . then predict the plain text 
        
"""
# importing neccessary libraries
import re,math ,collections,statistics,itertools

# FILE NAME
plaintextFileName = 'plaintext2.txt'
cipherFileName = 'cyphertext3.txt'
keyFileName = 'key2.txt'
originaltxtFileName = 'original_plaintxt.txt'
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
original_plaintxtFile = open(originaltxtFileName,'r+')
# read cipher text
cipherText = cipherFile.read()
original_plaintxt = original_plaintxtFile.read()
#print(original_plaintxt)
# clean the cipher text & also make it uppercase
cipherTextClean = "".join(re.split("[^a-zA-Z]*", cipherText))
#cipherTextClean = cipherTextClean.upper()
#print(cipherTextClean)

# this list will store all the factors
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



# get repeated sequances & also their repeat distance
seqDistance  = {} # dictionary of seq's distance
repeatedSeq = []  #which seq"s were repeated
repeatLenNumbers = [] # values of distance
numofrepeatation = {} # num of time a seq is repeated

# Repeated sequence lenght within 5 to 8, smaller or greater len string repeatation will be
# ignore, this range can be updated to find more frequent string patter
for repeatLen in range(5,8):
    # loop for every char in cipher text
    for strStart in range(len(cipherTextClean)-repeatLen):
        #get the targetted sequence
        targetSeq = cipherTextClean[strStart:strStart+repeatLen]
        
        # search for the sequence if repeated
        for i in range(strStart+repeatLen,len(cipherTextClean)-repeatLen):
            
            # string seq which to be tested
            testSeq = cipherTextClean[i:i+repeatLen]
            # if repeat found
            if testSeq == targetSeq :
                # if no entry for targetseq
                if testSeq not in seqDistance:
                    seqDistance[testSeq] = []
                    repeatedSeq.append(testSeq) # store the frequent string
                #save the distance of the target seq    
                seqDistance[testSeq].append(i-strStart)
                # save the distance value for factor calculation
                repeatLenNumbers.append(i-strStart)
        # get number of repeatations of any sequances
        if targetSeq in seqDistance:
             numofrepeatation[targetSeq]=len(seqDistance[targetSeq])
             
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
       if i%5==0:
           convertedplaintext+=" "
       j+=1
    return convertedplaintext
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
# get the factor lists of the distance number
get_factors(repeatLenNumbers)
"""

res = max(set(factorList), key = factorList.count)
res2 = statistics.mode(factorList)
print("\n\n"+str(res)+"\n\n")
"""
# calculate the frequency of the factors 
frequency = collections.Counter(factorList)


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
# get most frequent  items

# how many frequent item to be seeen
freq_count =len(frequency)      # number of factors generated
# we will take maximum 4 factors here, 
# so if factors are less than 4, we will take that count
if(freq_count>4):
    freq_count = 4
    
    
# get the top frequent factors & create a copy
most_freq_two_list = frequency.most_common(freq_count)
most_freq_two_list2 = frequency.most_common(freq_count)

# NOW if two factors has same frequency , we have to check if 
# those two are each others factor
for i in range(freq_count):
   # print("checking "+str(most_freq_two_list[i][1])+" & "+str(most_freq_two_list[i-1][1]))
    if i>0:
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

#pred_keylen =   most_freq_two_list2[0][0]
pred_keylen = 6
fst_nth = ""

# this function get every n'th character from the cipher text
def get_nth_char_string(n):
    temp=""
    fst_nth=""
    for i in range(len(cipherTextClean)):
        if i%pred_keylen == n:
            #print(i)
            temp = cipherTextClean[i]
            fst_nth+= temp
    return fst_nth

# this function predicts the key's nth character
def predicted_nth_letter(fst_nth):
    # count frequency of the characters
    fstfreq = collections.Counter(fst_nth)
    # get the most frequent one
    most_commonn_letter = fstfreq.most_common(1)
    #print(most_commonn_letter) 
    # get the most common letter
    letter = most_commonn_letter[0][0]
    # predict the key letter assuming the most common letter is 'e'
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

# predict the key
predicted_key=""
for i in range(pred_keylen):
    checktxt = get_nth_char_string(i)
    check_key = predicted_nth_letter(checktxt)
    print(check_key) 
    predicted_key+=check_key
print(predicted_key)


get_the_plaintxt = cypherToPlain(cipherTextClean, predicted_key)

#print(get_the_plaintxt)

def get_percantage_of_match(get_the_plaintxt,original_plaintxt):
    get_the_plaintxt = "".join(re.split("[^a-zA-Z]*", get_the_plaintxt)) 
    original_plaintxt = "".join(re.split("[^a-zA-Z]*", original_plaintxt))
    successcount=0
    print("original file len"+str(len(original_plaintxt))+"ciphered file len"+str(len(get_the_plaintxt)))
    for  i in range(len(get_the_plaintxt)):
        #print("check "+get_the_plaintxt[i].lower()+" "+original_plaintxt[i].lower())
        if get_the_plaintxt[i].lower()==original_plaintxt[i].lower():
            successcount+=1
        
    print(successcount )       
    return (successcount/len(get_the_plaintxt))*100
print(get_percantage_of_match(get_the_plaintxt,original_plaintxt))            
# close the file
cipherFile.close()
plainFile.close()
keyFile.close()
    