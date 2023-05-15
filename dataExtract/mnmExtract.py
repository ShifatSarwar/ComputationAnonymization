from mixandmatch import mnm
import os
import time
from functions.csvEntry import addLine
import sys
path = '../dataList/tests/'
pathMain = '../'       

# Combines the three graphs 1,8 and 9
def runGraph189(file1):
    graphNum = [1,8,9]
    updateValues=[file1, file1, file1]
    inputSize = os.path.getsize(file1)
    output = mnm.process189W(updateValues)
    outputValues = output[0]
    timeValues = output[1]
    index=0
    for x in outputValues:
        name = 'graph0'+str(graphNum[index])
        if(type(x)==str):
            outputSize = os.path.getsize(x)
        else:
            outputSize = sys.getsizeof(x)
        dataLine = name+',1,1,'+str(inputSize)+','+str(outputSize)+','+str(timeValues[index])+','+str(graphNum[index]-1)
        addLine(path+name+'.csv',dataLine)
        index=index+1

# Combines the four graphs 2,3,5 and 6
def runGraph2356(file1, file2, file1E, file2E):
    inputFiles=[file1, file2]
    inputFiles2=[file1E, file2E]
    inputFiles3=[file1E, file2E]
    inputFiles4=[file1E, file2E]
    graphNum = [2,3,5,6]
    updateValues=[inputFiles,inputFiles2,inputFiles3,inputFiles4]
    inputSize = os.path.getsize(file1)+os.path.getsize(file2)
    inputSize2 = os.path.getsize(file1E)+ os.path.getsize(file2E)
    output = mnm.process2356W(updateValues)
    outputValues = output[0]
    timeValues = output[1]
    index=0
    for x in outputValues:
        name = 'graph0'+str(graphNum[index])
        if(index != 0):
            iSize = inputSize2
        else:
            iSize = inputSize
        if(type(x)==str):
            outputSize = os.path.getsize(x)
        else:
            outputSize = sys.getsizeof(x)
        dataLine = name+',2,1,'+str(iSize)+','+str(outputSize)+','+str(timeValues[index])+','+str(graphNum[index]-1)
        addLine(path+name+'.csv',dataLine)
        index=index+1

# Combines the three graphs 4,7 and 10
def runGraph4710(file1, file2, file3, file1E, file2E, file3E):
    inputFiles=[file1, file2, file3]
    inputFiles2=[file1, file2, file3]
    inputFiles3=[file1E, file2E, file3E]
    graphNum = [4,7,10]
    updateValues=[inputFiles,inputFiles2,inputFiles3]
    inputSize = os.path.getsize(file1)+os.path.getsize(file2)+os.path.getsize(file3)
    inputSize2 = os.path.getsize(file1E)+os.path.getsize(file2E)+os.path.getsize(file3E)
    output = mnm.process4710W(updateValues)
    outputValues = output[0]
    timeValues = output[1]
    index=0
    for x in outputValues:
        if(type(x)==str):
            outputSize = os.path.getsize(x)
        else:
            outputSize = sys.getsizeof(x)
        if index != 2:
            name = 'graph0'+str(graphNum[index])
            iSize = inputSize
        else: 
            name = 'graph'+str(graphNum[index])
            iSize = inputSize2

        dataLine = name+',3,1,'+str(iSize)+','+str(outputSize)+','+str(timeValues[index])+','+str(graphNum[index]-1)
        addLine(path+name+'.csv',dataLine)
        index=index+1
