cipher_1 = 0xe93ae9c5fc7355d5
cipher_2 = 0xf43afec7e1684adf

#cipher_1 = '0x'+cipher_1.replace(' ', '')
#cipher_2 = '0x'+cipher_2.replace(' ', '')


# xor_Ciphers = hex((int((cipher_1.encode('utf-8')).hex(), 16))
#               ^ (int(cipher_2.encode('utf-8').hex(), 16)))
xor_Ciphers = hex(cipher_1 ^ cipher_2)
input_file = open(
    'words.txt', 'r')
wordsList = []

for i in range(2502):
    word = '0x'+input_file.readline()
    wordsList.append(word[0:-1])
input_file.close()

result = []

print(len(wordsList[0]))
for i in range(len(wordsList)):
    text_1 = wordsList[i]
    for j in range(i, len(wordsList)):
        text_2 = wordsList[j]
        xor_texts = hex(int(text_1.encode('utf-8').hex(), 16)
                        ^ int(text_2.encode('utf-8').hex(), 16))
        if(xor_Ciphers == xor_texts):
            result.append(text_1[2:])
            result.append(text_2[2:])
            break
print(result)

print(xor_Ciphers)
