import csv
from hashlib import sha256
import os
from Crypto.Cipher import AES
pathMain = '/Users/shifatsarwar/Downloads/Job/graphfunction/dataList/arrayFiles/'
pathEncrypted = '/Users/shifatsarwar/Downloads/Job/graphfunction/dataList/encryptedFiles/'
pathCompressed = '/Users/shifatsarwar/Downloads/Job/graphfunction/dataList/compressedFiles/'

def encryptArray(arrayLoc):
    password = 'myfile'
    with open(arrayLoc, 'rb') as f:
        original_file = f.read()
    
    while len(original_file)%16 !=0:
        original_file = original_file + b'0'
    
    password = password.encode()
    key = sha256(password).digest()
    mode = AES.MODE_CBC
    iv = os.urandom(16)
    cipher = AES.new(key, mode, iv)
    encryptedFile = cipher.encrypt(original_file)
    with open(arrayLoc, 'wb') as e:
        e.write(encryptedFile)


def startEncryption():
    arrayOfarray = []
    arrayOfarray2 = []
    arrayOfarray3 = []
    with open(pathMain+"array_file111.csv") as f:
        reader = csv.reader(f) 
        for row in reader: 
            arrayOfarray.append(row)
    
    with open(pathMain+"array_file222.csv") as f:
        reader = csv.reader(f) 
        for row in reader: 
            arrayOfarray2.append(row)

    with open(pathMain+"array_file333.csv") as f:
        reader = csv.reader(f) 
        for row in reader: 
            arrayOfarray3.append(row)

    index = 0
    while index < 100:
        line = arrayOfarray[index]
        line2 = arrayOfarray2[index]
        line3 = arrayOfarray3[index]
        array1 = []
        array2 = []
        array3 = []
        for l in line:
            array1.append(int(l))
        
        for l in line2:
            array2.append(int(l))

        for l in line3:
            array3.append(int(l))

        array1 = str(array1)
        array2 = str(array2)
        array3 = str(array3)
        array1Loc = pathEncrypted+'array111'+str(index)+'.csv'
        array2Loc = pathEncrypted+'array222'+str(index)+'.csv'
        array3Loc = pathEncrypted+'array333'+str(index)+'.csv'
        with open(array1Loc, 'w') as f:
            f.write(array1)
            f.write("\n")
        f.close()

        with open(array2Loc, 'w') as f:
            f.write(array2)
            f.write("\n")
        f.close()

        with open(array3Loc, 'w') as f:
            f.write(array3)
            f.write("\n")
        f.close()

        encryptArray(array1Loc)
        encryptArray(array2Loc)
        encryptArray(array3Loc)
        index = index + 1

startEncryption()