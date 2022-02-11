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
        
        
    We have done all those steps, then we predicted keys for some predicted keylength
    Then we calculated percantage of how much good our prediction for every key
    
        
"""
# importing neccessary libraries
import re ,collections

# get factors of the numbers
def get_factors(repeatLenNumbers):
    x=2
    factorList = []
    for j in range(len(repeatLenNumbers)):
       x=repeatLenNumbers[j] 
       for i in range(2, x + 1):
           if x % i == 0:
               factorList.append(i)
    return factorList


# this will make cipher text to plaintext using predicted ky             
def cypherToPlain(cipherText,key):
    ciphertextLen = len(cipherText)
    j = 0
    convertedplaintext = ""
    chara = ""
    charplain = 0
    keyLen = len(key)
    for i in range(ciphertextLen):
      
       # if keylen reached , start from starting
       if(j==keyLen):
           j=0
       chara = cipherText[i] # ciphertext character   
       if chara==" ":       # if space nothing to do
           continue
       # calculate to plaintext 
       charplain = ((dicti[cipherText[i]]-dicti[key[j]])%52)
       
       # get the plaintext character 
       chara = alphlist[charplain]    
       # add character to olaintext
       convertedplaintext+=chara
       # if 5th char reached, add a space
       if i%5==0:
           convertedplaintext+=" "
       j+=1
    return convertedplaintext


# this function get every n'th character from the cipher text
def get_nth_char_string(n):
    temp=""
    fst_nth=""
    # go to every n'th char from 1
    for i in range(len(cipherTextClean)):
        if i%pred_keylen == n:
            
            temp = cipherTextClean[i]  # get the nth char
            fst_nth+= temp             # add that to string
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
    #print(letter.lower())
    predicted_key = alphlist_lower[(dicti[letter.lower()]-dicti['e'])%26]
    return predicted_key
    

# predict the key
def predict_the_key(pred_keylen):
    predicted_key=""
    for i in range(pred_keylen):
        
        checktxt = get_nth_char_string(i)  # the the cohert with every n'th char
        check_key = predicted_nth_letter(checktxt) # get predicted key char
        #print(check_key) 
        predicted_key+=check_key # get the key
    
    return predicted_key


#print(get_the_plaintxt)

def get_percantage_of_match(get_the_plaintxt,original_plaintxt):
    # clean texts
    get_the_plaintxt = "".join(re.split("[^a-zA-Z]*", get_the_plaintxt)) 
    original_plaintxt = "".join(re.split("[^a-zA-Z]*", original_plaintxt))
    successcount=0
    for  i in range(len(get_the_plaintxt)):
        if get_the_plaintxt[i].lower()==original_plaintxt[i].lower():
            successcount+=1 # if plaintext & predicted plaintext matched, hoilla
        
    print("total matched chars : "+str(successcount )+"\ntotal text chars :"+str(len(get_the_plaintxt))) 
    # return success percantage      
    return (successcount/len(get_the_plaintxt))*100

# FILE NAME

cipherFileName = 'output.txt'
#keyFileName = 'key2.txt'
originaltxtFileName = 'input.txt'

# how many keys to take for prediction
how_many_keys_to_search = 10
# mapping characters

# mapping characters
# dictionary will map as : {A:0, B:1, C:2....., Z:25, a:26,b:27 ...}
# alphlist will map : [A,B,C......Z,a,b,c,..z]
# alphlist_lower will map : [a,b,c,..z]
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

#print(alphlist_lower)


# open files
cipherFile = open(cipherFileName,'r+')
#keyFile = open(keyFileName ,'w+')
original_plaintxtFile = open(originaltxtFileName,'r+')

# read cipher text & original plaintext
cipherText = cipherFile.read()
original_plaintxt = original_plaintxtFile.read()

print("The original plain text file : \n\n")
print(original_plaintxt)

# clean the cipher text 
cipherTextClean = "".join(re.split("[^a-zA-Z]*", cipherText))


# this list will store all the factors




# get repeated sequances & also their repeat distance
seqDistance  = {} # dictionary of seq's distance
repeatedSeq = []  #which seq"s were repeated
repeatLenNumbers = [] # values of distance
numofrepeatation = {} # num of time a seq is repeated

# Repeated sequence lenght within 5 to 8, smaller or greater len string repeatation will be
# ignore, this range can be updated to find more frequent string patter
for repeatLen in range(3,8):
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

# get the factor lists of the distance number
factorList=get_factors(repeatLenNumbers)

# calculate the frequency of the factors 
frequency = collections.Counter(factorList)

# how many keys to take for prediction
how_many_keys_to_search = len(cipherTextClean)

# get most frequent  items

# how many frequent item to be seeen
freq_count =len(frequency)      # number of factors generated
# we will take maximum limited factors here, 
# so if factors are less than that limit, we will take that count
if(freq_count>how_many_keys_to_search):
    freq_count = how_many_keys_to_search
    
    
# get the top frequent factors & create a copy
most_freq_two_list = frequency.most_common(freq_count)
most_freq_two_list2 = frequency.most_common(freq_count)

"""
# NOW if two factors has same frequency , we have to check if 
# those two are each others factor,
# for example, if 2 has frequency =315 & 
#                 4 has frequency =315
# so , 4 is very likely to be our keylenght, as 2 is a factor of 4,
for i in range(freq_count):
    # if it is 2nd item   
    if i>0:
        # if current & previous has same freq count
        if most_freq_two_list[i][1] == most_freq_two_list[i-1][1]:
            # check if two are each others factor
            if most_freq_two_list[i][0]%most_freq_two_list[i-1][0]==0:
                # ignore first one
                
                most_freq_two_list2.remove( most_freq_two_list[i-1]) 


"""
print("predicted key lens ( max "+str(how_many_keys_to_search)+" key lengths):")
for i in range(len(most_freq_two_list2)):
    print(most_freq_two_list2[i][0])     

# keylen prediction completed 



# max percantage
max_percant =-99
max_percant_i = 0
cur_percant = 0;
# loop for every possible key len to predict key & get success percantage of predicting plaintext
for i in range(len(most_freq_two_list2)):
    pred_keylen = most_freq_two_list2[i][0] # get i'th keylen
    predicted_key = predict_the_key(pred_keylen) # predict the key
    print("\n\nPredicted Key : "+predicted_key)
    get_the_plaintxt = cypherToPlain(cipherTextClean, predicted_key) 
    
    print("for length : "+str(pred_keylen))
    print("\n")
    print(get_the_plaintxt)
    cur_percant = get_percantage_of_match(get_the_plaintxt,original_plaintxt)
    print("success rate: " +str(cur_percant)+" %")           
    print("\n\n *************  ***********  *******\n\n\n")
    
    if cur_percant>=max_percant:
        max_percant_i = i
        max_percant = cur_percant


#print("\n\n******** ans : *********")
pred_keylen = most_freq_two_list2[max_percant_i][0] # get i'th keylen
predicted_key = predict_the_key(pred_keylen) # predict the key
print("\n\nPredicted Key : "+predicted_key)
get_the_plaintxt = cypherToPlain(cipherTextClean, predicted_key) 

print("for length : "+str(pred_keylen))
print("\n")
print(get_the_plaintxt)
cur_percant = get_percantage_of_match(get_the_plaintxt,original_plaintxt)
print("success rate: " +str(cur_percant)+" %")           


# close the file
cipherFile.close()
original_plaintxtFile.close()
#keyFile.close()
    