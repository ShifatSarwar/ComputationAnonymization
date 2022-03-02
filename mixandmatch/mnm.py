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


def process189W(updateValues):
    steps = [0,0,0]
    index = 6
    graphNums = [1,2,3]
    weights = [25, 25, 50]
    array = []
    timeStamps = [time.time(), time.time(), time.time()]
    while index > 0:
        if sum(weights) > 0:
            chooseFun = random.choices(graphNums, weights, k=1)
            chooseFun = chooseFun[0]

        if chooseFun == 1:
            updateValues[0] = graph01(steps[0], updateValues[0])
            steps[0] = steps[0] + 1
            if steps[0] == 2:
                timeStamps[0] = time.time() - timeStamps[0]
                weights = updateWeight(weights, 0)

        elif chooseFun == 2:
            updateValues[1] = graph08(steps[1], updateValues[1])
            steps[1] = steps[1] + 1
            if steps[1] == 2:
                timeStamps[1] = time.time() - timeStamps[1]
                weights = updateWeight(weights, 1) 

        elif chooseFun == 3:
            updateValues[2] = graph09(steps[2], updateValues[2])
            steps[2] = steps[2] + 1
            if steps[2] == 2:
                timeStamps[2] = time.time() - timeStamps[2]
                weights = updateWeight(weights, 2)
        
                        
        index = index-1
    array.append(updateValues)
    array.append(timeStamps)
    return array

def process2356W(updateValues):
    steps = [0,0,0,0]
    index = 18
    graphNums = [1,2,3,4]
    weights = [25, 50, 12.5, 12.5]
    array = []
    timeStamps= [time.time(), time.time(), time.time(), time.time()]
    while index > 0:
        if sum(weights) > 0:
            chooseFun = random.choices(graphNums, weights, k=1)
            chooseFun = chooseFun[0]
        
        if chooseFun == 1:
            updateValues[0] = graph02(steps[0], updateValues[0])
            steps[0] = steps[0] + 1
            if steps[0] == 3:
                timeStamps[0] = time.time() - timeStamps[0]
                weights = updateWeight(weights, 0)

        elif chooseFun == 2:
            updateValues[1] = graph03(steps[1], updateValues[1])
            steps[1] = steps[1] + 1
            if steps[1] == 4:
                timeStamps[1] = time.time() - timeStamps[1]
                weights = updateWeight(weights, 1)

        elif chooseFun == 3:
            updateValues[2] = graph05(steps[2], updateValues[2])
            steps[2] = steps[2] + 1
            if steps[2] == 6:
                timeStamps[2] = time.time() - timeStamps[2]
                weights = updateWeight(weights, 2)

        elif chooseFun == 4:
            updateValues[3] = graph06(steps[3], updateValues[3])
            steps[3] = steps[3] + 1
            if steps[3] == 5:
                timeStamps[3] = time.time() - timeStamps[3]
                weights = updateWeight(weights, 3)

        index = index-1
    array.append(updateValues)
    array.append(timeStamps)
    return array


def process4710W(updateValues):
    steps = [0,0,0]
    index = 14
    graphNums = [1,2,3]
    weights = [50, 25, 25]
    array = []
    timeStamps= [time.time(), time.time(), time.time(), time.time()]
    while index > 0:
        if sum(weights) > 0:
            chooseFun = random.choices(graphNums, weights, k=1)
            chooseFun = chooseFun[0]
      
        if chooseFun == 1:
            updateValues[0] = graph04(steps[0], updateValues[0])
            steps[0] = steps[0] + 1
            if steps[0] == 2:
                timeStamps[0] = time.time() - timeStamps[0]
                weights = updateWeight(weights, 0)

        elif chooseFun == 2:
            updateValues[1] = graph07(steps[1], updateValues[1])
            steps[1] = steps[1] + 1
            if steps[1] == 5:
                timeStamps[1] = time.time() - timeStamps[1]
                weights = updateWeight(weights, 1)

        elif chooseFun == 3:
            updateValues[2] = graph10(steps[2], updateValues[2])
            steps[2] = steps[2] + 1
            if steps[2] == 7:
                timeStamps[2] = time.time() - timeStamps[2]
                weights = updateWeight(weights, 2)

        index = index-1
    array.append(updateValues)
    array.append(timeStamps)
    return array


# Code for 0 weights
# def process189(updateValues):
#     steps = [0,0,0]
#     index = 6
#     done = [] 
#     graphNums = [1,2,3]
#     array = []
#     timeStamps= [time.time(), time.time(), time.time()]
#     while index > 0:
#         if len(done) == 2:
#             check = [1,2,3]
#             for x in check:
#                 if x not in done:
#                     chooseFun = x
#         else:
#             chooseFun = random.choices(graphNums, weights=(25, 25, 50), k=1)
#             chooseFun = choices([i for i in range(1,3) if i not in done])
        
#         if chooseFun == 1:
#             updateValues[0] = graph01(steps[0], updateValues[0])
#             steps[0] = steps[0] + 1
#             if steps[0] == 2:
#                 timeStamps[0] = time.time() - timeStamps[0]
#                 done.append(chooseFun)

#         elif chooseFun == 2:
#             updateValues[1] = graph08(steps[1], updateValues[1])
#             steps[1] = steps[1] + 1
#             if steps[1] == 2:
#                 timeStamps[1] = time.time() - timeStamps[1]
#                 done.append(chooseFun)

#         elif chooseFun == 3:
#             updateValues[2] = graph09(steps[2], updateValues[2])
#             steps[2] = steps[2] + 1
#             if steps[2] == 2:
#                 timeStamps[2] = time.time() - timeStamps[2]
#                 done.append(chooseFun)
        
                        
#         index = index-1
#     array.append(updateValues)
#     array.append(timeStamps)
#     return array

# def process2356(updateValues):
#     steps = [0,0,0,0]
#     index = 18
#     done = [] 
#     array = []
#     timeStamps= [time.time(), time.time(), time.time(), time.time()]
#     while index > 0:
#         if len(done) == 3:
#             check = [1,2,3,4]
#             for x in check:
#                 if x not in done:
#                     chooseFun = x
#         else:
#             chooseFun = choice([i for i in range(1,4) if i not in done])
        
#         if chooseFun == 1:
#             updateValues[0] = graph02(steps[0], updateValues[0])
#             steps[0] = steps[0] + 1
#             if steps[0] == 3:
#                 timeStamps[0] = time.time() - timeStamps[0]
#                 done.append(chooseFun)

#         elif chooseFun == 2:
#             updateValues[1] = graph03(steps[1], updateValues[1])
#             steps[1] = steps[1] + 1
#             if steps[1] == 4:
#                 timeStamps[1] = time.time() - timeStamps[1]
#                 done.append(chooseFun)

#         elif chooseFun == 3:
#             updateValues[2] = graph05(steps[2], updateValues[2])
#             steps[2] = steps[2] + 1
#             if steps[2] == 6:
#                 timeStamps[2] = time.time() - timeStamps[2]
#                 done.append(chooseFun)

#         elif chooseFun == 4:
#             updateValues[3] = graph06(steps[3], updateValues[3])
#             steps[3] = steps[3] + 1
#             if steps[3] == 5:
#                 timeStamps[3] = time.time() - timeStamps[3]
#                 done.append(chooseFun)

#         index = index-1
#     array.append(updateValues)
#     array.append(timeStamps)
#     return array


# def process4710(updateValues):
#     steps = [0,0,0]
#     index = 14
#     done = [] 
#     array = []
#     timeStamps= [time.time(), time.time(), time.time(), time.time()]
#     while index > 0:
#         if len(done) == 2:
#             check = [1,2,3]
#             for x in check:
#                 if x not in done:
#                     chooseFun = x
#         else:
#             chooseFun = choice([i for i in range(1,3) if i not in done])
        
#         if chooseFun == 1:
#             updateValues[0] = graph04(steps[0], updateValues[0])
#             steps[0] = steps[0] + 1
#             if steps[0] == 2:
#                 timeStamps[0] = time.time() - timeStamps[0]
#                 done.append(chooseFun)

#         elif chooseFun == 2:
#             updateValues[1] = graph07(steps[1], updateValues[1])
#             steps[1] = steps[1] + 1
#             if steps[1] == 5:
#                 timeStamps[1] = time.time() - timeStamps[1]
#                 done.append(chooseFun)

#         elif chooseFun == 3:
#             updateValues[2] = graph10(steps[2], updateValues[2])
#             steps[2] = steps[2] + 1
#             if steps[2] == 7:
#                 timeStamps[2] = time.time() - timeStamps[2]
#                 done.append(chooseFun)
#         index = index-1
        
#     array.append(updateValues)
#     array.append(timeStamps)
#     return array