
from baseGraphs import graphNodes
import os
import time
from functions.csvEntry import addLine
import sys
path = '/Users/shifatsarwar/Downloads/Job/graphfunction/dataList/tests/'     

def runGraph01(file1):
    inputSize = os.path.getsize(file1)
    start_time = time.time()
    output = graphNodes.graph01(file1)
    stop_time = time.time()
    timeTaken = stop_time-start_time
    outputSize = sys.getsizeof(output)
    dataLine = 'graph01,1,1,'+str(inputSize)+','+str(outputSize)+','+str(timeTaken)+',0'
    addLine(path+'graph01.csv',dataLine)

def runGraph02(file1, file2):
    inputSize = os.path.getsize(file1)+os.path.getsize(file2)
    start_time = time.time()
    output = graphNodes.graph02(file1, file2)
    stop_time = time.time()
    timeTaken = stop_time-start_time
    outputSize = sys.getsizeof(output)
    # outputSize = os.path.getsize(output)
    dataLine = 'graph02,2,1,'+str(inputSize)+','+str(outputSize)+','+str(timeTaken)+',1'
    addLine(path+'graph02.csv',dataLine)

def runGraph03(file1, file2):
    inputSize = os.path.getsize(file1)+os.path.getsize(file2)
    start_time = time.time()
    output = graphNodes.graph03(file1, file2)
    stop_time = time.time()
    timeTaken = stop_time-start_time
    outputSize = sys.getsizeof(output)
    dataLine = 'graph03,2,1,'+str(inputSize)+','+str(outputSize)+','+str(timeTaken)+',2'
    addLine(path+'graph03.csv',dataLine)

def runGraph04(file1, file2, file3):
    inputSize = os.path.getsize(file1)+os.path.getsize(file2)+os.path.getsize(file3)
    start_time = time.time()
    output = graphNodes.graph04(file1, file2, file3)
    stop_time = time.time()
    timeTaken = stop_time-start_time
    outputSize = sys.getsizeof(output)
    # outputSize = os.path.getsize(output)
    dataLine = 'graph04,3,1,'+str(inputSize)+','+str(outputSize)+','+str(timeTaken)+',3'
    addLine(path+'graph04.csv',dataLine)

def runGraph05(file1, file2):
    inputSize = os.path.getsize(file1)+os.path.getsize(file2)
    start_time = time.time()
    output = graphNodes.graph05(file1, file2)
    stop_time = time.time()
    timeTaken = stop_time-start_time
    outputSize = sys.getsizeof(output)
    dataLine = 'graph05,2,1,'+str(inputSize)+','+str(outputSize)+','+str(timeTaken)+',4'
    addLine(path+'graph05.csv',dataLine)

def runGraph06(file1, file2):
    inputSize = os.path.getsize(file1)+os.path.getsize(file2)
    start_time = time.time()
    output = graphNodes.graph06(file1, file2)
    stop_time = time.time()
    timeTaken = stop_time-start_time
    outputSize = sys.getsizeof(output)
    dataLine = 'graph06,2,1,'+str(inputSize)+','+str(outputSize)+','+str(timeTaken)+',5'
    addLine(path+'graph06.csv',dataLine)

def runGraph07(file1, file2, file3):
    inputSize = os.path.getsize(file1)+os.path.getsize(file2)+os.path.getsize(file3)
    start_time = time.time()
    output = graphNodes.graph07(file1, file2, file3)
    stop_time = time.time()
    timeTaken = stop_time-start_time
    outputSize = sys.getsizeof(output)
    dataLine = 'graph07,3,1,'+str(inputSize)+','+str(outputSize)+','+str(timeTaken)+',6'
    addLine(path+'graph07.csv',dataLine)

def runGraph08(file1):
    inputSize = os.path.getsize(file1)
    start_time = time.time()
    output = graphNodes.graph08(file1)
    stop_time = time.time()
    timeTaken = stop_time-start_time
    outputSize = sys.getsizeof(output)
    dataLine = 'graph08,1,1,'+str(inputSize)+','+str(outputSize)+','+str(timeTaken)+',7'
    addLine(path+'graph08.csv',dataLine)

def runGraph09(file1):
    inputSize = os.path.getsize(file1)
    start_time = time.time()
    output = graphNodes.graph09(file1)
    stop_time = time.time()
    timeTaken = stop_time-start_time
    outputSize = sys.getsizeof(output)
    dataLine = 'graph09,1,1,'+str(inputSize)+','+str(outputSize)+','+str(timeTaken)+',8'
    addLine(path+'graph09.csv',dataLine)

def runGraph10(file1, file2, file3):
    inputSize = os.path.getsize(file1)+os.path.getsize(file2)+os.path.getsize(file3)
    start_time = time.time()
    output = graphNodes.graph10(file1, file2, file3)
    stop_time = time.time()
    timeTaken = stop_time-start_time
    outputSize = sys.getsizeof(output)
    dataLine = 'graph10,3,1,'+str(inputSize)+','+str(outputSize)+','+str(timeTaken)+',9'
    addLine(path+'graph10.csv',dataLine)


# def runGraph01():
#     graph = 'graph01'
#     createCSV(path+graph+'.csv')
#     arrayOfarray = []
#     with open(pathMain+"array_file111.csv") as f:
#         reader = csv.reader(f) 
#         for row in reader: 
#             arrayOfarray.append(row)

#     index = 0
#     while index < 100:
#         line = arrayOfarray[index]
#         array1 = []
#         for l in line:
#             array1.append(int(l))
        
#         start_time = time.time()
#         output = graphNodes.graph01(array1)
#         stop_time = time.time()
#         index = index+1
#         timeTaken = stop_time-start_time
#         inputSize = sys.getsizeof(array1)
#         outputSize = sys.getsizeof(output)
#         dataLine = graph+',1,1,'+str(inputSize)+','+str(outputSize)+','+str(timeTaken)+',0'
#         addLine(path+graph+'.csv',dataLine)

# def runGraph02():
#     graph = 'graph02'
#     createCSV(path+graph+'.csv')
#     arrayOfarray2 = []
#     with open(pathMain+"array_file222.csv") as f:
#         reader = csv.reader(f) 
#         for row in reader: 
#             arrayOfarray2.append(row)

#     index = 0
#     while index < 100:
#         file1Loc = '/Users/shifatsarwar/Downloads/Job/graphfunction/dataList/compressedFiles/array111'+str(index)
#         line2 = arrayOfarray2[index]
#         array2 = []
        
#         for l in line2:
#             array2.append(int(l))
#         inputSize = os.path.getsize(file1Loc+'.gz')+sys.getsizeof(array2)
#         start_time = time.time()
#         output = graphNodes.graph02(file1Loc, array2)
#         stop_time = time.time()
#         index = index+1
#         timeTaken = stop_time-start_time
#         outputSize = sys.getsizeof(output)
#         dataLine = graph+',2,1,'+str(inputSize)+','+str(outputSize)+','+str(timeTaken)+',1'
#         addLine(path+graph+'.csv',dataLine)
#         # Password can be a third input that can be provoked after initial process is complete.


# def runGraph03():
#     graph = 'graph03'
#     createCSV(path+graph+'.csv')
    
#     index = 0
#     while index < 100:
#         file1Loc = '/Users/shifatsarwar/Downloads/Job/graphfunction/dataList/encryptedFiles/array111'+str(index)+'.csv'
#         file2Loc = '/Users/shifatsarwar/Downloads/Job/graphfunction/dataList/encryptedFiles/array222'+str(index)+'.csv'
        
#         inputSize = os.path.getsize(file1Loc)+os.path.getsize(file2Loc)
#         start_time = time.time()
#         output = graphNodes.graph03(file1Loc, file2Loc)
#         stop_time = time.time()
#         index = index+1
#         timeTaken = stop_time-start_time
#         outputSize = sys.getsizeof(output)
#         dataLine = graph+',2,1,'+str(inputSize)+','+str(outputSize)+','+str(timeTaken)+',2'
#         addLine(path+graph+'.csv',dataLine)
#         # Password can be a third input that can be provoked after initial process is complete.

# def runGraph04():
#     graph = 'graph04'
#     createCSV(path+graph+'.csv')
#     arrayOfarray3 = []    
#     with open(pathMain+"array_file333.csv") as f:
#         reader = csv.reader(f) 
#         for row in reader: 
#             arrayOfarray3.append(row)

#     index = 0
#     while index < 100:
#         file1Loc = '/Users/shifatsarwar/Downloads/Job/graphfunction/dataList/compressedFiles/array111'+str(index)
#         file2Loc = '/Users/shifatsarwar/Downloads/Job/graphfunction/dataList/compressedFiles/array222'+str(index)
#         line3 = arrayOfarray3[index]
#         array3 = []
#         for l in line3:
#             array3.append(int(l))
#         inputSize = os.path.getsize(file1Loc+'.gz')+os.path.getsize(file2Loc+'.gz')+sys.getsizeof(array3)
#         start_time = time.time()
#         output = graphNodes.graph04(file1Loc, file2Loc, array3)
#         stop_time = time.time()
#         index = index+1
#         timeTaken = stop_time-start_time
#         outputSize = sys.getsizeof(output)
#         dataLine = graph+',3,1,'+str(inputSize)+','+str(outputSize)+','+str(timeTaken)+',3'
#         addLine(path+graph+'.csv',dataLine)
#         # Password can be a third input that can be provoked after initial process is complete.

# def runGraph05():
#     graph = 'graph05'
#     createCSV(path+graph+'.csv')    
#     index = 0
#     while index < 100:
#         file1Loc = '/Users/shifatsarwar/Downloads/Job/graphfunction/dataList/encryptedFiles/array111'+str(index)+'.csv'
#         file2Loc = '/Users/shifatsarwar/Downloads/Job/graphfunction/dataList/compressedFiles/array222'+str(index)
        
#         inputSize = os.path.getsize(file1Loc)+os.path.getsize(file2Loc+'.gz')
#         start_time = time.time()
#         output = graphNodes.graph05(file1Loc, file2Loc)
#         stop_time = time.time()
#         index = index+1
#         timeTaken = stop_time-start_time
#         outputSize = sys.getsizeof(output)
#         dataLine = graph+',2,1,'+str(inputSize)+','+str(outputSize)+','+str(timeTaken)+',4'
#         addLine(path+graph+'.csv',dataLine)

# def runGraph06():
#     graph = 'graph06'
#     createCSV(path+graph+'.csv')
    
#     index = 0
#     while index < 100:
#         file1Loc = '/Users/shifatsarwar/Downloads/Job/graphfunction/dataList/compressedFiles/array111'+str(index)
#         file2Loc = '/Users/shifatsarwar/Downloads/Job/graphfunction/dataList/compressedFiles/array222'+str(index)
        
#         inputSize = os.path.getsize(file1Loc+'.gz')+os.path.getsize(file2Loc+'.gz')
#         start_time = time.time()
#         output = graphNodes.graph06(file1Loc, file2Loc)
#         stop_time = time.time()
#         index = index+1
#         timeTaken = stop_time-start_time
#         outputSize = sys.getsizeof(output)
#         dataLine = graph+',2,1,'+str(inputSize)+','+str(outputSize)+','+str(timeTaken)+',5'
#         addLine(path+graph+'.csv',dataLine)

# def runGraph07():
#     graph = 'graph07'
#     createCSV(path+graph+'.csv')
#     arrayOfarray2 = []
#     with open(pathMain+"array_file333.csv") as f:
#         reader = csv.reader(f) 
#         for row in reader: 
#             arrayOfarray2.append(row)
    
#     index = 0
#     while index < 100:
#         line2 = arrayOfarray2[index]
#         array2 = []
#         for l in line2:
#             array2.append(int(l))
#         file1Loc = '/Users/shifatsarwar/Downloads/Job/graphfunction/dataList/compressedFiles/array111'+str(index)
#         file2Loc = '/Users/shifatsarwar/Downloads/Job/graphfunction/dataList/encryptedFiles/array222'+str(index)+'.csv'
        
#         inputSize = os.path.getsize(file1Loc+'.gz')+os.path.getsize(file2Loc)+sys.getsizeof(array2)
#         start_time = time.time()
#         output = graphNodes.graph07(file1Loc, file2Loc, array2)
#         stop_time = time.time()
#         index = index+1
#         timeTaken = stop_time-start_time
#         outputSize = sys.getsizeof(output)
#         dataLine = graph+',3,1,'+str(inputSize)+','+str(outputSize)+','+str(timeTaken)+',6'
#         addLine(path+graph+'.csv',dataLine)


# def runGraph08():
#     graph = 'graph08'
#     createCSV(path+graph+'.csv')
    
#     index = 0
#     while index < 100:
#         file1Loc = '/Users/shifatsarwar/Downloads/Job/graphfunction/dataList/encryptedFiles/array111'+str(index)+'.csv'
        
#         inputSize = os.path.getsize(file1Loc)
#         start_time = time.time()
#         output = graphNodes.graph08(file1Loc)
#         stop_time = time.time()
#         index = index+1
#         timeTaken = stop_time-start_time
#         outputSize = sys.getsizeof(output)
#         dataLine = graph+',1,1,'+str(inputSize)+','+str(outputSize)+','+str(timeTaken)+',7'
#         addLine(path+graph+'.csv',dataLine)


# def runGraph09():
#     graph = 'graph09'
#     createCSV(path+graph+'.csv')
    
#     index = 0
#     while index < 100:
#         file1Loc = '/Users/shifatsarwar/Downloads/Job/graphfunction/dataList/encryptedFiles/array111'+str(index)+'.csv'
        
#         inputSize = os.path.getsize(file1Loc)
#         start_time = time.time()
#         output = graphNodes.graph09(file1Loc)
#         stop_time = time.time()
#         index = index+1
#         timeTaken = stop_time-start_time
#         outputSize = sys.getsizeof(output)
#         dataLine = graph+',1,1,'+str(inputSize)+','+str(outputSize)+','+str(timeTaken)+',8'
#         addLine(path+graph+'.csv',dataLine)

# def runGraph10():
#     graph = 'graph10'
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
        
#         inputSize = os.path.getsize(file1Loc)+sys.getsizeof(array1)+os.path.getsize(file2Loc+'.gz')
#         start_time = time.time()
#         output = graphNodes.graph10(file1Loc, array1, file2Loc)
#         stop_time = time.time()
#         index = index+1
#         timeTaken = stop_time-start_time
#         outputSize = sys.getsizeof(output)
#         dataLine = graph+',3,1,'+str(inputSize)+','+str(outputSize)+','+str(timeTaken)+',9'
#         addLine(path+graph+'.csv',dataLine)

# rand = random.randint(1, 1500)
# rand = str(rand)
# s = time.time()
# x = 3+4
# print(time.time()-s)