def convertInByte(msg):
    return bytearray(msg, 'ascii')


def xor_Strings(a, b):
    
    return a ^ b


def encryption(msg, pad):
    msg = convertInByte(msg)
    pad = convertInByte(pad)
    cipher = bytearray()
    print(type(msg[0]))
    cipher.append(xor_Strings(msg[0], pad[0]))
    
    for i in range(1, len(msg)):
        temp = (cipher[i-1] + pad[i]) % 256
        
        cipher.append(xor_Strings(msg[i], temp))
    print(cipher.hex())
    return cipher.hex()


def decryption(cipher, pad):
    cipher = bytearray.fromhex(cipher)
    pad = bytearray(pad, 'ascii')
    # print(len(cipher))
    # print(len(pad))

    msg = bytearray()

    msg.append(xor_Strings(cipher[0], pad[0]))

    for i in range(1, len(cipher)):
        msg.append(xor_Strings(cipher[i], (pad[i] + cipher[i-1]) % 256))
    return msg.decode('utf-8')


def main():
    msg = 'absolutely'
    pad = 'assistance'
    x = encryption(msg, pad)

    print('Encrypted Message: '+x)
    y = decryption(x, pad)
    print('Decrypted Message: '+y)


main()
