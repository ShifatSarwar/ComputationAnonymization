from functions import graphFunctions
import time
from random  import choices, choice
import random

def graph01(step,output):
    # Calculate Sort 
    # output = graphFunctions.decryptAES(output1)
    if step == 0:
        output = graphFunctions.getArray(output)
        return graphFunctions.sortArray(output)
    elif step == 1:
        return graphFunctions.calculateContentsSingle(output)
    # output = graphFunctions.encryptAES(output)

def graph02(step, output):
    # Sort Calculate Compress
    # output1 = graphFunctions.decryptAES(output1)
    # output2 = graphFunctions.decryptAES(output2)
    if step == 0:
        output[0] = graphFunctions.getArray(output[0])
        output[1] = graphFunctions.getArray(output[1])
        output[1] = graphFunctions.sortArray(output[1])
        return output
    # output = graphFunctions.fixLength(output1, output2)
    elif step == 1:
        return graphFunctions.calculateContents(output[0], output[1])
    elif step == 2:
        return graphFunctions.compressGZip(output)
    # output = graphFunctions.encryptAESFile(output)

def graph03(step, output):
    # Decrypt Calculate Encrypt
    if step == 0:
        output[0] = graphFunctions.decryptAES(output[0])
        return output
    elif step == 1:
        output[1] = graphFunctions.decryptAES(output[1])
        return output
    elif step == 2:
        output = graphFunctions.fixLength(output[0], output[1])
        return graphFunctions.calculateContents(output[0], output[1])
    elif step == 3:
        return graphFunctions.encryptAES(output)

def graph04(step, output):
    # Calculate Compress
    # output1 = graphFunctions.decryptAES(output1)
    # output3 = graphFunctions.decryptAES(output3)
    # output = graphFunctions.fixLength(output1, output3)
    if step == 0:
        output[0] = graphFunctions.getArray(output[0])
        output[1] = graphFunctions.getArray(output[1])
        output[2] = graphFunctions.getArray(output[2])
        output[0] = graphFunctions.calculateContents(output[0], output[1])
    # output2 = graphFunctions.decryptAES(output2)
    # output = graphFunctions.fixLength(output, output2)
        return graphFunctions.calculateContents(output[0], output[2])
    elif step == 1:
        return graphFunctions.compressGZip(output)
    # output = graphFunctions.encryptAESFile(output)

def graph05(step, output):
    # Decrypt Sort Compress Encrypt
    if step == 0:
        output[0] = graphFunctions.decryptAES(output[0])
        return output
    elif step == 1:
        output[1] = graphFunctions.decryptAES(output[1])
        return output
    elif step == 2:
        output[0] = graphFunctions.sortArray(output[0])
        return output
    elif step == 3:
        output[1] = graphFunctions.sortArray(output[1])
        return output
    elif step == 4:
        return graphFunctions.compressGZip(output)
    elif step == 5:
        return graphFunctions.encryptAESFile(output)

def graph06(step, output):
    # Decrypt Sort Encrypt
    if step == 0:
        output[0] = graphFunctions.decryptAES(output[0])
        return output
    elif step == 1:
        output[1] = graphFunctions.decryptAES(output[1])
        return output
    elif step == 2:
        output[0] = graphFunctions.sortArray(output[0])
        return output
    elif step == 3:
        output[1] = graphFunctions.sortArray(output[1])
        return output
    elif step == 4:
        return graphFunctions.encryptAES(output)

def graph07(step, output):
    # Sort Compress Encrypt
    # output1 = graphFunctions.decryptAES(output1)
    # output2 = graphFunctions.decryptAES(output2)
    # output3 = graphFunctions.decryptAES(output3)
    if step == 0:
        output[0] = graphFunctions.getArray(output[0])
        output[0] = graphFunctions.sortArray(output[0])
        return output
    elif step == 1:
        output[1] = graphFunctions.getArray(output[1])
        output[1] = graphFunctions.sortArray(output[1])
        return output
    elif step == 2:
        output[2] = graphFunctions.getArray(output[2])
        output[2] = graphFunctions.sortArray(output[2])
        return output
    elif step == 3:
        return graphFunctions.compressGZip(output)
    elif step == 4:
        return graphFunctions.encryptAESFile(output)

def graph08(step, output):
    # Sort Encrypt
    # output = graphFunctions.decryptAES(file)
    if step == 0:
        output = graphFunctions.getArray(output)
        output = graphFunctions.sortArray2(output)
        return output
    elif step == 1:
        return graphFunctions.encryptAES(output)

def graph09(step, output):
    # Compress Encrypt
    # output = graphFunctions.decryptAES(output)
    if step == 0:
        output = graphFunctions.getArray(output)
        output = graphFunctions.compressGZip(output)
        return output
    elif step == 1:
        return graphFunctions.encryptAESFile(output)

def graph10(step, output):
    # Decrypt Calculate Sort Compress
    if step == 0:
        output[0] = graphFunctions.decryptAES(output[0])
        return output
    elif step == 1:
        output[1] = graphFunctions.decryptAES(output[1])
        return output
    elif step == 2:
        output[2] = graphFunctions.decryptAES(output[2])
        return graphFunctions.fixLengthAll(output[0], output[1], output[2])
    elif step == 3:
        output[0] = graphFunctions.sortArray(output[0])
        return output
    elif step == 4:
        output[0] = graphFunctions.calculateContents(output[0], output[1])
        return graphFunctions.calculateContents(output[0], output[2])
    elif step == 5:
        return graphFunctions.compressGZip(output)
    elif step == 6:
        return graphFunctions.encryptAESFile(output)


# g1:step:2, g2:step:3, g3:step:4,
# g4:step:2, g5:step:5, g6:step:5,
# g7:step:6, g8:step:5, g9:step:5,
# g10:step:7

def process2W(updateValues, level, index):
    steps = [0,0,0]    
    # Change index based on graph step add
    index = 9
    index += level
    graphNums = [1,2,3]
    weights = [40, 30, 30]
    array = []
    timeStamps = [time.time(), time.time(), time.time()]
    while index > 0:
        if sum(weights) > 0:
            chooseFun = random.choices(graphNums, weights, k=1)
            chooseFun = chooseFun[0]

        if chooseFun == 1:
            updateValues[0] = graph10(steps[0], updateValues[0])
            steps[0] = steps[0] + 1
            # Change step comparison based on graph
            if steps[0] == 3:
                timeStamps[0] = time.time() - timeStamps[0]
                weights = graphFunctions.updateWeight(weights, 0)

        elif chooseFun == 2:
            updateValues[1] = graph10(steps[1], updateValues[1])
            steps[1] = steps[1] + 1
            # Change step comparison based on graph
            if steps[1] == 3:
                timeStamps[1] = time.time() - timeStamps[1]
                weights = graphFunctions.updateWeight(weights, 1) 
        
        # Runs anonymization as another mixed entity that could be chosen
        # at random
        elif chooseFun == 3:
            steps[2] = steps[2] + 1
            graphFunctions.doNothing()
            # Change step comparison based on graph
            if steps[2] == level:
                timeStamps[2] = time.time() - timeStamps[2]
                weights = graphFunctions.updateWeight(weights, 2)
                        
        index = index-1

    array.append(updateValues, level)
    array.append(timeStamps)
    return array

 
def process3W(updateValues, level):
    steps = [0,0,0,0]
    # Change index based on graph
    index = 12
    index += level
    graphNums = [1,2,3,4]
    weights = [40, 10, 40, 10]
    array = []
    timeStamps= [time.time(), time.time(), time.time(), time.time()]
    while index > 0:
        if sum(weights) > 0:
            chooseFun = random.choices(graphNums, weights, k=1)
            chooseFun = chooseFun[0]
        
        if chooseFun == 1:
            updateValues[0] = graph10(steps[0], updateValues[0])
            steps[0] = steps[0] + 1
            # Change step comparison based on graph
            if steps[0] == 3:
                timeStamps[0] = time.time() - timeStamps[0]
                weights = graphFunctions.updateWeight(weights, 0)

        elif chooseFun == 2:
            updateValues[1] = graph10(steps[1], updateValues[1])
            steps[1] = steps[1] + 1
            # Change step comparison based on graph
            if steps[1] == 3:
                timeStamps[1] = time.time() - timeStamps[1]
                weights = graphFunctions.updateWeight(weights, 1)

        elif chooseFun == 3:
            updateValues[2] = graph10(steps[2], updateValues[2])
            steps[2] = steps[2] + 1
            # Change step comparison based on graph
            if steps[2] == 3:
                timeStamps[2] = time.time() - timeStamps[2]
                weights = graphFunctions.updateWeight(weights, 2)

        elif chooseFun == 4:
            steps[3] = steps[3] + 1
            graphFunctions.doNothing()
            # Change step comparison based on graph
            if steps[3] == level:
                timeStamps[3] = time.time() - timeStamps[2]
                weights = graphFunctions.updateWeight(weights, 3)

        index = index-1

    array.append(updateValues, level)
    array.append(timeStamps)
    return array

def process4W(updateValues, level):
    steps = [0,0,0,0,0]
    # Change index based on graph
    index = 21
    index += level
    graphNums = [1,2,3,4,5]
    weights = [30, 5, 30, 5, 30]
    array = []
    timeStamps= [time.time(), time.time(), time.time(), time.time(), time.time()]
    while index > 0:
        if sum(weights) > 0:
            chooseFun = random.choices(graphNums, weights, k=1)
            chooseFun = chooseFun[0]
        
        if chooseFun == 1:
            updateValues[0] = graph01(steps[0], updateValues[0])
            steps[0] = steps[0] + 1
            # Change step comparison based on graph
            if steps[0] == 4:
                timeStamps[0] = time.time() - timeStamps[0]
                weights = graphFunctions.updateWeight(weights, 0)

        elif chooseFun == 2:
            updateValues[1] = graph03(steps[1], updateValues[1])
            steps[1] = steps[1] + 1
            # Change step comparison based on graph
            if steps[1] == 5:
                timeStamps[1] = time.time() - timeStamps[1]
                weights = graphFunctions.updateWeight(weights, 1)

        elif chooseFun == 3:
            updateValues[2] = graph08(steps[2], updateValues[2])
            steps[2] = steps[2] + 1
            # Change step comparison based on graph
            if steps[2] == 5:
                timeStamps[2] = time.time() - timeStamps[2]
                weights = graphFunctions.updateWeight(weights, 2)

        elif chooseFun == 4:
            updateValues[3] = graph09(steps[3], updateValues[3])
            steps[3] = steps[3] + 1
            # Change step comparison based on graph
            if steps[3] == 3:
                timeStamps[3] = time.time() - timeStamps[3]
                weights = graphFunctions.updateWeight(weights, 3)
        

        elif chooseFun == 5:
            steps[4] = steps[4] + 1
            graphFunctions.doNothing()
            # Change step comparison based on graph
            if steps[4] == 3:
                timeStamps[4] = time.time() - timeStamps[4]
                weights = graphFunctions.updateWeight(weights, 4)

        index = index-1

    array.append(updateValues, level)
    array.append(timeStamps)
    return array
