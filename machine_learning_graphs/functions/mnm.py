from functions.imageEnhancement import *
from functions.objectDetection import *
from functions.simpleClustering import *
from functions.neuralNetwork import *
from functions.imageCaption import *
import random

#Updates weight values for mix and match
def updateWeight(weight, val):
    current = weight[val]
    weight[val] = 0
    remains = 0
    for x in weight:
        if x != 0:
            remains = remains+1
    if remains > 0:
        valDiv = current/remains
        index = 0
        while index < len(weight):
            if weight[index] != 0:
                weight[index] = weight[index]+valDiv
            index = index + 1
    return weight

# Recreates Nodes to allow easiern mixing of nodes
def graph01(step, output):
    if step == 0:
        output[0] = loadImageIE(output[0])    
    elif step == 1:
        output[0] = inverteIE(output[0])
    elif step == 2:
        output[0] = dehazeIE(output[0])
    elif step == 3:
        output = inverteIE(output[0])
    return output

def graph03(step, output):
    if step == 0:
        output[3] = getFramesOD(output[0], output[1])
    elif step == 1:
        output[3] = preProcessImageOD(output[3])
    elif step == 2:
        output[1] = getClassOD(output[0])
    elif step == 3:
        output[2] = getModelOD(output[0])
    elif step == 4:
        output = getBoundingBoxesOD(output[2], output[3], output[1])
    return output 

def graph08(step, output):
    if(step == 0):
        output[1] = loadModelIC()
    elif(step == 1):
        output[2] = loadTokenizerIC()
    elif(step == 2):
        output[3] = extract_featuresIC(output[0])
    elif(step == 3):
        output[0] = generate_descIC(output[1], output[2], output[3])
    elif(step == 4):
        # Change Output Location
        writeToFileIC(output[0])
        output = 'extra/output2.txt'
    return output

def graph09(step, output):
    if step == 0:
        X,y = preProcessNN(output[0])
        output[0] = X
        output[2] = y
    elif step == 1:
        X_train, X_test, y_train, y_test = train_test_split(output[0],output[2],test_size=0.2, random_state=3, stratify=output[2])
        output[0] = X_train
        output[2] = y_train
        output[3] = y_test
    elif step == 2:
        dummy_y, dummy_v = transformDataNN(output[2], output[3])
        output[2] = dummy_y
    elif step == 3:
        model = getModelNN(output[0], output[2])
        output = model
    return output

def graph10(step, output):
    if step == 0:
        X,y = preProcessCN(output[0])
        output[0] = X
        output[2] = y
    elif step == 1:
        X_train, X_test, y_train, y_test = train_test_split(output[0],output[2],test_size=0.2, random_state=3, stratify=output[2])
        output[0] = X_train
        output[2] = y_train
    elif step == 2:
        model = trainCN(output[0], output[2])
        output = model
    return output
 
def process2W(updateValues):
    steps = [0,0]
    # 1,10 = index:7, g1:step:4, g10:step:3
    # 3,9 = index:9, g3:step:5, g9:step:4
    # 1,8 = index:9, g1:step:4, g8:step:5
    # 8,10 = index:8, g8:step:5, g10:step:3
    # Change index based on graph
    index = 6
    graphNums = [1,2]
    weights = [50, 50]
    array = []
    timeStamps = [time.time(), time.time()]
    while index > 0:
        if sum(weights) > 0:
            chooseFun = random.choices(graphNums, weights, k=1)
            chooseFun = chooseFun[0]

        if chooseFun == 1:
            # Change Graph ID
            updateValues[0] = graph10(steps[0], updateValues[0])
            steps[0] = steps[0] + 1
            # Change step comparison based on graph
            if steps[0] == 3:
                timeStamps[0] = time.time() - timeStamps[0]
                weights = updateWeight(weights, 0)

        elif chooseFun == 2:
            # Change graph ID
            updateValues[1] = graph10(steps[1], updateValues[1])
            steps[1] = steps[1] + 1
            # Change step comparison based on graph
            if steps[1] == 3:
                timeStamps[1] = time.time() - timeStamps[1]
                weights = updateWeight(weights, 1) 
                
        index = index-1
    
    array.append(updateValues)
    array.append(timeStamps)
    return array


def process3W(updateValues):
    steps = [0,0,0]
    # 1,8,10 = index:12, g1:step:4, g8:step:5, g10:step:3
    # 3,9,10 = index:12, g3:step:5, g9:step:4, g10:step:3, 30:30:40
    # 1,3,8 = index:14, g1:step:4, g3:step:5, g8:step:5, 40:20:40
    # 1,9,10 = index:11, g1:step:4, g9:step:4, g10:step:3, 40:20:40
    # Change index based on graph
    index = 9
    graphNums = [1,2,3]
    weights = [40, 20, 40]
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
                weights = updateWeight(weights, 0)

        elif chooseFun == 2:
            updateValues[1] = graph10(steps[1], updateValues[1])
            steps[1] = steps[1] + 1
            # Change step comparison based on graph
            if steps[1] == 3:
                timeStamps[1] = time.time() - timeStamps[1]
                weights = updateWeight(weights, 1) 

        elif chooseFun == 3:
            updateValues[2] = graph10(steps[2], updateValues[2])
            steps[2] = steps[2] + 1
            # Change step comparison based on graph
            if steps[2] == 3:
                timeStamps[2] = time.time() - timeStamps[2]
                weights = updateWeight(weights, 2)
                        
        index = index-1

    array.append(updateValues)
    array.append(timeStamps)
    return array


# 
def process4W(updateValues):
    steps = [0,0,0,0]
    # 1,3,8,9 = index:18, g1:step:4, g3:step:5, g8:step:5, g09:step:4, 40:10:40:10
    # 1,3,9,10 = index:16, g1:step:4, g3:step:5, g9:step:4, g10:step:3, 40:10:10:40
    # 1,3,8,10 = index:17, g1:step:4, g3:step:5, g8:step:5, g10:step:3, 40:10:10:40
    # 1,8,9,10 = index:16, g1:step:4, g8:step:5, g9:step:4, g10:step:3, 40:10:10:40
    # Change index based on graph
    index = 12
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
                weights = updateWeight(weights, 0)

        elif chooseFun == 2:
            updateValues[1] = graph10(steps[1], updateValues[1])
            steps[1] = steps[1] + 1
            # Change step comparison based on graph
            if steps[1] == 3:
                timeStamps[1] = time.time() - timeStamps[1]
                weights = updateWeight(weights, 1)

        elif chooseFun == 3:
            updateValues[2] = graph10(steps[2], updateValues[2])
            steps[2] = steps[2] + 1
            # Change step comparison based on graph
            if steps[2] == 3:
                timeStamps[2] = time.time() - timeStamps[2]
                weights = updateWeight(weights, 2)

        elif chooseFun == 4:
            updateValues[3] = graph10(steps[3], updateValues[3])
            steps[3] = steps[3] + 1
            # Change step comparison based on graph
            if steps[3] == 3:
                timeStamps[3] = time.time() - timeStamps[3]
                weights = updateWeight(weights, 3)

        index = index-1

    array.append(updateValues)
    array.append(timeStamps)
    return array

def process5W(updateValues):
    steps = [0,0,0,0,0]
    # 1,3,8,9,10 = index:21, g1:step:4, g3:step:5, g8:step:5, g9:step:4, g10:step:3
    # Change index based on graph
    index = 21
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
                weights = updateWeight(weights, 0)

        elif chooseFun == 2:
            updateValues[1] = graph03(steps[1], updateValues[1])
            steps[1] = steps[1] + 1
            # Change step comparison based on graph
            if steps[1] == 5:
                timeStamps[1] = time.time() - timeStamps[1]
                weights = updateWeight(weights, 1)

        elif chooseFun == 3:
            updateValues[2] = graph08(steps[2], updateValues[2])
            steps[2] = steps[2] + 1
            # Change step comparison based on graph
            if steps[2] == 5:
                timeStamps[2] = time.time() - timeStamps[2]
                weights = updateWeight(weights, 2)

        elif chooseFun == 4:
            updateValues[3] = graph09(steps[3], updateValues[3])
            steps[3] = steps[3] + 1
            # Change step comparison based on graph
            if steps[3] == 3:
                timeStamps[3] = time.time() - timeStamps[3]
                weights = updateWeight(weights, 3)
        

        elif chooseFun == 5:
            updateValues[4] = graph10(steps[4], updateValues[4])
            steps[4] = steps[4] + 1
            # Change step comparison based on graph
            if steps[4] == 3:
                timeStamps[4] = time.time() - timeStamps[4]
                weights = updateWeight(weights, 4)

        index = index-1

    array.append(updateValues)
    array.append(timeStamps)
    return array
