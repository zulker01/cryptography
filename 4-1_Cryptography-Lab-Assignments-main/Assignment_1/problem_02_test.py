import sys
import math

maxKeyLength = 60

Letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

myfile1 = open("output.txt", "r")
message = myfile1.read()
message.replace(" ", '')
myfile1.close()


myfile2 = open("input.txt", "r")
originalMessage = myfile2.read()
myfile2.close()

myfile3 = open("key.txt", "r")
originalKey = myfile3.read()
myfile3.close()

pos = {}
icDiff = [100.0] * maxKeyLength
icEnglish = 0.0686
originalFreq = [0.0815, 0.0144, 0.0276, 0.0379, 0.1311, 0.0292, 0.0199, 0.0526, 0.0635, 0.0013, 0.0042, 0.0339, 0.0254,
                0.0710, 0.0800, 0.0198, 0.0012, 0.0683, 0.0610, 0.1047, 0.0246, 0.0092, 0.0154, 0.0017, 0.0198, 0.0008]


def formatText(message):
    filteredMessage = ''
    for i in range(0, len(message)):
        if(message[i] != ' '):
            filteredMessage += message[i]

    filteredMessage = filteredMessage.lower()
    return filteredMessage


def getPos(originalMessage):
    tempMessage = originalMessage
    szTempMessage = len(tempMessage)

    for i in range(0, szTempMessage + 5):
        pos[i] = 0
    for i in range(0, szTempMessage):
        if (tempMessage[i] >= 'A' and tempMessage[i] <= 'Z'):
            pos[i] = 1


def formatOriginalMessage(message):

    filteredMessage = ''
    for i in range(0, len(message)):
        if (ord(message[i]) >= 65 and ord(message[i]) <= 90):
            filteredMessage += message[i]

        if (ord(message[i]) >= 97 and ord(message[i]) <= 122):
            filteredMessage += message[i]

    # filteredMessage.lower()
    getPos(filteredMessage)

    return filteredMessage


def shift_string(str, idx):
    ans = ''
    for i in range(0, len(str)):
        x = ord(str[i])-idx
        if(x < 97):
            x += 26
        ans += chr(x)
    return ans


def getICValue(leng, msg):
    cosetArray = [''] * leng
    for i in range(0, len(msg)):
        idx = i % leng
        cosetArray[idx] += msg[i]

    h, w = leng, 26
    localFreq = [[0.0 for x in range(w)] for y in range(h)]

    ddemo = 0.0
    avg = 0.0

    for i in range(0, leng):
        sz = len(cosetArray[i])

        for j in range(0, 26):
            localFreq[i][j] = 0.0
        for j in range(0, sz):
            localFreq[i][ord(cosetArray[i][j]) - 97] += 1

        for j in range(0, 26):
            temp = localFreq[i][j]
            temp *= (temp-1)
            ddemo += temp

        ddemo /= (sz*1.0)
        ddemo /= (sz-1.0)
        avg += ddemo

        # print(localFreq[i])
    ic = avg / leng
    #print(leng, ic)
    return ic


def getKeySize(message):
    icValues = [0.0] * maxKeyLength
    for i in range(3, maxKeyLength):
        icValues[i] = getICValue(i, message)

    minDiff = 100000
    keyLegth = 2

    for i in range(3, maxKeyLength):
        temp = icEnglish - icValues[i]
        if(temp < 0):
            temp *= -1
        icDiff[i] = temp
        if(temp < minDiff):
            minDiff = temp
            keyLegth = i

    return keyLegth


def guessKey(message, keySize):
    cosetArray = [''] * keySize
    for i in range(0, len(message)):
        idx = i % keySize
        cosetArray[idx] += message[i]

    # for i in range (0,keySize):
    #    print(cosetArray[i])

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

            # print(localFreq[i])

        flag = 1

    # for i in range (0,26):
    #    print(i, x2[i])
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
    # print('Possible key is: ' + key)'''


def decode(message, key):

    cipherText = message
    decodedMessage = ''

    for i in range(len(cipherText)):
        index = (Letters.index(cipherText[i]) -
                 Letters.index(key[i % len(key)])) % 52
        decodedMessage += Letters[index]

    decodedMessage = decodedMessage.lower()
    finalMessage = ''
    for i in range(0, len(decodedMessage)):
        if(pos[i] == 1):
            temp = chr(ord(decodedMessage[i])-32)
        else:
            temp = decodedMessage[i]
        finalMessage += temp

    return decodedMessage


def getMessage(message, key):
    demoKey = key
    for i in range(len(key), len(message)):
        demoKey += key[i % len(key)]
    # print(message)
    # print(demoKey)
    decodedMessage = decode(message, demoKey)

    return decodedMessage


def comparison(originalMessage, message, originalKey, key):

    print('Original size of key: ' + str(len(originalKey)))
    print('Predicted key: ' + key)
    print('Original key: ' + originalKey)

    matched, unmatched = 0, 0
    for i in range(0, min(len(key), len(originalKey))):
        if(key[i] == originalKey[i]):
            matched += 1
        else:
            unmatched += 1

    unmatched += abs(len(key) - len(originalKey))
    temp = (100.0*matched) / (matched + unmatched)
    print('Matched character: ' + str(matched) +
          ', accuracy = ' + str(temp)[0:5] + '%')
    temp = 100 - temp
    print('Unmatched character: ' + str(unmatched) +
          ', accuracy = ' + str(temp)[0:5] + '%\n')

    print('Original message: \n' + originalMessage)
    print('Predicted message: \n' + message)
    matched, unmatched = 0, 0
    for i in range(0, len(message)):
        if (message[i] == originalMessage[i]):
            matched += 1
        else:
            unmatched += 1

    temp = (100.0 * matched) / len(message)
    print('Matched character: ' + str(matched) +
          ', accuracy = ' + str(temp)[0:5] + '%')
    temp = 100 - temp
    print('Unmatched character: ' + str(unmatched) +
          ', accuracy = ' + str(temp)[0:5] + '%')

    return


def tryMoreKeys(idx):

    print('######################### ' + str(idx))

    print('Possible size of key: ' + str(idx))
    ##key = guessKey(message, idx)
    # print(key)
    #decodedMessage = getMessage(message, key)
    # print(decodedMessage)
    #comparison(originalMessage, decodedMessage, originalKey, key)

    return


# main function from here

message = formatText(message)
originalMessage = formatOriginalMessage(originalMessage)
keySize = getKeySize(message)
maxKeyLength = keySize + 5
print('Possible size of key: ' + str(keySize))
key = guessKey(message, keySize)
print(key)
decodedMessage = getMessage(message, key)
print(decodedMessage)
comparison(originalMessage, decodedMessage, originalKey, key)
