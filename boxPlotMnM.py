from mixandmatch import mnm, mixAndMatch
import time
import sys
import os
from random import choice
import random
from functions.csvEntry import addLine
path = '/Users/shifatsarwar/Downloads/Job/graphfunction/dataList/tests/'
dataPath = '/Users/shifatsarwar/Downloads/Job/graphfunction/dataList/arrayFiles/array111'
dataPath2 = '/Users/shifatsarwar/Downloads/Job/graphfunction/dataList/arrayFiles/array222'

def runMnM19(updateValues):
    steps = [0,0]
    graphNums = [1,2]
    weights = [25, 75]
    index = 4
    done = [] 
    timeStamps= [time.time(), time.time()]
    while index > 0:
        chooseFun = random.choices(graphNums, weights, k=1)
        chooseFun = chooseFun[0]
        if chooseFun in done:
            if chooseFun == 1:
                chooseFun = 2
            else:
                chooseFun = 1

        if chooseFun == 1:
            updateValues[0] = mnm.graph01(steps[0], updateValues[0])
            steps[0] = steps[0] + 1
            if steps[0] == 2:
                timeStamps[0] = time.time() - timeStamps[0]
                done.append(chooseFun)

        elif chooseFun == 2:
            updateValues[1] = mnm.graph09(steps[1], updateValues[1])
            steps[1] = steps[1] + 1
            if steps[1] == 2:
                timeStamps[1] = time.time() - timeStamps[1]
                done.append(chooseFun)
                        
        index = index-1
    array = []
    array.append(updateValues)
    array.append(timeStamps)
    return array

def runMnM24(updateValues):
    steps = [0,0]
    index = 4
    done = [] 
    timeStamps= [time.time(), time.time()]
    while index > 0:
        chooseFun = choice([1,2])
        if chooseFun in done:
            if chooseFun == 1:
                chooseFun = 2
            else:
                chooseFun = 1

        if chooseFun == 1:
            updateValues[0] = mixAndMatch.graph02(steps[0], updateValues[0])
            steps[0] = steps[0] + 1
            if steps[0] == 2:
                timeStamps[0] = time.time() - timeStamps[0]
                done.append(chooseFun)

        elif chooseFun == 2:
            updateValues[1] = mixAndMatch.graph04(steps[1], updateValues[1])
            steps[1] = steps[1] + 1
            if steps[1] == 2:
                timeStamps[1] = time.time() - timeStamps[1]
                done.append(chooseFun)
                        
        index = index-1
    array = []
    array.append(updateValues)
    array.append(timeStamps)
    return array

def runMnM18(updateValues):
    steps = [0,0]
    index = 4
    done = [] 
    timeStamps= [time.time(), time.time()]
    while index > 0:
        chooseFun = choice([1,2])
        if chooseFun in done:
            if chooseFun == 1:
                chooseFun = 2
            else:
                chooseFun = 1

        if chooseFun == 1:
            updateValues[0] = mnm.graph01(steps[0], updateValues[0])
            steps[0] = steps[0] + 1
            if steps[0] == 2:
                timeStamps[0] = time.time() - timeStamps[0]
                done.append(chooseFun)

        elif chooseFun == 2:
            updateValues[1] = mnm.graph08(steps[1], updateValues[1])
            steps[1] = steps[1] + 1
            if steps[1] == 2:
                timeStamps[1] = time.time() - timeStamps[1]
                done.append(chooseFun)
                        
        index = index-1
    
    array = []
    array.append(updateValues)
    array.append(timeStamps)
    return array

def genValGraph(runs):
    index = 0
    while index < runs:
        file1 = dataPath+str(index)+'.csv'
        graphNum = [1,2,3,4]
        updateValues=[file1, file1, file1, file1]
        inputSize = os.path.getsize(file1)
        output = mixAndMatch.process1234W(updateValues)
        outputValues = output[0]
        timeValues = output[1]
        index2 = 0
        for x in outputValues:
            name = 'graph0'+str(graphNum[index2])
            outputSize = sys.getsizeof(x)
            dataLine = name+',1,1,'+str(inputSize)+','+str(outputSize)+','+str(timeValues[index2])+','+str(graphNum[index2]-1)
            addLine(path+name+'.csv',dataLine)
            index2 = index2 + 1

        index = index + 1


def genValGraphSame(runs):
    index = 0
    while index < runs:
        file1 = dataPath+'1.csv'
        graphNum = [1,2,3,4]
        updateValues=[file1, file1, file1, file1]
        inputSize = os.path.getsize(file1)
        output = mixAndMatch.process1234W(updateValues)
        outputValues = output[0]
        timeValues = output[1]
        index2 = 0
        for x in outputValues:
            name = 'graph0'+str(graphNum[index2])
            outputSize = sys.getsizeof(x)
            dataLine = name+',1,1,'+str(inputSize)+','+str(outputSize)+','+str(timeValues[index2])+','+str(graphNum[index2]-1)
            addLine(path+name+'.csv',dataLine)
            index2 = index2 + 1

        index = index + 1

# Case 1 (2 MnMs with and without Sort diff input size) D
# Case 2 (2 MnMs both with sort diff input size) D
# For case 3 accuracy not required
# Case 3 (Normal execution with different input size)