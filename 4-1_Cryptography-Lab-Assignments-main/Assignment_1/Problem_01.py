plain_file = open("input.txt", "r")

key_file = open("key.txt", "r")

output_file = open("output.txt", "w")

plain = plain_file.readline()
key = key_file.readline()
plain = plain.replace(" ", '')

 
Letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

plain_text = ''

for i in range(len(plain)):
    if (plain[i] >= 'a' and plain[i]<='z') or (plain[i] >= 'A' and plain[i]<='Z'):
        plain_text += plain[i]

print("Plain Text: "+plain_text)

plain_length = len(plain_text)
key_length = len(key)

'''ratio = int(plain_length/key_length)

key = key + key*ratio

key = key[0:int(plain_length)]

key = str(key)'''


'''<<< Encryption >>> '''
encrypted_Message = ''


for i in range(len(plain_text)):
     index = (Letters.index(plain_text[i]) + Letters.index(key[i % key_length])) % 52
     encrypted_Message += Letters[index]

cipher_Text = ''
k = 0

for i in range(0,len(encrypted_Message)):
    if i != 0 and i%5 == 0:
        cipher_Text += encrypted_Message[k:i] + ' '
        k = i
cipher_Text += encrypted_Message[k:]



output_file.write(cipher_Text)
output_file.close()
print("Cipher Text: "+cipher_Text)


'''Decryption'''

decrypted_Message = ''
output_file = open("output.txt", "r")
cipher_Text = output_file.readline()
cipher_Text = cipher_Text.replace(" ", '')

print("cipher Text: "+cipher_Text)

for i in range(len(cipher_Text)):
     index = (Letters.index(cipher_Text[i]) - Letters.index(key[i%key_length])) % 52
     decrypted_Message += Letters[index]


print("Orginal Message: "+decrypted_Message)

cnt = 0

for i in range(len(plain_text)):
    if plain_text[i] != decrypted_Message[i]:
        cnt += 1

print("Miss Match in Character: "+str(cnt))


