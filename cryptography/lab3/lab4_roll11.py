# -*- coding: utf-8 -*-
"""
Name : Zulker Nayeen
Roll : FH-11
Lab assignment : 4  : AES enrcryption algorithm

key expansion :

    1.         RotWord performs a one-byte circular left shift on a word. This means that an input word [B0, B1, B2, B3] is transformed into [B1, B2, B3, B0].

2.         SubWord performs a byte substitution on each byte of its input word, using the S-box (Table 5.2a).

3.         The result of steps 1 and 2 is XORed with a round constant, Rcon[j].

AES encryption :
1. shift row, 2, substitute byte 3. mix column, 4 add round

"""
from collections import deque
# the irreversitble polymar to mod for galois field 2^8
irrpoly = "100011011"

# substitution box
s_box = [
    [0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76],
    [0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0],
    [0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15],
    [0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75],
    [0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84],
    [0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF],
    [0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8],
    [0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2],
    [0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73],
    [0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB],
    [0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79],
    [0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08],
    [0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A],
    [0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E],
    [0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF],
    [0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16],
]



# galois field

import itertools


# compares 2 binary string , by converting them to int,
# if 1st is big then retunr 1, 2nd big return -1 , same if zero
def compare2values(str1, str2):
    # if dividend out of bound of 256
    if int(str1, 2) > 255:
        return 1
    if int(str1, 2) > int(str2, 2):

        return 1
    elif int(str1, 2) < int(str2, 2):
        return -1
    else:
        return 0

# divide the 2 binary strings
def division(dividend,divisor):
    
    if len(divisor)<8:
        tmpstr = ""
        for i in range(8-len(divisor)):
            tmpstr+="0"
        divisor = tmpstr+divisor
    # get the multiplicative inverse, then multiply them & mod
    mulInverseofDivisor = multInverseDict[divisor]
    return multiply(dividend, mulInverseofDivisor)
    
def getAllPossible8bitString():
    
    # possible bit for every position
    possiblebit = ["01","01","01","01","01","01","01","01"]
    
    global allpossibleBitString
    allpossibleBitString=[]
    
    # get all possible binary  list
    for element in itertools.product(*possiblebit):
        currentBin = "".join(element)
        
        allpossibleBitString.append(currentBin)
        
    #print(" all p ossible Len "+str(len(allpossibleBitString)))
    
def calculateMulInverse():
    global multInverseDict
    multInverseDict = {}
    for i in range(256):
        #if i>3: break
        for j in range(256):
            # if we got its mod inverse, continue
            if allpossibleBitString[i] in multInverseDict:
                continue
            multAns = multiply(allpossibleBitString[i], allpossibleBitString[j])
            #print(multAns+" int : "+str(int(multAns,2)))
            #if j>4: break
            if int(multAns,2)==1:
                multInverseDict[allpossibleBitString[i]] = allpossibleBitString[j]
                multInverseDict[allpossibleBitString[j]] = allpossibleBitString[i]
                #print("inverse found : "+allpossibleBitString[i]+ "   ->   "+allpossibleBitString[j])
    #print("multinver : "+str(len(multInverseDict)))            


# function to get mod / reminder
def mod(moddivi, moddivisor):
    modans = 0b00  # ans after mod opertation / reminder
    i = 1
    # print("ans = "+str(modans)+" divisor = "+moddivisor+ " dividend = "+moddivi)
    # if divisor is already big , return ans
    if compare2values(moddivi, moddivisor) == -1:
        # print("return do nothing ans = "+str(modans)+" divisor = "+moddivisor+ " dividend = "+moddivi)
        return moddivi
    while (compare2values(moddivi, moddivisor) != -1):
        # if both string has same len, then div ans append 1
        # and direct mod with the divisor & dividend ,
        # print("ans = "+str(modans)+" divisor = "+moddivisor+ " dividend = "+moddivi)
        if len(moddivi) == len(moddivisor):

            tmpmodans = 0b1
            modans = tmpmodans + modans
            moddivi = xorStrings(moddivi, moddivisor)
            # print("inside if : tmpans = "+str(tmpmodans)+" divi= "+moddivi+" ans = "+str(modans))
        else:
            # if dividend is greater , means it has higher power, so have to multiply,
            # that's why left shift to get tmp dividend, then xor
            tmpmodans = 0b1 << (len(moddivi) - len(moddivisor))

            tmpmoddivi = leftShift(moddivisor, (len(moddivi) - len(moddivisor)))
            moddivi = xorStrings(tmpmoddivi, moddivi)  # new divisor
            modans = tmpmodans + modans
            # print("inside else : tmpans = "+str(tmpmodans)+" tmpdivi = "+str(int(tmpmoddivi,2))+" divi= "+str(int(moddivi,2))+" ans = "+str(modans))

    # print("ans = "+str(modans)+" divisor = "+moddivisor+ " dividend = "+moddivi)

    return moddivi


# this funciton xors 2 binary strings

def xorStrings(str1, str2):
    ans = ""
    # make the the string same len
    if len(str1) < len(str2):
        for i in range(len(str2) - len(str1)):
            str1 = "0" + str1

    elif len(str1) > len(str2):
        for i in range(len(str1) - len(str2)):
            str2 = "0" + str2
    for i in range(len(str2) - 1, -1, -1):

        if str2[i] == str1[i]:
            ans = "0" + ans
        else:
            ans = "1" + ans
    if len(ans) == 0:
        return "0"
    # delete the extra zeros from front
    while (ans[0] == "0"):

        ans = ans[1:]
        if (len(ans) == 1):
            break
    return ans


# left shift string
def leftShift(str1, cnt):
    ans = "".join(["0" for i in range(cnt)])
    return str1 + ans


# multiply strings of binary
def multiply(str1, str2):
    """
    str1
    *str2

    101
   *011

   -----
   101
  101
 000
    """
    j = 0
    # initial ans = 0000000
    ans = "".join(["0" for i in range(len(str2))])
    # loop from last to first, if 1 then, left shift & xor, else do nothing

    for i in range(len(str2) - 1, -1, -1):
        if str2[i] == "1":
            ans = xorStrings(ans, leftShift(str1, j))
        j += 1

    # print("multiply ans : "+ans)
    return mod(ans, irrpoly)


# galois field code ends : works with binary string





def msg2matrix(text):
    """ Converts a 16-byte array into a 4x4 matrix.  """

    """
    text = "0123456789101112131415"
             |
             | 0 4 8 12
    matrix = | 1 5 9 13
             | 2 6 10 14
             | 3 7 11 15

    matrix[i]  = word[i] = " 00123 "
    key = "ab cd ef 2e "
    wordmatrix = [["ab"," cd"," ef"," 2e "]]
    """

    matrix = []
    for i in range(0, len(text), 8):
        tmpstr = text[i:i + 8]  #get the first 8 char , means 4 bytes
        # print(tmpstr)
        tmp = []
        for j in range(0, 8, 2):
            tmp.append(tmpstr[j:j + 2])  # make the 4 bytes each 1 byte in matrix index
        matrix.append(tmp)

    # return [list(text[i:i+4]) for i in range(0, len(text), 4)]
    return matrix


# xor 2 list of word
def xor2word(wrd1, wrd2):
    tmp = []
    for i in range(4):
        tmpstr = hex(int(wrd1[i], 16) ^ int(wrd2[i], 16))[2:]
        #insert 0 before if its single digit
        if len(tmpstr) == 1:
            tmpstr = "0" + tmpstr
        tmp.append(tmpstr)
    return tmp

# exapnsion of key 16byte to 44 bytes, returns a matrix of 4*44
def keyExpansion(key):
    # create the msg into matrix
    key_column = msg2matrix(key)
    expandedKey = []  # contains the ans

    # first 4 words are same as input
    for i in range(4):
        expandedKey.append(key_column[i])


    for i in range(4, 44):
        tmp = expandedKey[i - 1]  # string list of word = ["ab","bc","2f","4e"]

        if i % 4 == 0:
            tmp = subWord(rotateWord(tmp, -1))
            # print(tmp)
            tmp[0] = hex(int(tmp[0], 16) ^ int(rc[int(i / 4) - 1], 16))[2:]
            # if xor returns single digit, append zero
            if len(tmp[0]) == 1:
                tmpstr = "0" + tmp[0]
            # print(tmp)
        expandedKey.append(xor2word(expandedKey[i - 4], tmp))

    return expandedKey


# rotates word , cnt times , return list of byte, -1 means left shift 1 times
def rotateWord(word, cnt):
    items = deque(word)
    items.rotate(cnt)

    return list(items)


# substitute word ( list of bytes ) with sbox
def subWord(w3):
    tmpword = []
    # w3 = ["ab","bc","cd","de"]
    for i in range(4):

        tmp = w3[i]

        # row & column of sbox
        indRow = int(tmp[0], 16)
        indCol = int(tmp[1], 16)

        tmphexStr = sboxCalculated[indRow][indCol][2:]
        if len(tmphexStr) < 2:
            tmphexStr = "0" + tmphexStr
        tmpword.append(tmphexStr)

    return tmpword


# this subMatrix , takes a 16*16 matrix & calculates substitiuteion

def subMatrix(matrix):
    newMatrix = []
    for i in range(4):  # for every column
        tmp = subWord(matrix[i])
        # print(tmp)
        newMatrix.append(tmp)
    return newMatrix


# calculate RC[j] for key expansion
def calculateRC():
    # hex to bin : bin(int(my_hexdata, 16))[2:]
    # bin to hex : hex(int(my_bin,2))[2:]
    global rc
    rc = []
    rc.append("01")
    for i in range(44):
        tmprc = multiply(bin(int(rc[i], 16))[2:], "10")
        rc.append(hex(int(tmprc, 2))[2:])
    # rc = ["1","2","4","8",...]


"""
this matrix does the shift column op

         |
         | 0f 47 0c 4f |    
matrix = | 15 d9 b7 7f |
         | 71 e8 ad 57 |
         | c9 59 d6 98 |

index  = | 00 10 20 30
         | 01 11 21 31
         | 02 12 22 32
         | 03 13 23 33
"""


def shiftColumn(matrix):

    for i in range(4):  # for every row of the matrix:
        tmplist = []
        for j in range(4):  # list every element of the row
            tmplist.append(matrix[j][i])
        tmplist = rotateWord(tmplist, -1 * i) # rotate the row for row num

        # update the matrix
        for j in range(4):
            matrix[j][i] = tmplist[j]

    return matrix


# this func does the mix column option,
# for each column, it calculates the new column with the given equation of AES
def mixColumn(matrix):
    new_matrix = []
    for i in range(4):  # for every column of the matrix
        tmplist = []
        # for j in range(4):  # for entry in every column
        # s0, j = (2 * s0, j) ⊕(3 * s1, j) ⊕s2, j⊕s3, j
        #calculate the column of the matrix
        tmplist.append(hex(int((xorStrings(xorStrings(multiply(bin(int(matrix[i][0], 16))[2:], "10"),
                                                      multiply(bin(int(matrix[i][1], 16))[2:], "11"))
                                           ,
                                           xorStrings(bin(int(matrix[i][2], 16))[2:],
                                                      bin(int(matrix[i][3], 16))[2:])
                                           )), 2))[2:])
        tmplist.append(hex(int((xorStrings(xorStrings(multiply(bin(int(matrix[i][1], 16))[2:], "10"),
                                                      multiply(bin(int(matrix[i][2], 16))[2:], "11"))
                                           ,
                                           xorStrings(bin(int(matrix[i][0], 16))[2:],
                                                      bin(int(matrix[i][3], 16))[2:])
                                           )), 2))[2:])
        tmplist.append(hex(int((xorStrings(xorStrings(multiply(bin(int(matrix[i][2], 16))[2:], "10"),
                                                      multiply(bin(int(matrix[i][3], 16))[2:], "11"))
                                           ,
                                           xorStrings(bin(int(matrix[i][0], 16))[2:],
                                                      bin(int(matrix[i][1], 16))[2:])
                                           )), 2))[2:])
        tmplist.append(hex(int((xorStrings(xorStrings(multiply(bin(int(matrix[i][3], 16))[2:], "10"),
                                                      multiply(bin(int(matrix[i][0], 16))[2:], "11"))
                                           ,
                                           xorStrings(bin(int(matrix[i][1], 16))[2:],
                                                      bin(int(matrix[i][2], 16))[2:])
                                           )), 2))[2:])
        new_matrix.append(tmplist)
    return new_matrix

# count different of bits of 2 hex stiring
def diff_letters(a,b):

    result = int(a, 16) ^ int(b, 16)
    count = 0
    # Check for 1's in the binary form using
    # the count of 1 is the count of diffrenet bit
    while (result):
        result = result & (result - 1)
        count += 1
    return count


# add round

def addRoundKey(textMatrix, WordMatrix):
    new_matrix = []
    for i in range(4):  # for every column xor the column with corresponding word
        new_matrix.append(xor2word(textMatrix[i], WordMatrix[i]))

    return new_matrix

# matrix to text conversion
def matrix2txt(matrix):
    txt=""
    for i in range(4):
        for j in range(4):
            txt+=matrix[i][j]
    #print(txt)
    return txt

#sbox creating
def sboxCalc():
    global sboxCalculated
    sboxCalculated = []
    bin63rev = "11000110"
    for i in range(16):
        tmp = []
        for j in range(16):
            tmp.append(hex(i)[2:]+hex(j)[2:])
        sboxCalculated.append(tmp)
        
    #print(sboxCalculated)
    sboxCalculated[0][0] = "0x63"
    for i in range(16):
        for j in range(16):
            if j==0 and i==0:
                continue
            entry = sboxCalculated[i][j]
            binentry = bin(int(entry,16))[2:]
            if len(binentry)<8:
                for k in range(8-len(binentry)):
                    binentry = "0"+binentry
            #print(binentry)
            # get mul inverse
            binentry = multInverseDict[binentry]
            #print(binentry)
            # get reverse binary string
            binentry = binentry[::-1]
            #print(bin63rev)
            #print(binentry)
            tmpentry =""
            for k in range(8):
                #text[:1] + "Z" + text[2:]
                """
                if binentry[k]==binentry[(k+4)%8]==binentry[(k+5)%8]==binentry[(k+6)%8]==binentry[(k+7)%8]==bin63rev[k]:
                    tmpentry+="0"
                else :
                    tmpentry+="1"
                
                    """
                #print("zoring "+str(int(binentry[i],2))+str(int(binentry[(i+4)%8],2))+str(int(binentry[(i+5)%8],2))+str(int(binentry[(i+6)%8],2))+str(int(binentry[(i+7)%8],2))+str(int(bin63rev[i],2)))
                
                #print(int(binentry[k],2)^int(binentry[(k+4)%8],2)^int(binentry[(k+5)%8],2)^int(binentry[(k+6)%8],2)^int(binentry[(k+7)%8],2)^int(bin63rev[k],2))
                
                tmpentry+=(bin(int(binentry[k],2)^int(binentry[(k+4)%8],2)^int(binentry[(k+5)%8],2)^int(binentry[(k+6)%8],2)^int(binentry[(k+7)%8],2)^int(bin63rev[k],2)))[2:]
            #print(tmpentry)
            tmpentry = tmpentry[::-1]
            sboxCalculated[i][j] = hex(int(tmpentry,2))
            
            if len(sboxCalculated[i][j])<2:
                sboxCalculated[i][j] = "0"+sboxCalculated[i][j]
            sboxCalculated[i][j]="0x"+sboxCalculated[i][j]
            
    #print(sboxCalculated)       
            

# ciphertexted=[] contains ciphered text for each round
def aesAlgorithm(plaintxt, master_key):
    # calculate rc value for key expansion
    calculateRC()
    # get the state matrix from plain text string
    plaintxtMat = msg2matrix(plaintxt)
    ciphertexted=[]
    # first one is the plain text
    ciphertexted.append(plaintxt)

    # expand the key
    expandedKey = keyExpansion(master_key)

    # first add round
    plaintxtMat = addRoundKey(plaintxtMat, expandedKey[0:4])
    # 2nd round check
    ciphertexted.append(matrix2txt(plaintxtMat))



    # for the 9 round of encryption
    for i in range(9):

        # sub, shif, mix col, add round
        plaintxtMat = subMatrix(plaintxtMat)

        plaintxtMat = shiftColumn(plaintxtMat)
        plaintxtMat = mixColumn(plaintxtMat)
        plaintxtMat = addRoundKey(plaintxtMat, expandedKey[(i + 1) * 4:((i + 1) * 4) + 4])

        # append the cipher for each round
        ciphertexted.append(matrix2txt(plaintxtMat))
    # for the last round : sub shift , addround

    plaintxtMat = subMatrix(plaintxtMat)

    plaintxtMat = shiftColumn(plaintxtMat)
    plaintxtMat = addRoundKey(plaintxtMat, expandedKey[40:44])

    # append the cipher text
    ciphertexted.append(matrix2txt(plaintxtMat))

    return ciphertexted

getAllPossible8bitString()
calculateMulInverse()
sboxCalc()
# first aes plain text
aesTxt = "0123456789abcdeffedcba9876543210"
# aes key
aesKey = "0f1571c947d9e8590cb7add6af7f6798"

# aes encryption & list of ciphers from every round
cipher1List = aesAlgorithm(aesTxt, aesKey)

# aes plaintext 2
aesTxt2 = "0023456789abcdeffedcba9876543210"
# aes encryption of 2nd plain text& list of ciphers from every round
cipher2List = aesAlgorithm(aesTxt2, aesKey)

# for every round's cipher text, show the cipher & count difference of bits of between two
for i in range(len(cipher1List)):
    if i==0:
        print("Round 1 : first given plain text :")
    else:
        print("Round :"+str(i+1))
    print(cipher1List[i])
    print(cipher2List[i])
    print("difference : "+str(diff_letters(cipher1List[i],cipher2List[i])))

