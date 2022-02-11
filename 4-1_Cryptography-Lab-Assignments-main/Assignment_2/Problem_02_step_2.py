import itertools


def valid(n):
    if (n >= 65 and n <= 90) or (n >= 97 and n <= 122) or n == 32 or n == 33 or n == 40 or n == 41 or n == 44 or n == 45 or n == 46 or n == 63:
        return 1
    else:
        return 0


def compare(a, b, c):
    if a == 0:
        xor = (a ^ b)
    else:
        xor = b ^ (a + c) % 256
    if valid(xor) == 1:
        return 1
    else:
        return 0


def generateTable(cipher):
    value = []
    comTable = []
    for i in range(60):
        value = []
        for j in range(256):
            cnt = 0
            for k in range(10):
                if i == 0:
                    temp = compare(j, cipher[k][i], 0)
                else:
                    temp = compare(j, cipher[k][i], cipher[k][i-1])
                if temp == 1:
                    cnt += 1
            if cnt == 10:
                value.append(j)
        comTable.append(value)

    return comTable


# def combine(temp):
class TrieNode:
    # Trie node class

    def __init__(self):

        self.children = [None]*26

        # isEndOfWord is True if node represent the end of the word

        self.isEndOfWord = False


class Trie:

    # Trie data structure class

    def __init__(self):

        self.root = self.getNode()

    def getNode(self):

        # Returns new trie node (initialized to NULLs)

        return TrieNode()

    def _charToIndex(self, ch):

        # private helper function

        # Converts key current character into index

        # use only 'a' through 'z' and lower case

        return ord(ch)-ord('a')

    def insert(self, key):

        # If not present, inserts key into trie

        # If the key is prefix of trie node,

        # just marks leaf node

        pCrawl = self.root

        length = len(key)

        for level in range(length):

            index = self._charToIndex(key[level])

            # if current character is not present

            if not pCrawl.children[index]:

                pCrawl.children[index] = self.getNode()

            pCrawl = pCrawl.children[index]
            pCrawl.isEndOfWord = True

        # mark last node as leaf

        #pCrawl.isEndOfWord = True

    def search(self, key):

        # Search key in the trie

        # Returns true if key presents

        # in trie, else false

        pCrawl = self.root

        length = len(key)

        for level in range(length):

            index = self._charToIndex(key[level])

            if not pCrawl.children[index]:

                return False

            pCrawl = pCrawl.children[index]

        return pCrawl != None and pCrawl.isEndOfWord


def main():
    cipher = [[32, 14, 162, 166, 143, 97, 199, 84, 128, 186, 67, 246, 43, 37, 76, 222, 75, 131, 131, 185, 79, 149, 100, 201, 116, 219, 101, 188, 112, 206, 25, 63, 147, 142, 153, 112, 190, 67, 231, 37, 246, 85, 249, 123, 161, 135, 215, 124, 193, 143, 135, 201, 67, 237, 54, 246, 74, 196, 77, 80],
              [39, 0, 27, 44, 224, 51, 18, 23, 10, 43, 233, 81, 198, 215, 123, 142, 182, 124, 137, 167, 108, 187, 67, 244, 104, 192, 128, 151, 142, 174,
                  124, 225, 32, 250, 13, 90, 212, 35, 82, 206, 41, 3, 33, 236, 84, 242, 7, 60, 0, 21, 20, 36, 167, 143, 136, 201, 104, 164, 119, 218],
              [36, 10, 29, 37, 8, 28, 68, 254, 37, 16, 233, 93, 197, 133, 236, 29, 5, 36, 253, 57, 138, 216, 26, 34, 58, 82, 169, 192, 66, 8, 22, 123,
                  140, 135, 140, 137, 158, 96, 200, 64, 219, 111, 217, 82, 252, 100, 164, 158, 186, 155, 108, 193, 75, 254, 38, 167, 159, 105, 184, 157],
              [35, 6, 19, 53, 170, 127, 168, 114, 203, 116, 131, 188, 100, 181, 139, 153, 140, 136, 220, 78, 218, 52, 196, 114, 170, 203, 159, 246, 47,
               18, 17, 56, 201, 64, 207, 94, 214, 43, 19, 9, 250, 30, 9, 5, 114, 206, 86, 251, 18, 52, 239, 77, 144, 180, 121, 163, 151, 141, 146, 164],
              [58, 204, 20, 103, 216, 44, 2, 14, 54, 235, 45, 25, 9, 26, 42, 234, 67, 249, 8, 36, 250, 19, 164, 143, 140, 237, 80, 245, 55, 27,
               227, 75, 203, 20, 236, 60, 233, 45, 19, 15, 226, 6, 59, 248, 55, 9, 16, 59, 23, 63, 135, 205, 66, 230, 75, 197, 109, 170, 126, 143],
              [57, 205, 18, 17, 70, 214, 112, 183, 108, 207, 47, 29, 20, 33, 72, 204, 51, 232, 51, 236, 45, 246, 19, 3, 35, 13, 47, 8, 75, 247, 13,
               114, 130, 142, 138, 146, 159, 127, 190, 8, 227, 7, 39, 236, 78, 182, 69, 255, 79, 244, 40, 49, 243, 72, 254, 47, 27, 20, 231, 56],
              [51, 23, 237, 70, 242, 6, 99, 132, 181, 111, 141, 177, 100, 251, 98, 162, 154, 134, 155, 139, 144, 159, 99, 210, 67, 247, 10, 32, 163, 168,
               123, 161, 103, 181, 71, 148, 134, 146, 130, 158, 125, 181, 215, 77, 242, 91, 191, 39, 61, 19, 21, 107, 172, 150, 205, 91, 236, 43, 255, 16],
              [39, 7, 25, 32, 28, 238, 27, 239, 94, 213, 103, 213, 91, 245, 76, 197, 99, 220, 34, 17, 242, 48, 216, 15, 17, 55, 12, 38, 251, 64, 139,
               164, 119, 192, 79, 156, 158, 125, 181, 111, 157, 142, 183, 107, 217, 81, 169, 152, 172, 193, 90, 233, 63, 242, 44, 224, 4, 20, 225, 99],
              [35, 6, 31, 114, 172, 120, 185, 81, 189, 126, 131, 183, 111, 128, 179, 119, 158, 133, 144, 185, 68, 138, 143, 142, 135, 232, 120, 202, 95,
               227, 39, 10, 23, 227, 48, 233, 47, 211, 2, 4, 31, 7, 105, 169, 147, 190, 64, 168, 172, 149, 146, 164, 98, 199, 62, 249, 79, 222, 35, 116],
              [32, 14, 162, 189, 125, 158, 131, 204, 108, 210, 45, 15, 67, 29, 10, 28, 19, 2, 4, 55, 219, 97, 189, 96, 220, 120, 217, 99, 230, 106,
               186, 223, 36, 226, 34, 228, 101, 191, 96, 234, 16, 60, 23, 10, 119, 217, 40, 3, 89, 231, 33, 54, 237, 93, 218, 92, 128, 132, 157, 171]
              ]
    temp = generateTable(cipher)
    # combine(temp)
    print(temp)
    for i in range(len(temp)):
        for j in range(len(temp[i])):
            temp[i][j] = chr(temp[i][j])
    print(temp)


main()
