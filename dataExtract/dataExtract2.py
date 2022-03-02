
from anonymization.notUsed import anonimizedNodes
import os
import time
from functions.csvEntry import addLine
import sys
path = '/Users/shifatsarwar/Downloads/Job/graphfunction/dataList/'
pathMain = '/Users/shifatsarwar/Downloads/Job/graphfunction/'       
level = 5

def runGraph01(name, file1):
    inputSize = os.path.getsize(file1)
    start_time = time.time()
    output = anonimizedNodes.graph01(file1, level)
    stop_time = time.time()
    timeTaken = stop_time-start_time
    outputSize = sys.getsizeof(output)
    dataLine = name+',1,1,'+str(inputSize)+','+str(outputSize)+','+str(timeTaken)+',0'
    addLine(path+name+'.csv',dataLine)

def runGraph02(name, file1, file2):
    inputSize = os.path.getsize(file1)+os.path.getsize(file2)
    start_time = time.time()
    output = anonimizedNodes.graph02(file1, file2, level)
    stop_time = time.time()
    timeTaken = stop_time-start_time
    outputSize = sys.getsizeof(output)
    dataLine = name+',2,1,'+str(inputSize)+','+str(outputSize)+','+str(timeTaken)+',1'
    addLine(path+name+'.csv',dataLine)

def runGraph03(name, file1, file2):
    inputSize = os.path.getsize(file1)+os.path.getsize(file2)
    start_time = time.time()
    output = anonimizedNodes.graph03(file1, file2, level)
    stop_time = time.time()
    timeTaken = stop_time-start_time
    outputSize = sys.getsizeof(output)
    dataLine = name+',2,1,'+str(inputSize)+','+str(outputSize)+','+str(timeTaken)+',2'
    addLine(path+name+'.csv',dataLine)

def runGraph04(name, file1, file2, file3):
    inputSize = os.path.getsize(file1)+os.path.getsize(file2)+os.path.getsize(file3)
    start_time = time.time()
    output = anonimizedNodes.graph04(file1, file2, file3, level)
    stop_time = time.time()
    timeTaken = stop_time-start_time
    outputSize = sys.getsizeof(output)
    dataLine = name+',3,1,'+str(inputSize)+','+str(outputSize)+','+str(timeTaken)+',3'
    addLine(path+name+'.csv',dataLine)

def runGraph05(name, file1, file2):
    inputSize = os.path.getsize(file1)+os.path.getsize(file2)
    start_time = time.time()
    output = anonimizedNodes.graph05(file1, file2, level)
    stop_time = time.time()
    timeTaken = stop_time-start_time
    outputSize = sys.getsizeof(output)
    dataLine = name+',2,1,'+str(inputSize)+','+str(outputSize)+','+str(timeTaken)+',4'
    addLine(path+name+'.csv',dataLine)

def runGraph06(name, file1, file2):
    inputSize = os.path.getsize(file1)+os.path.getsize(file2)
    start_time = time.time()
    output = anonimizedNodes.graph06(file1, file2, level)
    stop_time = time.time()
    timeTaken = stop_time-start_time
    outputSize = sys.getsizeof(output)
    dataLine = name+',2,1,'+str(inputSize)+','+str(outputSize)+','+str(timeTaken)+',5'
    addLine(path+name+'.csv',dataLine)

def runGraph07(name, file1, file2, file3):
    inputSize = os.path.getsize(file1)+os.path.getsize(file2)+os.path.getsize(file3)
    start_time = time.time()
    output = anonimizedNodes.graph07(file1, file2, file3, level)
    stop_time = time.time()
    timeTaken = stop_time-start_time
    outputSize = sys.getsizeof(output)
    dataLine = name+',3,1,'+str(inputSize)+','+str(outputSize)+','+str(timeTaken)+',6'
    addLine(path+name+'.csv',dataLine)

def runGraph08(name, file1):
    inputSize = os.path.getsize(file1)
    start_time = time.time()
    output = anonimizedNodes.graph08(file1, level)
    stop_time = time.time()
    timeTaken = stop_time-start_time
    outputSize = sys.getsizeof(output)
    dataLine = name+',1,1,'+str(inputSize)+','+str(outputSize)+','+str(timeTaken)+',7'
    addLine(path+name+'.csv',dataLine)

def runGraph09(name, file1):
    inputSize = os.path.getsize(file1)
    start_time = time.time()
    output = anonimizedNodes.graph09(file1, level)
    stop_time = time.time()
    timeTaken = stop_time-start_time
    outputSize = sys.getsizeof(output)
    dataLine = name+',1,1,'+str(inputSize)+','+str(outputSize)+','+str(timeTaken)+',8'
    addLine(path+name+'.csv',dataLine)

def runGraph10(name, file1, file2, file3):
    inputSize = os.path.getsize(file1)+os.path.getsize(file2)+os.path.getsize(file3)
    start_time = time.time()
    output = anonimizedNodes.graph10(file1, file2, file3, level)
    stop_time = time.time()
    timeTaken = stop_time-start_time
    outputSize = sys.getsizeof(output)
    dataLine = name+',3,1,'+str(inputSize)+','+str(outputSize)+','+str(timeTaken)+',9'
    addLine(path+name+'.csv',dataLine)

# import csv
# import os
# from compress import Compressor
# import random
# import time
# from functions.csvEntry import addLine, createCSV
# import sys
# from anonymization import anonimizedNodes
# from Crypto.Cipher import AES
# from hashlib import sha256

# path = '/Users/shifatsarwar/Downloads/Job/graphfunction/dataList/'
# pathMain = '/Users/shifatsarwar/Downloads/Job/graphfunction/'
# pathCompressed = '/Users/shifatsarwar/Downloads/Job/graphfunction/dataList/compressedFiles/'
# level = 1

# def getArray(file):
#     arrayOfarray = []
#     with open(pathMain+file) as f:
#         reader = csv.reader(f) 
#         for row in reader: 
#             arrayOfarray.append(row)
    
#     return arrayOfarray


# def padArray(array):
#     size = len(array)
#     val = random.randint(10,30)
#     nSize = (val/100)*size
#     nSize = int(nSize)
#     while nSize > 0:
#         array.append(0)
#         nSize = nSize - 1
    
#     return array

# def makeFile(arrayName, array, index):
#     array = str(array)
#     aName = arrayName+str(index)
#     with open(path+aName+'.csv', 'w') as f:
#         f.write(array)
#         f.write("\n")
#     f.close()


# def compressArray(arrayName):
#     with open(pathCompressed+arrayName+'.csv', 'rb') as f:
#        original_file = f.read()
#     c = Compressor()
#     c.use_gzip() # or use_bz2, use_lzma, use_lz4, use_snappy
#     with open(pathCompressed+arrayName+'.gz', 'wb') as e:
#         e.write(c.compress(original_file))

# def encryptArray(arrayLoc):
#     password = 'myfile'
#     with open(path+arrayLoc, 'rb') as f:
#         original_file = f.read()
    
#     while len(original_file)%16 !=0:
#         original_file = original_file + b'0'
    
#     password = password.encode()
#     key = sha256(password).digest()
#     mode = AES.MODE_CBC
#     iv = os.urandom(16)
#     cipher = AES.new(key, mode, iv)
#     encryptedFile = cipher.encrypt(original_file)
#     with open(path+arrayLoc, 'wb') as e:
#         e.write(encryptedFile)


# def getinstantarray(line):
#     array = []
#     for l in line:
#         array.append(int(l))
#     return array

# def runAnonymizedGraph01():
#     graph = 'anonimizedGraph01'
#     createCSV(path+graph+'.csv')
#     arrayOfarray = getArray("array_file111.csv")

#     index = 0
#     while index < 100:
#         array1 = getinstantarray(arrayOfarray[index])
#         array1 = padArray(array1)
#         start_time = time.time()
#         output = anonimizedNodes.graph01(array1, level)
#         stop_time = time.time()
#         index = index+1
#         timeTaken = stop_time-start_time
#         inputSize = sys.getsizeof(array1)
#         outputSize = sys.getsizeof(output)
#         dataLine = graph+',1,1,'+str(inputSize)+','+str(outputSize)+','+str(timeTaken)+',0'
#         addLine(path+graph+'.csv',dataLine)
    
# def runAnonymizedGraph02():
#     graph = 'anonimizedGraph02'
#     createCSV(path+graph+'.csv')
#     arrayOfarray = getArray("array_file111.csv")
#     arrayOfarray2 = getArray("array_file222.csv")

#     index = 0
#     while index < 100:
#         array = getinstantarray(arrayOfarray[index])
#         array2 = getinstantarray(arrayOfarray2[index])
#         array = padArray(array)
#         array2 = padArray(array2)
#         makeFile("compressedFiles/array111", array, index)
#         compressArray("array111"+str(index))
#         file1Loc = '/Users/shifatsarwar/Downloads/Job/graphfunction/dataList/compressedFiles/array111'+str(index)
#         inputSize = os.path.getsize(file1Loc+'.gz')+sys.getsizeof(array2)
#         start_time = time.time()
#         output = anonimizedNodes.graph02(file1Loc, array2, level)
#         stop_time = time.time()
#         index = index+1
#         timeTaken = stop_time-start_time
#         outputSize = sys.getsizeof(output)
#         dataLine = graph+',2,1,'+str(inputSize)+','+str(outputSize)+','+str(timeTaken)+',1'
#         addLine(path+graph+'.csv',dataLine)

# def runAnonymizedGraph03():
#     graph = 'anonimizedGraph03'
#     createCSV(path+graph+'.csv')
#     arrayOfarray = getArray("array_file111.csv")
#     arrayOfarray2 = getArray("array_file222.csv")

#     index = 0
#     while index < 100:
#         array = getinstantarray(arrayOfarray[index])
#         array2 = getinstantarray(arrayOfarray2[index])
#         array = padArray(array)
#         array2 = padArray(array2)
#         makeFile("encryptedFiles/array111", array, index)
#         encryptArray("encryptedFiles/array111"+str(index)+'.csv')
#         makeFile("encryptedFiles/array222", array2, index)
#         encryptArray("encryptedFiles/array222"+str(index)+'.csv')
#         file1Loc = '/Users/shifatsarwar/Downloads/Job/graphfunction/dataList/encryptedFiles/array111'+str(index)+'.csv'
#         file2Loc = '/Users/shifatsarwar/Downloads/Job/graphfunction/dataList/encryptedFiles/array222'+str(index)+'.csv'
#         inputSize = os.path.getsize(file1Loc)+os.path.getsize(file2Loc)
#         start_time = time.time()
#         output = anonimizedNodes.graph03(file1Loc, file2Loc, level)
#         stop_time = time.time()
#         index = index+1
#         timeTaken = stop_time-start_time
#         outputSize = sys.getsizeof(output)
#         dataLine = graph+',2,1,'+str(inputSize)+','+str(outputSize)+','+str(timeTaken)+',2'
#         addLine(path+graph+'.csv',dataLine)

# def runAnonymizedGraph04():
#     graph = 'anonimizedGraph04'
#     createCSV(path+graph+'.csv')
#     arrayOfarray = getArray("array_file111.csv")
#     arrayOfarray2 = getArray("array_file222.csv")
#     arrayOfarray3 = getArray("array_file333.csv")   
#     index = 0
#     while index < 100:
#         array1 = getinstantarray(arrayOfarray[index])
#         array2 = getinstantarray(arrayOfarray2[index])
#         array3 = getinstantarray(arrayOfarray3[index])
#         array1 = padArray(array1)
#         array2 = padArray(array2)
#         array2 = padArray(array3)
#         makeFile("compressedFiles/array111", array1, index)
#         compressArray("array111"+str(index))
#         makeFile("compressedFiles/array222", array2, index)
#         compressArray("array222"+str(index))
#         file1Loc = '/Users/shifatsarwar/Downloads/Job/graphfunction/dataList/compressedFiles/array111'+str(index)
#         file2Loc = '/Users/shifatsarwar/Downloads/Job/graphfunction/dataList/compressedFiles/array222'+str(index)
#         inputSize = os.path.getsize(file1Loc+'.gz')+os.path.getsize(file2Loc+'.gz')+sys.getsizeof(array3)
#         start_time = time.time()
#         output = anonimizedNodes.graph04(file1Loc, file2Loc, array3, level)
#         stop_time = time.time()
#         index = index+1
#         timeTaken = stop_time-start_time
#         outputSize = sys.getsizeof(output)
#         dataLine = graph+',3,1,'+str(inputSize)+','+str(outputSize)+','+str(timeTaken)+',3'
#         addLine(path+graph+'.csv',dataLine)
    
# def runAnonymizedGraph05():
#     graph = 'anonimizedGraph05'
#     createCSV(path+graph+'.csv')
#     arrayOfarray = getArray("array_file111.csv")
#     arrayOfarray2 = getArray("array_file222.csv")
#     index = 0
#     while index < 100:
#         array1 = getinstantarray(arrayOfarray[index])
#         array2 = getinstantarray(arrayOfarray2[index])
#         array1 = padArray(array1)
#         array2 = padArray(array2)
#         makeFile("encryptedFiles/array111", array1, index)
#         encryptArray("encryptedFiles/array111"+str(index)+'.csv')
#         makeFile("compressedFiles/array222", array2, index)
#         compressArray("array222"+str(index))
#         file1Loc = '/Users/shifatsarwar/Downloads/Job/graphfunction/dataList/encryptedFiles/array111'+str(index)+'.csv'
#         file2Loc = '/Users/shifatsarwar/Downloads/Job/graphfunction/dataList/compressedFiles/array222'+str(index)
#         inputSize = os.path.getsize(file1Loc)+os.path.getsize(file2Loc+'.gz')
#         start_time = time.time()
#         output = anonimizedNodes.graph05(file1Loc, file2Loc, level)
#         stop_time = time.time()
#         index = index+1
#         timeTaken = stop_time-start_time
#         outputSize = sys.getsizeof(output)
#         dataLine = graph+',2,1,'+str(inputSize)+','+str(outputSize)+','+str(timeTaken)+',4'
#         addLine(path+graph+'.csv',dataLine)

    
# def runAnonymizedGraph06():
#     graph = 'anonimizedGraph06'
#     createCSV(path+graph+'.csv')
#     arrayOfarray = getArray("array_file111.csv")
#     arrayOfarray2 = getArray("array_file222.csv")
#     index = 0
#     while index < 100:
#         array1 = getinstantarray(arrayOfarray[index])
#         array2 = getinstantarray(arrayOfarray2[index])
#         array1 = padArray(array1)
#         array2 = padArray(array2)
#         makeFile("compressedFiles/array111", array1, index)
#         compressArray("array111"+str(index))
#         makeFile("compressedFiles/array222", array2, index)
#         compressArray("array222"+str(index))
#         file1Loc = '/Users/shifatsarwar/Downloads/Job/graphfunction/dataList/compressedFiles/array111'+str(index)
#         file2Loc = '/Users/shifatsarwar/Downloads/Job/graphfunction/dataList/compressedFiles/array222'+str(index)
#         inputSize = os.path.getsize(file1Loc+'.gz')+os.path.getsize(file2Loc+'.gz')
#         start_time = time.time()
#         output = anonimizedNodes.graph06(file1Loc, file2Loc, level)
#         stop_time = time.time()
#         index = index+1
#         timeTaken = stop_time-start_time
#         outputSize = sys.getsizeof(output)
#         dataLine = graph+',2,1,'+str(inputSize)+','+str(outputSize)+','+str(timeTaken)+',5'
#         addLine(path+graph+'.csv',dataLine)
    
    
# def runAnonymizedGraph07():
#     graph = 'anonimizedGraph07'
#     createCSV(path+graph+'.csv')
#     arrayOfarray = getArray("array_file111.csv")
#     arrayOfarray2 = getArray("array_file222.csv")
#     arrayOfarray3 = getArray("array_file333.csv") 
#     index = 0
#     while index < 100:
#         array1 = getinstantarray(arrayOfarray[index])
#         array2 = getinstantarray(arrayOfarray2[index])
#         array3 = getinstantarray(arrayOfarray3[index])
#         array1 = padArray(array1)
#         array2 = padArray(array2)
#         array2 = padArray(array3)
#         makeFile("compressedFiles/array222", array2, index)
#         compressArray("array222"+str(index))
#         makeFile("encryptedFiles/array333", array3, index)
#         encryptArray("encryptedFiles/array333"+str(index)+'.csv')
#         file1Loc = '/Users/shifatsarwar/Downloads/Job/graphfunction/dataList/compressedFiles/array222'+str(index)
#         file2Loc = '/Users/shifatsarwar/Downloads/Job/graphfunction/dataList/encryptedFiles/array333'+str(index)+'.csv'
#         inputSize = os.path.getsize(file1Loc+'.gz')+os.path.getsize(file2Loc)+sys.getsizeof(array1)
#         start_time = time.time()
#         output = anonimizedNodes.graph07(array1, file1Loc, file2Loc, level)
#         stop_time = time.time()
#         index = index+1
#         timeTaken = stop_time-start_time
#         outputSize = sys.getsizeof(output)
#         dataLine = graph+',3,1,'+str(inputSize)+','+str(outputSize)+','+str(timeTaken)+',6'
#         addLine(path+graph+'.csv',dataLine)
    
    

# def runAnonymizedGraph08():
#     graph = 'anonimizedGraph08'
#     createCSV(path+graph+'.csv')
#     arrayOfarray = getArray("array_file111.csv")
#     index = 0
#     while index < 100:
#         array1 = getinstantarray(arrayOfarray[index])
#         array1 = padArray(array1)
#         makeFile("encryptedFiles/array111", array1, index)
#         encryptArray("encryptedFiles/array111"+str(index)+'.csv')
#         file1Loc = '/Users/shifatsarwar/Downloads/Job/graphfunction/dataList/encryptedFiles/array111'+str(index)+'.csv'
#         inputSize = os.path.getsize(file1Loc)
#         start_time = time.time()
#         output = anonimizedNodes.graph08(file1Loc, level)
#         stop_time = time.time()
#         index = index+1
#         timeTaken = stop_time-start_time
#         outputSize = sys.getsizeof(output)
#         dataLine = graph+',1,1,'+str(inputSize)+','+str(outputSize)+','+str(timeTaken)+',7'
#         addLine(path+graph+'.csv',dataLine)
    
    

# def runAnonymizedGraph09():
#     graph = 'anonimizedGraph09'
#     createCSV(path+graph+'.csv')
#     index = 0
#     while index < 100:
#         file1Loc = '/Users/shifatsarwar/Downloads/Job/graphfunction/dataList/encryptedFiles/array111'+str(index)+'.csv'
#         # padFile(file1Loc)
#         inputSize = os.path.getsize(file1Loc)
#         start_time = time.time()
#         output = anonimizedNodes.graph09(file1Loc, level)
#         stop_time = time.time()
#         index = index+1
#         timeTaken = stop_time-start_time
#         outputSize = sys.getsizeof(output)
#         dataLine = graph+',1,1,'+str(inputSize)+','+str(outputSize)+','+str(timeTaken)+',8'
#         addLine(path+graph+'.csv',dataLine)
    
# def runAnonymizedGraph10():
#     graph = 'anonimizedGraph10'
#     createCSV(path+graph+'.csv')
#     arrayOfarray = []
#     with open(pathMain+"array_file333.csv") as f:
#         reader = csv.reader(f) 
#         for row in reader: 
#             arrayOfarray.append(row)
    
#     index = 0
#     while index < 100:
#         line = arrayOfarray[index]
#         array1 = []
#         for l in line:
#             array1.append(int(l))
        
#         file1Loc = '/Users/shifatsarwar/Downloads/Job/graphfunction/dataList/encryptedFiles/array111'+str(index)+'.csv'
#         file2Loc = '/Users/shifatsarwar/Downloads/Job/graphfunction/dataList/compressedFiles/array222'+str(index)
#         # padFile(file1Loc)
#         # padFile(file2Loc)
#         array1 = padArray(array1)
#         inputSize = os.path.getsize(file1Loc)+sys.getsizeof(array1)+os.path.getsize(file2Loc+'.gz')
#         start_time = time.time()
#         output = anonimizedNodes.graph10(file1Loc, array1, file2Loc, level)
#         stop_time = time.time()
#         index = index+1
#         timeTaken = stop_time-start_time
#         outputSize = sys.getsizeof(output)
#         dataLine = graph+',3,1,'+str(inputSize)+','+str(outputSize)+','+str(timeTaken)+',9'
#         addLine(path+graph+'.csv',dataLine)