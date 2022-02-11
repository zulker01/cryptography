def convertToBinary(a):
    return f'{a:16b}'


def addition(a, b):
    return a ^ b


table = []


def inversTable():
    for i in range(256):
        t = []
        for j in range(256):
            t.append(multiplication(i, j))
            if multiplication(i, j) == 1:
                print(i, j)
        table.append(t)
    return table


def multiplication(a, b):
    tmp = str(convertToBinary(b))
    tmp = ''.join(reversed(tmp))
    m = convertToBinary(283)

    result = int('0', 2)
    for i in range(len(tmp)):
        if tmp[i] == '1':
            result ^= a << i

    # Reduce
    tmp2 = str(convertToBinary(result))
    tmp2 = convertToBinary(result)

    k = 0
    for i in range(len(tmp2)):
        if tmp2[i] == '0' or tmp2[i] == '1':
            k = i
            break
    tmp2 = tmp2[k:len(tmp2)]
    mod = str(m)
    for i in range(len(mod)):
        if mod[i] == '0' or mod[i] == '1':
            k = i
            break
    mod = mod[k:len(mod)]
    k = modularInverse(tmp2, mod)
    print(type(k))
    return str(k)


def modularInverse(a, b):
    pick = len(b)
    tmp = a[0: pick]

    while pick < len(a):
        if tmp[0] == '1':
            tmp = xor(b, tmp) + a[pick]
        else:
            tmp = xor('0' * pick, tmp) + a[pick]
        pick += 1

    if len(convertToBinary(a), 2) < len(convertToBinary(b), 2):
        return a
    if tmp[0] == '1':
        tmp = xor(b, tmp)
    else:
        tmp = xor('0' * pick, tmp)
    print(tmp)
    return int(str(tmp), 2)


def xor(a, b):
    res = []
    for i in range(1, len(b)):
        if a[i] == b[i]:
            res.append('0')
        else:
            res.append('1')
    return ''.join(res)


def division(a, b):
    inverse = table[b].index(1)
    return a * inverse



def main():
    print(table)
    operand_1 = int(input("enter a bit stream of first operand: "), 2)
    operand_2 = int(input("enter a bit stream of second operand: "), 2)
    option = input("enter an option (+,-,*,/): ")

    if option == '+' or option == '-':
        print('Addition or Substraction: ' +
              str(convertToBinary(addition(operand_1, operand_2))))
    elif option == '*':
        x = multiplication(operand_1, operand_2)
        print('Multiplication: '+str(convertToBinary(x)))
        print(x)
    elif option == '/':
        x = division(operand_1, operand_2)
        print('division: '+str(x))
    inversTable()


main()
