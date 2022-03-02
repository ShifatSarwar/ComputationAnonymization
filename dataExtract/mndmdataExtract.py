from mixandmatch import mixAndMatch
import os
import time
from functions.csvEntry import addLine
import sys
# from mnmExtract import runGraph2356
path = '/Users/shifatsarwar/Downloads/Job/graphfunction/dataList/'
pathMain = '/Users/shifatsarwar/Downloads/Job/graphfunction/'       

def runGraph01to4(file1):
    array=[]
    graphNum = [1,2,3,4]
    updateValues=[file1, file1, file1, file1]
    step = [0,0,0,0]
    array.append(graphNum)
    array.append(updateValues)
    array.append(step)
    inputSize = os.path.getsize(file1)
    output = mixAndMatch.process1to4(array)
    outputValues = output[0]
    timeValues = output[1]
    index=0
    for x in outputValues:
        name = 'graph0'+str(graphNum[index])
        outputSize = sys.getsizeof(x)
        dataLine = name+',1,1,'+str(inputSize)+','+str(outputSize)+','+str(timeValues[index])+','+str(index)
        addLine(path+name+'.csv',dataLine)
        index=index+1


def runGraph05to8(file1, file2, file1E, file2E):
    array=[]
    inputFiles=[file1, file2]
    inputFiles2=[file1E, file2E]
    inputFiles3=[file1, file2]
    inputFiles4=[file1E, file2E]
    graphNum = [5,6,7,8]
    updateValues=[inputFiles,inputFiles2,inputFiles3,inputFiles4]
    step = [0,0,0,0]
    array.append(graphNum)
    array.append(updateValues)
    array.append(step)
    inputSize = os.path.getsize(file1)+os.path.getsize(file2)
    output = mixAndMatch.process5to8(array)
    outputValues = output[0]
    timeValues = output[1]
    index=4
    for x in outputValues:
        name = 'graph0'+str(graphNum[index-4])
        if(type(x)==str):
            outputSize = os.path.getsize(x)
        else:
            outputSize = sys.getsizeof(x)
        dataLine = name+',2,1,'+str(inputSize)+','+str(outputSize)+','+str(timeValues[index-4])+','+str(index)
        addLine(path+name+'.csv',dataLine)
        index=index+1


def runGraph09to12(file1, file2, file3, file1E, file2E, file3E):
    array=[]
    inputFiles=[file1, file2, file3]
    inputFiles2=[file1, file2, file3]
    inputFiles3=[file1E, file2E, file3E]
    inputFiles4=[file1E, file2E, file3E]
    graphNum = [9,10,11,12]
    updateValues=[inputFiles,inputFiles2,inputFiles3,inputFiles4]
    step = [0,0,0,0]
    array.append(graphNum)
    array.append(updateValues)
    array.append(step)
    inputSize = os.path.getsize(file1)+os.path.getsize(file2)+os.path.getsize(file3)
    output = mixAndMatch.process9to12(array)
    outputValues = output[0]
    timeValues = output[1]
    index=8
    for x in outputValues:
        name = 'graph0'+str(graphNum[index-8])
        if(type(x)==str):
            outputSize = os.path.getsize(x)
        else:
            outputSize = sys.getsizeof(x)
        dataLine = name+',3,1,'+str(inputSize)+','+str(outputSize)+','+str(timeValues[index-8])+','+str(index)
        addLine(path+name+'.csv',dataLine)
        index=index+1

def runGraphMnm(file1):
    array=[]
    graphNum = [1,2,3,4]
    updateValues=[file1, file1, file1, file1]
    step = [0,0,0,0]
    array.append(graphNum)
    array.append(updateValues)
    array.append(step)
    output = mixAndMatch.process1to4(array)
    return output[1]



def getRepeatedValues():
    count = 0
    tArray = []
    paththis = '/Users/shifatsarwar/Downloads/Job/graphfunction/arrayFiles/array1110.csv'
    print('Choosen input file size')
    print(os.path.getsize(paththis))
    while count < 10:
        tArray.append(runGraphMnm(paththis))
        count = count+1
    index = 1
    for x in tArray:
        print('------------------------------Case'+str(index)+'--------------------------------')
        print(x)
        print('--------------------------------------------------------------------------------')
        index = index+1


getRepeatedValues()