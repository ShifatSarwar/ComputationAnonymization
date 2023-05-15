from baseGraphs import graphs
import os
import time
from functions.csvEntry import addLine
import sys
path = '../dataList/'    

def runGraph01(file1):
    inputSize = os.path.getsize(file1)
    start_time = time.time()
    output = graphs.graph01(file1)
    stop_time = time.time()
    timeTaken = stop_time-start_time
    outputSize = sys.getsizeof(output)
    dataLine = 'graph01,1,1,'+str(inputSize)+','+str(outputSize)+','+str(timeTaken)+',0'
    addLine(path+'graph01.csv',dataLine)

def runGraph02(file1):
    inputSize = os.path.getsize(file1)
    start_time = time.time()
    output = graphs.graph02(file1)
    stop_time = time.time()
    timeTaken = stop_time-start_time
    outputSize = sys.getsizeof(output)
    dataLine = 'graph02,1,1,'+str(inputSize)+','+str(outputSize)+','+str(timeTaken)+',1'
    addLine(path+'graph02.csv',dataLine)

def runGraph03(file1):
    inputSize = os.path.getsize(file1)
    start_time = time.time()
    output = graphs.graph03(file1)
    stop_time = time.time()
    timeTaken = stop_time-start_time
    outputSize = sys.getsizeof(output)
    dataLine = 'graph03,1,1,'+str(inputSize)+','+str(outputSize)+','+str(timeTaken)+',2'
    addLine(path+'graph03.csv',dataLine)

def runGraph04(file1):
    inputSize = os.path.getsize(file1)
    start_time = time.time()
    output = graphs.graph04(file1)
    stop_time = time.time()
    timeTaken = stop_time-start_time
    outputSize = sys.getsizeof(output)
    dataLine = 'graph04,1,1,'+str(inputSize)+','+str(outputSize)+','+str(timeTaken)+',3'
    addLine(path+'graph04.csv',dataLine)

def runGraph05(file1, file2):
    inputSize = os.path.getsize(file1)+os.path.getsize(file2)
    start_time = time.time()
    output = graphs.graph05(file1, file2)
    stop_time = time.time()
    timeTaken = stop_time-start_time
    outputSize = os.path.getsize(output)
    dataLine = 'graph05,2,1,'+str(inputSize)+','+str(outputSize)+','+str(timeTaken)+',4'
    addLine(path+'graph05.csv',dataLine)

def runGraph06(file1, file2):
    inputSize = os.path.getsize(file1)+os.path.getsize(file2)
    start_time = time.time()
    output = graphs.graph06(file1, file2)
    stop_time = time.time()
    timeTaken = stop_time-start_time
    outputSize = sys.getsizeof(output)
    dataLine = 'graph06,2,1,'+str(inputSize)+','+str(outputSize)+','+str(timeTaken)+',5'
    addLine(path+'graph06.csv',dataLine)

def runGraph07(file1, file2):
    inputSize = os.path.getsize(file1)+os.path.getsize(file2)
    start_time = time.time()
    output = graphs.graph07(file1, file2)
    stop_time = time.time()
    timeTaken = stop_time-start_time
    outputSize = os.path.getsize(output)
    dataLine = 'graph07,2,1,'+str(inputSize)+','+str(outputSize)+','+str(timeTaken)+',6'
    addLine(path+'graph07.csv',dataLine)

def runGraph08(file1, file2):
    inputSize = os.path.getsize(file1)+os.path.getsize(file2)
    start_time = time.time()
    output = graphs.graph08(file1, file2)
    stop_time = time.time()
    timeTaken = stop_time-start_time
    outputSize = sys.getsizeof(output)
    dataLine = 'graph08,2,1,'+str(inputSize)+','+str(outputSize)+','+str(timeTaken)+',7'
    addLine(path+'graph08.csv',dataLine)


def runGraph09(file1, file2, file3):
    inputSize = os.path.getsize(file1)+os.path.getsize(file2)+os.path.getsize(file3)
    start_time = time.time()
    output = graphs.graph09(file1, file2, file3)
    stop_time = time.time()
    timeTaken = stop_time-start_time
    outputSize = sys.getsizeof(output)
    dataLine = 'graph09,3,1,'+str(inputSize)+','+str(outputSize)+','+str(timeTaken)+',8'
    addLine(path+'graph09.csv',dataLine)

def runGraph10(file1, file2, file3):
    inputSize = os.path.getsize(file1)+os.path.getsize(file2)+os.path.getsize(file3)
    start_time = time.time()
    output = graphs.graph10(file1, file2, file3)
    stop_time = time.time()
    timeTaken = stop_time-start_time
    outputSize = sys.getsizeof(output)
    dataLine = 'graph10,3,1,'+str(inputSize)+','+str(outputSize)+','+str(timeTaken)+',9'
    addLine(path+'graph10.csv',dataLine)

def runGraph11(file1, file2, file3):
    inputSize = os.path.getsize(file1)+os.path.getsize(file2)+os.path.getsize(file3)
    start_time = time.time()
    output = graphs.graph11(file1, file2, file3)
    stop_time = time.time()
    timeTaken = stop_time-start_time
    outputSize = sys.getsizeof(output)
    dataLine = 'graph11,3,1,'+str(inputSize)+','+str(outputSize)+','+str(timeTaken)+',10'
    addLine(path+'graph11.csv',dataLine)

def runGraph12(file1, file2, file3):
    inputSize = os.path.getsize(file1)+os.path.getsize(file2)+os.path.getsize(file3)
    start_time = time.time()
    output = graphs.graph12(file1, file2, file3)
    stop_time = time.time()
    timeTaken = stop_time-start_time
    outputSize = sys.getsizeof(output)
    dataLine = 'graph12,3,1,'+str(inputSize)+','+str(outputSize)+','+str(timeTaken)+',11'
    addLine(path+'graph12.csv',dataLine)




