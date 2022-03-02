from functions import graphFunctions
from random import choice 
import random
import time


# 0 : GraphNum
# 1 : Updated Value
# 2 : Step of Program
# 3 : File Associated with Array(Can be array incase of multiple input)


def graph01(step, output):
    if step == 0:
        output = graphFunctions.getArray(output)
        return graphFunctions.sortArray(output)
    elif step == 1:
        return graphFunctions.calculateContentsSingle(output)

# Compress & Encrypt
def graph02(step, output):
    if step == 0:
        output = graphFunctions.getArray(output)
        return graphFunctions.compressGZip(output)
    elif step ==1:
        return graphFunctions.encryptAESFile(output)

# Sort & Encrypt
def graph03(step, output):
    if step == 0:
        output = graphFunctions.getArray(output)
        return graphFunctions.sortArray(output)
    elif step == 1:
        return graphFunctions.encryptAES(output)

# Calculate & Encrypt
def graph04(step, output):
    if step == 0:
        output = graphFunctions.getArray(output)
        return graphFunctions.calculateContentsSingle(output)
    elif step == 1:
        return graphFunctions.encryptAES(output)

# Sort Calculate Compress
def graph05(step, output):
    if step == 0:
        output[0] = graphFunctions.getArray(output[0])
        output[0] = graphFunctions.sortArray(output[0])
        output[1] = graphFunctions.getArray(output[1])
        output[1] = graphFunctions.sortArray(output[1])
        return output
    elif step == 1:
        # output = graphFunctions.fixLength(output[0],output[1])
        return graphFunctions.calculateContents(output[0], output[1])
    elif step == 2:
        return graphFunctions.compressGZip(output)

# Decrypt Calculate Encrypt
def graph06(step, output):
    if step == 0:
        output[0]=graphFunctions.decryptAES(output[0])
        output[1]=graphFunctions.decryptAES(output[1])
        return output
    elif step == 1:
        output = graphFunctions.fixLength(output[0], output[1])
        return graphFunctions.calculateContents(output[0], output[1])
    elif step == 2:
        return graphFunctions.encryptAES(output)

# Calculate Compress
def graph07(step, output):
    if step == 0:
        output[0] = graphFunctions.getArray(output[0])
        output[0] = graphFunctions.calculateContentsSingle(output[0])
        output[1] = graphFunctions.getArray(output[1])
        output[1] = graphFunctions.calculateContentsSingle(output[1])
        return output
    elif step == 1:
        # output = graphFunctions.fixLength(output[0], output[1])
        return graphFunctions.calculateContents(output[0], output[1])
    elif step == 2:
        return graphFunctions.compressGZip(output)
    
# Sort Decrypt Compress Calculate Encrypt
def graph08(step, output):
    if step == 0:
        output[0]=graphFunctions.decryptAES(output[0])
        output[1]=graphFunctions.decryptAES(output[1])
        return output
    elif step == 1:
        output = graphFunctions.fixLength(output[0], output[1])
        output[0] = graphFunctions.sortArray(output[0])
        output[1] = graphFunctions.sortArray(output[1])
        return output
    elif step == 2:
        return graphFunctions.calculateContents(output[0], output[1])
    elif step == 3:
        return graphFunctions.compressGZip(output)
    elif step == 4:
        return graphFunctions.encryptAESFile(output)

# Sort Calculate
def graph09(step, output):
    if step == 0:
        output[0] = graphFunctions.getArray(output[0])
        output[0] = graphFunctions.sortArray(output[0])
        output[1] = graphFunctions.getArray(output[1])
        output[1] = graphFunctions.sortArray(output[1])
        output[2] = graphFunctions.getArray(output[2])
        output[2] = graphFunctions.sortArray(output[2])
        return output
    elif step == 1:
        # output = graphFunctions.fixLengthAll(output[0], output[1], output[2])
        output[0] = graphFunctions.calculateContents(output[0], output[1])
        return graphFunctions.calculateContents(output[0], output[2])

# Calculate Compress Encrypt
def graph10(step, output):
    if step == 0:
        output[0] = graphFunctions.getArray(output[0])
        output[1] = graphFunctions.getArray(output[1])
        output[2] = graphFunctions.getArray(output[2])
        output[0] = graphFunctions.calculateContents(output[0], output[1])
        return graphFunctions.calculateContents(output[0], output[2])
    if step == 1:
        return graphFunctions.compressGZip(output)
    elif step == 2:
        return graphFunctions.encryptAESFile(output)

# Sort Decrypt Compress Calculate Encrypt
def graph11(step, output):
    if step == 0:
        output[0] = graphFunctions.decryptAES(output[0])
        output[1] = graphFunctions.decryptAES(output[1])
        output[2] = graphFunctions.decryptAES(output[2])
        return output
    elif step == 1:
        output = graphFunctions.fixLengthAll(output[0], output[1], output[2])
        output[0] = graphFunctions.sortArray(output[0])
        output[1] = graphFunctions.sortArray(output[1])
        output[2] = graphFunctions.sortArray(output[2])
        return output
    elif step == 2:
        output[0] = graphFunctions.calculateContents(output[0], output[1])
        return graphFunctions.calculateContents(output[0], output[2])
    elif step == 3:
        return graphFunctions.compressGZip(output)
    elif step == 4:
        return graphFunctions.encryptAESFile(output)


# Decrypt Calculate Encrypt
def graph12(step, output):
    if step == 0:
        output[0] = graphFunctions.decryptAES(output[0])
        output[1] = graphFunctions.decryptAES(output[1])
        output[2] = graphFunctions.decryptAES(output[2])
        return output
    elif step == 1:
        output = graphFunctions.fixLengthAll(output[0], output[1], output[2])
        output[0] = graphFunctions.calculateContentsSingle(output[0])
        output[1] = graphFunctions.calculateContentsSingle(output[1])
        output[2] = graphFunctions.calculateContentsSingle(output[2])
        return output
    elif step == 2:
        output[0] = graphFunctions.calculateContents(output[0], output[1])
        return graphFunctions.calculateContents(output[0], output[2])
    elif step == 3:
        return graphFunctions.encryptAES(output)



def process1to4(updateValues):
    steps = [0,0,0,0]
    index = 8
    done = [] 
    array = []
    timeStamps= [time.time(), time.time(), time.time(), time.time()]
    while index > 0:
        if len(done) == 3:
            check = [1,2,3,4]
            for x in check:
                if x not in done:
                    chooseFun = x
        else:
            chooseFun = choice([i for i in range(1,4) if i not in done])
        if chooseFun == 1:
            updateValues[0] = graph01(steps[0], updateValues[0])
            steps[0] = steps[0] + 1
            if steps[0] == 2:
                timeStamps[0] = time.time() - timeStamps[0]
                done.append(chooseFun)

        elif chooseFun == 2:
            updateValues[1] = graph02(steps[1], updateValues[1])
            steps[1] = steps[1] + 1
            if steps[1] == 2:
                timeStamps[1] = time.time() - timeStamps[1]
                done.append(chooseFun)

        elif chooseFun == 3:
            updateValues[2] = graph03(steps[2], updateValues[2])
            steps[2] = steps[2] + 1
            if steps[2] == 2:
                timeStamps[2] = time.time() - timeStamps[2]
                done.append(chooseFun)
        
        elif chooseFun == 4:
            updateValues[3] = graph04(steps[3], updateValues[3])
            steps[3] = steps[3] + 1
            if steps[3] == 2:
                timeStamps[3] = time.time() - timeStamps[3]
                done.append(chooseFun)
        
        index = index-1

    array.append(updateValues)
    array.append(timeStamps)
    return array

def process5to8(array):
    index = 14
    done = [] 
    numbers = array[0]
    updateValues = array[1]
    steps = array[2]
    array = []
    timeStamps= [time.time(), time.time(), time.time(), time.time()]
    while index>0:
        if len(done) == 3:
            check = [5,6,7,8]
            for x in check:
                if x not in done:
                    chooseFun = x
        else:
            chooseFun = choice([i for i in range(5,8) if i not in done])
        for x in numbers:
            if x == chooseFun:
                if chooseFun == 5:
                    updateValues[0]=graph05(steps[0], updateValues[0])
                    steps[0]= steps[0]+1
                    if steps[0] == 3:
                        timeStamps[0] = time.time() - timeStamps[0]
                        done.append(chooseFun)

                elif chooseFun == 6:
                    updateValues[1]=graph06(steps[1], updateValues[1])
                    steps[1]= steps[1]+1
                    if steps[1] == 3:
                        timeStamps[1] = time.time() - timeStamps[1]
                        done.append(chooseFun)

                elif chooseFun == 7:
                    updateValues[2]=graph07(steps[2], updateValues[2])
                    steps[2]= steps[2]+1
                    if steps[2] == 3:
                        timeStamps[2] = time.time() - timeStamps[2]
                        done.append(chooseFun)
                
                elif chooseFun == 8:
                    updateValues[3]=graph08(steps[3], updateValues[3])
                    steps[3]= steps[3]+1
                    if steps[3] == 5:
                        timeStamps[3] = time.time() - timeStamps[3]
                        done.append(chooseFun)
        index = index-1
    array.append(updateValues)
    array.append(timeStamps)
    return array
    
def process9to12(array):
    index = 14
    done = [] 
    numbers = array[0]
    updateValues = array[1]
    steps = array[2]
    array = []
    timeStamps= [time.time(), time.time(), time.time(), time.time()]
    while index>0:
        if len(done) == 3:
            check = [9,10,11,12]
            for x in check:
                if x not in done:
                    chooseFun = x
        else:
            chooseFun = choice([i for i in range(9,12) if i not in done])
        for x in numbers:
            if x == chooseFun:
                if chooseFun == 9:
                    updateValues[0]=graph09(steps[0], updateValues[0])
                    steps[0]= steps[0]+1
                    if steps[0] == 2:
                        timeStamps[0] = time.time() - timeStamps[0]
                        done.append(chooseFun)

                elif chooseFun == 10:
                    updateValues[1]=graph10(steps[1], updateValues[1])
                    steps[1]= steps[1]+1
                    if steps[1] == 3:
                        timeStamps[1] = time.time() - timeStamps[1]
                        done.append(chooseFun)

                elif chooseFun == 11:
                    updateValues[2]=graph11(steps[2], updateValues[2])
                    steps[2]= steps[2]+1
                    if steps[2] == 5:
                        timeStamps[2] = time.time() - timeStamps[2]
                        done.append(chooseFun)
                
                elif chooseFun == 12:
                    updateValues[3]=graph12(steps[3], updateValues[3])
                    steps[3]= steps[3]+1
                    if steps[3] == 4:
                        timeStamps[3] = time.time() - timeStamps[3]
                        done.append(chooseFun)
        index = index-1
    array.append(updateValues)
    array.append(timeStamps)
    return array


def process1234W(updateValues):
    steps = [0,0,0, 0]
    index = 8
    graphNums = [1,2,3,4]
    weights = [15, 25, 15, 45]
    array = []
    timeStamps = [time.time(), time.time(), time.time(), time.time()]
    while index > 0:
        if sum(weights) > 0:
            chooseFun = random.choices(graphNums, weights, k=1)
            chooseFun = chooseFun[0]

        if chooseFun == 1:
            updateValues[0] = graph01(steps[0], updateValues[0])
            steps[0] = steps[0] + 1
            if steps[0] == 2:
                timeStamps[0] = time.time() - timeStamps[0]
                weights = graphFunctions.updateWeight(weights, 0)

        elif chooseFun == 2:
            updateValues[1] = graph02(steps[1], updateValues[1])
            steps[1] = steps[1] + 1
            if steps[1] == 2:
                timeStamps[1] = time.time() - timeStamps[1]
                weights = graphFunctions.updateWeight(weights, 1) 

        elif chooseFun == 3:
            updateValues[2] = graph03(steps[2], updateValues[2])
            steps[2] = steps[2] + 1
            if steps[2] == 2:
                timeStamps[2] = time.time() - timeStamps[2]
                weights = graphFunctions.updateWeight(weights, 2)
        
        elif chooseFun == 4:
            updateValues[3] = graph04(steps[3], updateValues[3])
            steps[3] = steps[3] + 1
            if steps[3] == 2:
                timeStamps[3] = time.time() - timeStamps[3]
                weights = graphFunctions.updateWeight(weights, 3)
        
                        
        index = index-1
    array.append(updateValues)
    array.append(timeStamps)
    return array