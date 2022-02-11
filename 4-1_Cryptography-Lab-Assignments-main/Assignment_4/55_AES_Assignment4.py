from random import seed
from random import random


def makeSbox():
    sbox = [["" for i in range(16)] for j in range(16)]
    for i in range(16):
        for j in range(16):
            temp = bin(i)[2:].zfill(4)+bin(j)[2:].zfill(4)
            a = int(temp, 2)
            a = MultiInverse(a)
            sbox[i][j] = bin(a)[2:].zfill(8)
            sbox[i][j] = matMulSbox(sbox[i][j])

    return sbox


def mixColumn(s):
    mat = [[2, 3, 1, 1], [1, 2, 3, 1], [1, 1, 2, 3], [3, 1, 1, 2]]
    temp = matrixMul(mat, s)
    return temp


def shiftRow(ss):
    for i in range(4):
        temp = [0 for k in range(4)]
        for j in range(4):
            temp[j] = ss[i][(j-i+4) % 4]
        for j in range(4):
            ss[i][j] = temp[j]
    return ss


def addRoundkey(ss, kw):
    for i in range(4):
        for j in range(4):
            ss[j][i] = ss[j][i] ^ kw[j][i]
    return ss


def modular(m):
    while True:
        a = bin(m)[2:]
        b = ""
        b = bin(283)[2:]
        check = (len(a)-1)-(len(b)-1)
        if check < 0:
            return m
        m = m ^ (283 << check)


def multiplication(a, b):
    s2 = bin(b)[2:].zfill(8)
    s2 = ''.join(reversed(s2))
    m = 0
    for i in range(len(s2)):
        if s2[i] == '1':
            m = m ^ (a << i)
    temp = modular(m)
    return m


def MultiInverse(n):
    for i in range(0, 256):
        x = multiplication(n, i)
        if(x == 1):
            return i
    return 0


def matMulSbox(s):
    temp = [0 for i in range(8)]
    res = ""
    temp2 = [0 for i in range(8)]
    c = [1, 1, 0, 0, 0, 1, 1, 0]
    s = ''.join(reversed(s))
    for i in range(len(s)):
        if s[i] == '1':
            temp2[i] = 1
    for i in range(len(s)):
        temp[i] = temp2[i] ^ temp2[(i+4) % 8] ^ temp2[(i+5) %
                                                      8] ^ temp2[(i+6) % 8] ^ temp2[(i+7) % 8] ^ c[i]
    for i in range(len(temp)):
        if(temp[i] == 1):
            res += '1'
        else:
            res += '0'
    res = ''.join(reversed(res))
    return res


def matrixMul(mat, mat2):
    ss = [[0 for i in range(len(mat2[0]))] for j in range(len(mat))]
    for i in range(4):
        for j in range(4):
            m = 0
            for k in range(4):
                m = m ^ multiplication(mat[i][k], mat2[k][j])
            ss[i][j] = m
    return ss


def sboxValue(n, sBox):
    j = 0
    ss1 = ""
    ss2 = ""
    s2 = bin(n)[2:].zfill(8)

    for i in range(4):
        ss1 += s2[i]
    j = 4
    while j < len(s2):
        ss2 += s2[j]
        j += 1
    x = int(ss1, 2)
    y = int(ss2, 2)
    return int(sBox[x][y], 2)


def rcon(w, sBox, ii):
    temp = [0 for k in range(4)]
    b = 1

    for j in range(4):
        temp[j] = w[(j-1+4) % 4]
    for j in range(4):
        w[j] = sboxValue(temp[j], sBox)

    rc = [0 for k in range(4)]
    for v in range(ii-1):
        b = b << 1
        if(b > 255):
            b = b ^ 283
    rc[0] = b

    for j in range(4):
        w[j] = w[j] ^ rc[j]
    return w


def keyExpansion(key, sbox):
    word = [[0, 0, 0, 0] for i in range(44)]
    for i in range(4):
        word[i] = [key[4*i], key[4*i+1], key[4*i+2], key[4*i+3]]
    for i in range(4, 44):
        temp = word[i-1]
        if i % 4 == 0:
            temp = rcon(temp, sbox, int(i/4))
        for j in range(4):
            word[i][j] = word[i-4][j] ^ temp[j]
    return word


def changebitPlaintext(plaintext):
    v = int(random()*1000) % 16
    i = int(plaintext[v], 16)
    bi = bin(i)[2:]
    o = int(random()*1000) % (len(bi))
    stt = ""
    for u in range(len(bi)):
        if(u == o):
            if(bi[o] == '1'):
                stt += '0'
            else:
                stt += '1'
        else:
            stt += bi[u]
    i = int(stt, 2)

    plaintext[v] = hex(i)[2:]
    return plaintext


def AvalanceEffect(pl, apl):
    p = [0 for i in range(16)]
    ap = [0 for i in range(16)]
    xorsBins = ["" for i in range(16)]
    for i in range(16):
        p[i] = int(pl[i], 16)
        ap[i] = int(apl[i], 16)
    for i in range(16):
        xorsBins[i] += bin(p[i] ^ ap[i])[2:]
    an = 0
    for i in range(16):
        sttt = ""
        sttt += xorsBins[i]
        for j in range(len(sttt)):
            if(sttt[j] == '1'):
                an += 1
    return an


def AESEncryption(plaintxt, k):
    p = [0 for i in range(16)]
    ky = [0 for i in range(16)]
    for i in range(len(plaintxt)):
        p[i] = int(plaintxt[i], 16)
        ky[i] = int(k[i], 16)
    plainText = [[0 for i in range(4)] for j in range(4)]
    cypher = [[0 for i in range(4)] for j in range(4)]
    key = [[0 for i in range(4)] for j in range(4)]
    o = 0
    for i in range(4):
        for j in range(4):
            plainText[j][i] = p[o]
            o += 1
    sBox = makeSbox()
    words = keyExpansion(ky, sBox)

    for i in range(4):
        for j in range(4):
            w = words[i]
            key[j][i] = w[j]
            cypher = addRoundkey(plainText, key)
    # For round 1-11
    for r in range(1, 11):
        for i in range(4):
            for j in range(4):
                cypher[j][i] = sboxValue(cypher[j][i], sBox)
                w = words[4*r+i]
                key[j][i] = w[j]
        cypher = shiftRow(cypher)
        if(r != 10):
            cypher = mixColumn(cypher)
        addRoundkey(cypher, key)
    cypherText = ["" for i in range(16)]
    ct = 0
    for i in range(4):
        for j in range(4):
            cypherText[ct] += hex(cypher[j][i])[2:]
            ct += 1
    return cypherText


def main():
    plaintext = [["" for i in range(16)]for j in range(10)]
    key = ['0f', '15', '71', 'c9', '47', 'd9', 'e8', '59',
           '0c', 'b7', 'ad', 'd6', 'af', '7f', '67', '98']
    print("key: "+str(key))
    for j in range(10):
        for i in range(16):
            temp = (random()*1000) % 16
            if(temp == 0):
                plaintext[j][i] += "0"
            else:
                plaintext[j][i] += hex(int(temp))[2:]
            temp = (random()*1000) % 16
            if(temp == 0):
                plaintext[j][i] += "0"
            else:
                plaintext[j][i] += hex(int(temp))[2:]
        print("Round "+str(j)+":")
        print("PlainText:")
        print(plaintext[j])
        cypherpl = AESEncryption(plaintext[j], key)
        print("Cypher Text:")
        print(cypherpl)
        apl = changebitPlaintext(plaintext[j])
        cypherApl = AESEncryption(apl, key)
        print("Plaintext change:")
        print(apl)
        print("Avalanche Effect in ciphertext(changed in plaintext):")
        print(cypherApl)
        print(AvalanceEffect(cypherpl, cypherApl))


main()
