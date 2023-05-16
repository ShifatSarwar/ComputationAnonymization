import numpy as np
from hashlib import sha256
import time
import os
from Crypto.Cipher import AES
from numpy import random
from compress import Compressor

decryptLoc = 'dataList/decryptLoc/'
encryptLoc = 'dataList/encryptedFiles/'
compressedLoc = 'dataList/compressedFiles/'

#Merge Sort
def sortArray(array):
    for i in range(len(array)):
        min_idx = i
        for j in range(i+1, len(array)):
            if array[min_idx] > array[j]:
                min_idx = j    
        array[i], array[min_idx] = array[min_idx], array[i] 
    return array

def calculateContentsSingle(array):
    index = 0
    for i in array:
        array[index] = i*9 
        index = index + 1
    return array

def hashResults(product):
    hash_object = sha256((str(product)).encode())
    return hash_object.hexdigest()


def calculateContents(array1, array2):
    array1 = np.array(array1)
    array2 = np.array(array2)
    array3 = np.multiply(array1,array2)
    output = []
    for l in array3:
        output.append(int(l))
    return output

#Process for AES Encryption
def encryptAES(array):
    rand = random.randint(1,500)
    password = 'myfile'
    array = str(array)
    with open('arrayfinal.csv', 'w') as f:
        f.write(array)
        f.write("\n")
    f.close()
    with open('arrayfinal.csv', 'rb') as f:
        original_file = f.read()
    
    while len(original_file)%16 !=0:
        original_file = original_file + b'0'
    
    password = password.encode()
    key = sha256(password).digest()
    mode = AES.MODE_CBC
    iv = os.urandom(16)
    cipher = AES.new(key, mode, iv)
    encryptedFile = cipher.encrypt(original_file)
    
    with open(encryptLoc+'arrayfinal'+str(rand)+'.csv', 'wb') as e:
        e.write(encryptedFile)

    return encryptedFile


#Process for AES Decryption
def decryptAES(myFile):
    rand = random.randint(1,500)
    password = 'myfile'
    with open(myFile, 'rb') as f:
        encryptedFile = f.read()
    password = password.encode()
    key = sha256(password).digest()
    mode = AES.MODE_CBC
    iv = os.urandom(16)
    cipher = AES.new(key, mode, iv) 
    decryptedFile = cipher.decrypt(encryptedFile)
    with open(decryptLoc+'file'+str(rand)+'.csv', 'wb') as e:
        e.write(decryptedFile.rstrip(b'0'))
    
    with open(decryptLoc+'file'+str(rand)+'.csv', 'rb') as f:
        row = f.read()
        row = str(row)
    
    array = row.split(',')
    
    output = []
    for l in array:
        l = l.replace(' ', "")
        if(l.isdecimal()):
            output.append(int(l))
        else:
            output.append(random.randint(1000,10000))   
    return output

#Process for GZip Compression
def compressGZip(array):
    rand = random.randint(1,500)
    array = str(array)
    with open('arrayCompressed.csv', 'w') as f:
        f.write(array)
        f.write("\n")
    f.close()
    with open('arrayCompressed.csv', 'rb') as f:
       original_file = f.read()
    c = Compressor()
    c.use_gzip() # or use_bz2, use_lzma, use_lz4, use_snappy
    with open(compressedLoc+'arrayCompressed'+str(rand)+'.gz', 'wb') as e:
        e.write(c.compress(original_file))
    return compressedLoc+'arrayCompressed'+str(rand)+'.gz'

#Process for GZip Decompression
def decompressGZip(myFile):
    with open(myFile+'.gz', 'rb') as f:
       original_file = f.read()
    c = Compressor()
    c.use_gzip() # or use_bz2, use_lzma, use_lz4, use_snappy
    with open(myFile+'.csv', 'wb') as e:
        e.write(c.decompress(original_file))
    
    with open(myFile+'.csv', 'rb') as f:
        row = f.read()
        row = str(row)
    
    array = row.split(',')
    
    output = []
    for l in array:
        l = l.replace(' ', "")
        if(l.isdecimal()):
            output.append(int(l))
        else:
            output.append(random.randint(1000,10000))   
    return output
    

def fixLength(array1, array2):
    length = [len(array1), len(array2)]
    length.sort()
    while (len(array1) > length[0]):
        array1.pop(0)
    while (len(array2) > length[0]):
        array2.pop(0)
    array = [array1, array2]
    return array
        
def encryptAESFile(loc):
    rand = random.randint(1,1500)
    password = 'myfile'
    with open(loc, 'rb') as f:
        original_file = f.read()
    while len(original_file)%16 !=0:
        original_file = original_file + b'0'
    password = password.encode()
    key = sha256(password).digest()
    mode = AES.MODE_CBC
    iv = os.urandom(16)
    cipher = AES.new(key, mode, iv)
    encryptedFile = cipher.encrypt(original_file)
    with open(encryptLoc+'arrayfinal'+str(rand)+'.csv', 'wb') as e:
        e.write(encryptedFile)
    return encryptedFile

#Insert Sort
def sortArray2(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j] :
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key 
    return arr 

# returns an array from a file
def getArray(file):
    with open(file, 'rb') as f:
        row = f.read()
        row = str(row)
    array = row.split(',')
    output = []
    for l in array:
        l = l.replace(' ', "")
        if(l.isdecimal()):
            output.append(int(l))
        else:
            output.append(random.randint(1000,10000))   
    return output

# fixes length for data calculation
def fixLengthAll(a1,a2,a3):
    length = [len(a1), len(a2), len(a3)]
    length.sort()
    while (len(a1) > length[0]):
        a1.pop(0)
    while (len(a2) > length[0]):
        a2.pop(0)
    while (len(a3) > length[0]):
        a3.pop(0)
    array = [a1,a2,a3]
    return array

# wait time during anonymization
def doNothing():
    time.sleep(random.randint(0,2))
    return 0

# Checks anonymity level
def checkAnonymity(level, end):
    if level > 0:
        if end:
            while level > 0:
                doNothing()
                level = level - 1
        else:
            r = random.choice([0,1])
            if r == 1:
                doNothing()
                return level - 1
    return level



