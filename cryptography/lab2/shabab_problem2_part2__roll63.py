# Shabab Murshed SH-63
############################        #######################################################         ######################################
## part 2
################     ######################         ###########################       ########################################################

import itertools

#function to convert ascii to its char or string
def asciiToString(ascii_lst):
    str =''.join(chr(a) for a in ascii_lst)

    return str

cyphers = []
with open("Ciphertext_Assignment_2.txt") as f:
    for line in f:
        temp_cypher = []
        temp_cypher = [line.rstrip('\n')]  # each line is treated as a string
        temp_cypher[0] = temp_cypher[0].replace('[', '')  # removing [ from the string
        temp_cypher[0] = temp_cypher[0].replace(']', '')  # removing ] from the string
        temp_cypher = list(map(int, temp_cypher[0].split(',')))  # converting the string to a list of 60 numbers
        cyphers.append(temp_cypher)  # all 10 cyphers appending one by one
print("All the Cyphers in ASCII value is")
print(cyphers)
# print("Cyphertexts are")
# for i in range(len(cyphers)):
#     i = 5
#     a = asciiToString(cyphers[i])
#     print(f'Cyphertext {i+1} is: {a}')
print()


#the messagetext must be of the 60 valid characters
#which are *** a – z   A – Z   space   ,  .  ?  !  -  (  )  #97-122 65-90 32 44 46 63 33 45 40 41
#checks if the messagechar generated is a valid one
def validPlainTextChar(chr_ascii):
    chr_pTxt = chr(chr_ascii)
    # print(chr_pTxt)

    if 'a' <= chr_pTxt <= 'z' or 'A' <= chr_pTxt <= 'Z' or chr_pTxt == ' ' or chr_pTxt == ',' or chr_pTxt == '.' or chr_pTxt == '?' or chr_pTxt == '!' or chr_pTxt == '-' or chr_pTxt == '(' or chr_pTxt == ')':
        return 1
    else:
        return 0

#decryption using mi = ci ⊕ ((pi + ci−1 ) mod 256)
def decryption(index, cph_i, cphi_1, pad_i):
    possible_m_i = 0
    if index == 0:
        possible_m_i = cph_i ^ pad_i  #for the first position ci-1 = 0
    else:
        possible_m_i = cph_i ^ ((pad_i + cphi_1) % 256)  # mi = ci ⊕ ((pi + ci−1 ) mod 256)
    return possible_m_i


all_pos_possible_keychars = []
for i in range(len(cyphers[0])):  # iterates all 60 position of the cyphers
    ith_pos_possible_keychars = []
    for p in range(256):  # possible pad characters for ith position
        cnt = 0
        for j in range(len(cyphers)):  # iterates all 10 cyphers one by pne
            possible_m_i = 0
            if i == 0:
                possible_m_i = decryption(i, cyphers[j][i], 0, p)
            else:
                possible_m_i = decryption(i, cyphers[j][i], cyphers[j][i - 1], p)
            if validPlainTextChar(possible_m_i):
                cnt += 1
        if cnt == len(cyphers): #if all the 10 cyphers in the ith position gives valid message char for the keychar 'p' then the keychar 'p' is valid for that position i
            ith_pos_possible_keychars.append(p)
    all_pos_possible_keychars.append(ith_pos_possible_keychars)
print()
print("Possible key characters in ASCII value")
print(all_pos_possible_keychars)
print()
print("Possible key characters in")
for i in range(len(all_pos_possible_keychars)):
    a = ','.join(asciiToString(all_pos_possible_keychars[i]))
    print(f'{i+1}position is: {a}')
print()
# mul = 1
# for i in range(len(cyphers[0])):
#     print((all_pos_possible_keychars[i]))
#     mul *= len(all_pos_possible_keychars[i])
#     print(mul)

words =[]
with open("word_from_ubuntu.txt") as f: #The shortlist_dict.txt was continuosly updated by checking the output in the terminal by making guesswork on the half or almost full gibberish words
    words = [(line.rstrip('\n')) for line in f]
len_slice = 15 # size of each slice
possible_pad = []
iteration_no = 1
for start in range(0,60,10):

    if start == 50: #the last slice is of length 10
        len_slice = 10
    print(f'Iteration no: {iteration_no}')
    print(f'Slice starts from {start+1} to {start+len_slice} position')

    slice = all_pos_possible_keychars[start:start + len_slice] #taking a slice of the possible pad position chars
    mx_meaningful_count = 0
    possible_pad_slice = []
    for pad in itertools.product(*slice): #all cartesian product values of the elements within each position of the slice
        # print(pad[58])
        meaningful_word_cnt = 0 #keeps count of the meaningful words from all the 10 message slices using 'pad'

        for k in range(len(cyphers)): #iterating the 10 cyphers
            message_ith = []
            for i in range(len_slice):
                if i == 0 and start == 0: # the first position of the cypher
                    message_ith.append(decryption(start, cyphers[k][i+ start], 0, pad[i]))
                elif i != 0 and start == 0: # the other position of the cyphers
                    message_ith.append(decryption(i, cyphers[k][i + start], cyphers[k][i - 1 + start], pad[i]))
                else: # the other position of the cyphers
                    message_ith.append(decryption(start, cyphers[k][i + start], cyphers[k][i - 1 + start], pad[i]))
            message_ith_string = (asciiToString(message_ith))
            #print(message_ith_string)
            for wrd in words:
                if message_ith_string.find(wrd) != -1: #the message slice has the word 'wrd'
                    meaningful_word_cnt += 1  ##three letter words matched

        if meaningful_word_cnt > mx_meaningful_count: #pad slice which gives the highest meaningful word is a probable pad slice
            mx_meaningful_count = meaningful_word_cnt
            possible_pad_slice.append(pad)


    #print(possible_pad_slice1)
    pad_sliced = []
    print(f'Possible pad for the slice is {possible_pad_slice[len(possible_pad_slice) - 1]}')
    pad_sliced = possible_pad_slice[len(possible_pad_slice) - 1]  #the best guessed pad slice was appended at the last

    possible_pad.extend(pad_sliced[0:10]) #attaching the first 10characters of the padslice in the combined pad slice

    #printing all the 10message slices using the best guessed pad slice
    print(f'Possible message of the slice is:')
    for k in range(len(cyphers)):
        message_ith = []
        for i in range(len_slice):
            if i == 0 and start == 0:
                message_ith.append(decryption(start, cyphers[k][i + start], 0, pad_sliced[i]))
            elif i != 0 and start == 0:
                message_ith.append(decryption(i, cyphers[k][i + start], cyphers[k][i - 1 + start], pad_sliced[i]))
            else:
                message_ith.append(decryption(start, cyphers[k][i+ start], cyphers[k][i - 1+ start], pad_sliced[i]))
        print(f'Message {k+1}: {asciiToString(message_ith)}')
        #print(asciiToString(message_ith))
    iteration_no += 1
    print()
    print()

print("**********************************************************************************************************************************************************************************************************************************************************************************")
print()
print("Possible pad in ASCII value is:")
print(possible_pad)
print()
print("Possible pad is:")
print(asciiToString(possible_pad))
print()

for k in range(len(cyphers)):
    message_ith = []
    for i in range(60):
        if i == 0:
            message_ith.append(decryption(i, cyphers[k][i], 0, possible_pad[i]))
        else:
            message_ith.append(decryption(i, cyphers[k][i], cyphers[k][i - 1], possible_pad[i]))
    print(f'Possible message {k+1} is: {asciiToString(message_ith)}')




