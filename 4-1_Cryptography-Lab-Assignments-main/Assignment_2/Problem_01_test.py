cipher_1 = 'e9 3a e9 c5 fc 73 55 d5'
cipher_2 = 'f4 3a fe c7 e1 68 4a df'

cipher_1 = '0x'+cipher_1.replace(' ', '')
cipher_2 = '0x'+cipher_2.replace(' ', '')
print(cipher_1)

xor_Ciphers = hex((int((cipher_1.encode('utf-8')).hex(), 16))
                  ^ (int(cipher_2.encode('utf-8').hex(), 16)))
print(xor_Ciphers)


def xor_strings(s, t):
    return binascii.hexlify(''.join(chr(ord(a) ^ ord(b)) for a, b in zip(s, t)))


print(xor_strings(cipher_1, cipher_2))
