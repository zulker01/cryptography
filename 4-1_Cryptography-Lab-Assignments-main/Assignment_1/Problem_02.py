import sys
import math

maxKeylength = 60

Letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'


pos = {}
icDiff = [100.0] * maxKeylength
icEnglish = 0.0686
originalFreq = [0.0815, 0.0144, 0.0276, 0.0379, 0.1311, 0.0292, 0.0199, 0.0526, 0.0635, 0.0013, 0.0042, 0.0339, 0.0254,
                0.0710, 0.0800, 0.0198, 0.0012, 0.0683, 0.0610, 0.1047, 0.0246, 0.0092, 0.0154, 0.0017, 0.0198, 0.0008]

output_file = open(
    "H:/4-1/CSE-4137- Cryptography and Security/Assignment/Assignment_1/output.txt", "r")
message = output_file.read()
message.replace(" ", '')
output_file.close()

input_file = open(
    "H:/4-1/CSE-4137- Cryptography and Security/Assignment/Assignment_1/input.txt", "r")
originalMessage = input_file.read()
input_file.close()

key_file = open(
    "H:/4-1/CSE-4137- Cryptography and Security/Assignment/Assignment_1/key.txt", "r")
originalKey = key_file.read()
key_file.close()


def formatText(message):
    filteredMessage = ''
    for i in range(0, len(message)):
        if(message[i] != ' '):
            filteredMessage += message[i]

    filteredMessage = filteredMessage.lower()
    return filteredMessage


def getICValue(length, msg):
    cosets = [''] * length
    for i in range(0, len(msg)):
        idx = i % length
        cosets[idx] += msg[i]

    h, w = length, 26
    localFreq = [[0.0 for x in range(w)] for y in range(h)]

    d = 0.0
    avg = 0.0

    for i in range(0, length):
        sz = len(cosets[i])

        for j in range(0, 26):
            localFreq[i][j] = 0.0
        for j in range(0, sz):
            localFreq[i][ord(cosets[i][j]) - 97] += 1

        for j in range(0, 26):
            temp = localFreq[i][j]
            temp *= (temp-1)
            d += temp

        d /= (sz*1.0)
        d /= (sz-1.0)
        avg += d

    ic = avg / length
    return ic


def pridictKeySize(message):
    icValues = [0.0] * 26
    for i in range(1, 26):
        icValues[i] = getICValue(i, message)
    # print(icValues)
    minDiff = 100000
    keyLength = 2

    for i in range(1, 26):
        temp = icEnglish - icValues[i]
        if(temp < 0):
            temp = abs(temp)
        icDiff[i] = temp
        if(temp < minDiff):
            minDiff = temp
            keyLength = i

    return keyLength


def shift_string(str, idx):
    ans = ''
    for i in range(0, len(str)):
        x = ord(str[i])-idx
        if(x < 97):
            x += 26
        ans += chr(x)
    return ans


def predictKey(message, keySize):
    cosetArray = [''] * keySize
    for i in range(0, len(message)):
        idx = i % keySize
        cosetArray[idx] += message[i]

    h, w = keySize, 26
    localFreq = [[0.0 for x in range(w)] for y in range(h)]

    szCosets = (len(message) + keySize - 1) // keySize
    h, w = 26, szCosets+500
    x2 = [[0.0 for x in range(w)] for y in range(h)]

    flag = 0
    for k in range(0, 26):

        for i in range(0, keySize):
            cosetArray[i] = shift_string(cosetArray[i], flag)

        for i in range(0, keySize):
            sz = len(cosetArray[i])

            for j in range(0, 26):
                localFreq[i][j] = 0.0
            for j in range(0, sz):
                localFreq[i][ord(cosetArray[i][j]) - 97] += 1
            for j in range(0, 26):
                localFreq[i][j] /= (sz * 1.0)

            for j in range(0, 26):
                temp = localFreq[i][j] - originalFreq[j]
                temp *= temp
                temp /= originalFreq[j]
                x2[k][i] += temp

        flag = 1

    key = ''

    for i in range(0, keySize):
        pos = 0
        minVal = x2[0][i]
        for j in range(1, 26):
            if (x2[j][i] < minVal):
                minVal = x2[j][i]
                pos = j

        key += chr(97 + pos)

    return key


def decode(cipher_Text, key, key_length):
    decrypted_Message = ''
    print("cipher Text: "+cipher_Text)

    for i in range(len(cipher_Text)):
        index = (Letters.index(cipher_Text[i]) -
                 Letters.index(key[i % key_length])) % 52
        decrypted_Message += Letters[index]

    print("Predicted Message: "+decrypted_Message)
    return decrypted_Message


'''def divisor(keySize):
    L = []
    for i in range(2, keySize):
        if keySize % i == 0:
            L.append(i)
    return L'''


message = formatText(message)
keySize = pridictKeySize(message)
print(message)
maxKeylength = keySize + 5

guesskey = ''
print('Predicted Length of key: ' + str(keySize))
print('Orginal Length of key: ' + str(len(originalKey)))
predict_key = predictKey(message, keySize+8)
print('Predicted key: '+predict_key)
predictMessage = decode(message, predict_key, keySize)

cnt = 0
for i in range(len(message)):
    if message[i] != predictMessage[i]:
        cnt += 1

print("Miss Match: "+str(cnt))
