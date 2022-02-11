from cryptography.fernet import Fernet


# generates AES like random key
# returns byte object
def keyGeneration():
    key = Fernet.generate_key()
    return key


# creating the binary tree

def BinaryTreeConstruction(size):
    binaryTree = list()
    binaryTree.append(dict())
    for i in range(1, size + 1):
        node = dict()
        node['is_root'] = 0
        node['type'] = 0
        node['key'] = keyGeneration().decode('ascii')
        binaryTree.append(node)
    binaryTree[1]['is_root'] = 1
    binaryTree[1]['type'] = 1
    return binaryTree


# return all path keys
def getKeys(tree, position):
    keys = list()
    while position >= 1:
        keys.append(tree[position]['key'])
        position = position // 2
    return keys


# return key is content key or not
def find_contentkey(key, content_key):
    if key == content_key:
        return True
    else:
        return False


def make_movie(m, content_key, kroot):
    encryptedMovie = MovieEncryption(m, content_key)
    header = list()
    header.append(MovieEncryption(content_key, kroot))
    movie = dict()
    movie['header'] = header
    movie['eMovie'] = encryptedMovie
    return movie

# returns the sibling node id of a node
# works for binary tree only
def getSibling(id):
    if id % 2 == 0:
        return id + 1
    else:
        return id - 1

# initializes the dvd class
def DVD_construction(size, tree):
    dvd = list()
    for i in range(0, size):
        mydvd = dict()
        mydvd['pos'] = size + i
        mydvd['keys'] = getKeys(tree, mydvd['pos'])
        dvd.append(mydvd)
    return dvd


# AES encryption
def MovieEncryption(message, key):
    AES = Fernet(key)
    encryptedmovie = AES.encrypt(message.encode('ascii'))
    return encryptedmovie


# AES decryption
def MovieDecryption(encryptedData, key):
    AES = Fernet(key)
    try:
        decryptedData = AES.decrypt(encryptedData).decode('ascii')
    except:
        return str("-1")
    return decryptedData


# checks if a dvd can decrypt a particular movie
def decryptMovie(movie, tree, dvd, dvd_id, content_key):
    path_keys = dvd[dvd_id]['keys']
    for i in range(0, len(path_keys)):
        for j in range(0, len(movie['header'])):
            decryptedKey = MovieDecryption(movie['header'][j], path_keys[i])
            if find_contentkey(decryptedKey, content_key):
                decryptedMovie = MovieDecryption(movie['eMovie'], decryptedKey)
                return decryptedMovie
    message = "From DVD " + str(dvd_id) + " the movie can't be decrypted"
    return message



# updates the movie header by adding siblings' keys of decrypted DVD
# and remove decrypted DVD's content key.
def addNewKeyHeader(movie, content_key, redKey, greenKey):
    header = movie['header']
    for i in range(0, len(header)):
        decryptedKey = MovieDecryption(header[i], redKey)
        if decryptedKey == content_key:
            header.pop(i)
            break

    if greenKey != "":
        header.append(MovieEncryption(content_key, greenKey))
    movie['header'] = header
    return movie


# blocks a particular dvd node to access the movie further
def blockExposedDVD(tree, dvd, dvd_id, movie, content_key):
    treenode_id = dvd[dvd_id]['pos']
    if tree[treenode_id]['type'] == -1:
        print("dvd player " + str(dvd_id) + " is already blocked")
        return movie

    curAt = treenode_id
    while True:
        if curAt == 1:
            tree[curAt]['type'] = -1
            movie = addNewKeyHeader(movie, content_key, tree[curAt]['key'], "")
            print("dvd player " + str(dvd_id) + " is blocked")
            return movie

        if tree[curAt]['type'] == 1:
            movie = addNewKeyHeader(movie, content_key, tree[curAt]['key'], "")
        tree[curAt]['type'] = -1
        sibing = getSibling(curAt)

        if tree[sibing]['type'] == 0:
            tree[sibing]['type'] = 1
            movie = addNewKeyHeader(movie, content_key, tree[curAt]['key'], tree[sibing]['key'])

        curAt = curAt // 2


# blocks multiple dvds at a same time
def blockMulutipleDVD(tree, dvd, movie, content_key, start, end):
    for i in range(start, end + 1):
        movie = blockExposedDVD(tree, dvd, i, movie, content_key)
    return movie


# prints the current status of the whole network
def info(movie, tree, content_key):
    header = movie['header']
    l = list()
    for i in range(0, len(header)):
        for j in range(1, len(tree)):
            if MovieDecryption(header[i], tree[j]['key']) == content_key:
                l.append(j)
                break
    l.sort()
    print()
    print("Following encrypted keys are stored in header")
    print(len(l), l)
    print()


def main():


    keySize = 16
    noOfDVD = 64
    m = "It's a movie."
    content_key = keyGeneration().decode('ascii')


    Totalnodes = 2 * noOfDVD - 1 #total nodes in binary tree.
    tree = BinaryTreeConstruction(Totalnodes)
    dvd = DVD_construction(noOfDVD, tree)
    movie = make_movie(m, content_key, tree[1]['key'])

    #results of the code
    movie = blockExposedDVD(tree, dvd, 3, movie, content_key)
    print(len(movie['header']))
    print(decryptMovie(movie, tree, dvd, 3,content_key))
    info(movie, tree, content_key)

    movie = blockExposedDVD(tree, dvd, 3, movie, content_key)
    print(len(movie['header']))
    print(decryptMovie(movie, tree, dvd, 3,content_key))

    movie = blockExposedDVD(tree, dvd, 43, movie, content_key)
    print(len(movie['header']))
    print(decryptMovie(movie, tree, dvd, 43,content_key))
    info(movie, tree, content_key)

    movie = blockExposedDVD(tree, dvd, 17, movie, content_key)
    print(len(movie['header']))
    print(decryptMovie(movie, tree, dvd, 17,content_key))
    info(movie, tree, content_key)

    movie = blockExposedDVD(tree, dvd, 37, movie, content_key)
    print(len(movie['header']))
    print(decryptMovie(movie, tree, dvd, 37,content_key))
    info(movie, tree, content_key)

    movie = blockExposedDVD(tree, dvd, 55, movie, content_key)
    print(len(movie['header']))
    print(decryptMovie(movie, tree, dvd, 55,content_key))
    info(movie, tree, content_key)

    decryptedMovie = decryptMovie(movie, tree, dvd, 3,content_key)
    print(3, decryptedMovie)

    movie = blockExposedDVD(tree, dvd, 29, movie, content_key)
    print(len(movie['header']))
    print(decryptMovie(movie, tree, dvd, 29,content_key))
    info(movie, tree, content_key)

    movie = blockMulutipleDVD(tree, dvd, movie, content_key, 1, 5)

    for i in range(0, 64):
        decryptedMovie = decryptMovie(movie, tree, dvd, i,content_key)
        print(i, decryptedMovie)


main()

