import random
import csv
from utility import addLine
g1 = 'dataList/Alibaba/mixing/g1.csv'
g2 = 'dataList/Alibaba/mixing/g2.csv'
g3 = 'dataList/Alibaba/mixing/g3.csv'
g4 = 'dataList/Alibaba/mixing/g4.csv'
g5 = 'dataList/Alibaba/mixing/g5.csv'
g6 = 'dataList/Alibaba/mixing/g6.csv'
g7 = 'dataList/Alibaba/mixing/g7.csv'
g8 = 'dataList/Alibaba/mixing/g8.csv'
g9 = 'dataList/Alibaba/mixing/g9.csv'
g10 = 'dataList/Alibaba/mixing/g10.csv'
 
r1 = 'dataList/Alibaba/mixing/weighted/mix5/g1.csv'
r2 = 'dataList/Alibaba/mixing/weighted/mix5/g2.csv'
r3 = 'dataList/Alibaba/mixing/weighted/mix5/g3.csv'
r4 = 'dataList/Alibaba/mixing/weighted/mix5/g4.csv'
r5 = 'dataList/Alibaba/mixing/weighted/mix5/g5.csv'



#Updates weight values for mix and match
def updateWeight(weight, val):
    current = weight[val]
    weight[val] = 0
    remains = 0
    for x in weight:
        if x != 0:
            remains = remains+1
    
    if remains == 0:
        return weight
    if remains > 0:
        valDiv = current/remains
        index = 0
        while index < len(weight):
            if weight[index] != 0:
                weight[index] = weight[index]+int(valDiv)
            index = index + 1
        extra = 100 - sum(weight)
    
    index = 0
    while index < len(weight):
        if weight[index] != 0 and weight[index]!=2:
            weight[index] = weight[index]+extra
            break
        index = index + 1
    return weight



def mix2W():
    array1 = []
    with open(g1) as f:
        reader = csv.reader(f) 
        for row in reader: 
            array1.append(row)
    array2 = []
    with open(g2) as f:
        reader = csv.reader(f) 
        for row in reader: 
            array2.append(row)
    
    index = 0
    
    # Considering Single Node for Mix and Matches
    # CPU for the largest chosen
    while index < 1500:
        done = []
        currTime = 0
        if array1[index][3] == "timeTaken":
            index = index + 1
        graphNums = [1,2]
        weights = [75, 25]
        a0 = array1[index]
        a1 = array2[index]
        cpuVal = [int(float(a0[5])), int(float(a1[5]))]
        while True:
            if sum(weights) > 0:
                chooseFun = random.choices(graphNums, weights, k=1)
                chooseFun = chooseFun[0]
            else:
                break

            if chooseFun == 1:
                if (chooseFun not in done) :
                    currTime = currTime + int(a0[3]) 
                    a0[3] = str(currTime)
                    a0[5] = str(max(cpuVal))
                    dataLine = a0[0]+","+a0[1]+","+a0[2]+","+a0[3]+","+a0[4]+","+a0[5]+","+a0[6]
                    addLine(r1,dataLine)
                    weights = updateWeight(weights, 0)
                    done.append(1)
                else:
                    break


            elif chooseFun == 2:
                if (chooseFun not in done) :
                    currTime = currTime + int(a1[3]) 
                    a1[3] = str(currTime)
                    a1[5] = str(max(cpuVal))
                    dataLine = a1[0]+","+a1[1]+","+a1[2]+","+a1[3]+","+a1[4]+","+a1[5]+","+a1[6]
                    addLine(r2,dataLine)
                    weights = updateWeight(weights, 1)
                    done.append(2)
                else:
                    break
        index = index + 1

def mix3W():
    array1 = []
    with open(g1) as f:
        reader = csv.reader(f) 
        for row in reader: 
            array1.append(row)
    array2 = []
    with open(g2) as f:
        reader = csv.reader(f) 
        for row in reader: 
            array2.append(row)
    
    array3 = []
    with open(g3) as f:
        reader = csv.reader(f) 
        for row in reader: 
            array3.append(row)
    
    index = 0
    
    # Considering Single Node for Mix and Matches
    # CPU for the largest chosen
    while index < 1500:
        done = []
        currTime = 0
        if array1[index][3] == "timeTaken":
            index = index + 1
        graphNums = [1,2,3]
        weights = [40, 20, 40]
        a0 = array1[index]
        a1 = array2[index]
        a2 = array3[index]
        cpuVal = [int(float(a0[5])), int(float(a1[5])), int(float(a2[5]))]
        while True:
            if sum(weights) > 0:
                chooseFun = random.choices(graphNums, weights, k=1)
                chooseFun = chooseFun[0]
            else:
                break

            if chooseFun == 1:
                if (chooseFun not in done) :
                    currTime = currTime + int(a0[3]) 
                    a0[3] = str(currTime)
                    a0[5] = str(max(cpuVal))
                    dataLine = a0[0]+","+a0[1]+","+a0[2]+","+a0[3]+","+a0[4]+","+a0[5]+","+a0[6]
                    addLine(r1,dataLine)
                    weights = updateWeight(weights, 0)
                    done.append(1)
                else:
                    break


            elif chooseFun == 2:
                if (chooseFun not in done) :
                    currTime = currTime + int(a1[3]) 
                    a1[3] = str(currTime)
                    a1[5] = str(max(cpuVal))
                    dataLine = a1[0]+","+a1[1]+","+a1[2]+","+a1[3]+","+a1[4]+","+a1[5]+","+a1[6]
                    addLine(r2,dataLine)
                    weights = updateWeight(weights, 1)
                    done.append(2)
                else:
                    break

            elif chooseFun == 3:
                if (chooseFun not in done) :
                    currTime = currTime + int(a2[3]) 
                    a2[3] = str(currTime)
                    a2[5] = str(max(cpuVal))
                    dataLine = a2[0]+","+a2[1]+","+a2[2]+","+a2[3]+","+a2[4]+","+a2[5]+","+a2[6]
                    addLine(r3,dataLine)
                    weights = updateWeight(weights, 2)
                    done.append(3)
                else:
                    break
        index = index + 1

def mix4W():
    array1 = []
    with open(g1) as f:
        reader = csv.reader(f) 
        for row in reader: 
            array1.append(row)
    array2 = []
    with open(g2) as f:
        reader = csv.reader(f) 
        for row in reader: 
            array2.append(row)
    
    array3 = []
    with open(g3) as f:
        reader = csv.reader(f) 
        for row in reader: 
            array3.append(row)
    
    array4 = []
    with open(g5) as f:
        reader = csv.reader(f) 
        for row in reader: 
            array4.append(row)
    
    index = 0
    
    # Considering Single Node for Mix and Matches
    # CPU for the largest chosen
    while index < 1500:
        done = []
        currTime = 0
        if array1[index][3] == "timeTaken":
            index = index + 1
        graphNums = [1,2,3,4]
        weights = [40, 10, 30, 20]
        a0 = array1[index]
        a1 = array2[index]
        a2 = array3[index]
        a3 = array4[index]
        cpuVal = [int(float(a0[5])), int(float(a1[5])), int(float(a2[5])), int(float(a3[5]))]
        while True:
            if sum(weights) > 0:
                chooseFun = random.choices(graphNums, weights, k=1)
                chooseFun = chooseFun[0]
            else:
                break

            if chooseFun == 1:
                if (chooseFun not in done) :
                    currTime = currTime + int(a0[3]) 
                    a0[3] = str(currTime)
                    a0[5] = str(max(cpuVal))
                    dataLine = a0[0]+","+a0[1]+","+a0[2]+","+a0[3]+","+a0[4]+","+a0[5]+","+a0[6]
                    addLine(r1,dataLine)
                    weights = updateWeight(weights, 0)
                    done.append(1)
                else:
                    break


            elif chooseFun == 2:
                if (chooseFun not in done) :
                    currTime = currTime + int(a1[3]) 
                    a1[3] = str(currTime)
                    a1[5] = str(max(cpuVal))
                    dataLine = a1[0]+","+a1[1]+","+a1[2]+","+a1[3]+","+a1[4]+","+a1[5]+","+a1[6]
                    addLine(r2,dataLine)
                    weights = updateWeight(weights, 1)
                    done.append(2)
                else:
                    break

            elif chooseFun == 3:
                if (chooseFun not in done) :
                    currTime = currTime + int(a2[3]) 
                    a2[3] = str(currTime)
                    a2[5] = str(max(cpuVal))
                    dataLine = a2[0]+","+a2[1]+","+a2[2]+","+a2[3]+","+a2[4]+","+a2[5]+","+a2[6]
                    addLine(r3,dataLine)
                    weights = updateWeight(weights, 2)
                    done.append(3)
                else:
                    break
            
            elif chooseFun == 4:
                if (chooseFun not in done) :
                    currTime = currTime + int(a3[3]) 
                    a3[3] = str(currTime)
                    a3[5] = str(max(cpuVal))
                    dataLine = a3[0]+","+a3[1]+","+a3[2]+","+a3[3]+","+a3[4]+","+a3[5]+","+a3[6]
                    addLine(r4,dataLine)
                    weights = updateWeight(weights, 3)
                    done.append(4)
                else:
                    break
        index = index + 1

def mix5W():
    array1 = []
    with open(g1) as f:
        reader = csv.reader(f) 
        for row in reader: 
            array1.append(row)
    array2 = []
    with open(g2) as f:
        reader = csv.reader(f) 
        for row in reader: 
            array2.append(row)
    
    array3 = []
    with open(g3) as f:
        reader = csv.reader(f) 
        for row in reader: 
            array3.append(row)
    
    array4 = []
    with open(g5) as f:
        reader = csv.reader(f) 
        for row in reader: 
            array4.append(row)

    array5 = []
    with open(g6) as f:
        reader = csv.reader(f) 
        for row in reader: 
            array5.append(row)
    
    index = 0
    
    # Considering Single Node for Mix and Matches
    # CPU for the largest chosen
    while index < 1500:
        done = []
        currTime = 0
        if array1[index][3] == "timeTaken":
            index = index + 1
        graphNums = [1,2,3,4,5]
        weights = [30, 10, 25, 20, 15]
        a0 = array1[index]
        a1 = array2[index]
        a2 = array3[index]
        a3 = array4[index]
        a4 = array5[index]
        cpuVal = [int(float(a0[5])), int(float(a1[5])), int(float(a2[5])), int(float(a3[5])), int(float(a4[5]))]
        while True:
            if sum(weights) > 0:
                chooseFun = random.choices(graphNums, weights, k=1)
                chooseFun = chooseFun[0]
            else:
                break

            if chooseFun == 1:
                if (chooseFun not in done) :
                    currTime = currTime + int(a0[3]) 
                    a0[3] = str(currTime)
                    a0[5] = str(max(cpuVal))
                    dataLine = a0[0]+","+a0[1]+","+a0[2]+","+a0[3]+","+a0[4]+","+a0[5]+","+a0[6]
                    addLine(r1,dataLine)
                    weights = updateWeight(weights, 0)
                    done.append(1)
                else:
                    break


            elif chooseFun == 2:
                if (chooseFun not in done) :
                    currTime = currTime + int(a1[3]) 
                    a1[3] = str(currTime)
                    a1[5] = str(max(cpuVal))
                    dataLine = a1[0]+","+a1[1]+","+a1[2]+","+a1[3]+","+a1[4]+","+a1[5]+","+a1[6]
                    addLine(r2,dataLine)
                    weights = updateWeight(weights, 1)
                    done.append(2)
                else:
                    break

            elif chooseFun == 3:
                if (chooseFun not in done) :
                    currTime = currTime + int(a2[3]) 
                    a2[3] = str(currTime)
                    a2[5] = str(max(cpuVal))
                    dataLine = a2[0]+","+a2[1]+","+a2[2]+","+a2[3]+","+a2[4]+","+a2[5]+","+a2[6]
                    addLine(r3,dataLine)
                    weights = updateWeight(weights, 2)
                    done.append(3)
                else:
                    break
            
            elif chooseFun == 4:
                if (chooseFun not in done) :
                    currTime = currTime + int(a3[3]) 
                    a3[3] = str(currTime)
                    a3[5] = str(max(cpuVal))
                    dataLine = a3[0]+","+a3[1]+","+a3[2]+","+a3[3]+","+a3[4]+","+a3[5]+","+a3[6]
                    addLine(r4,dataLine)
                    weights = updateWeight(weights, 3)
                    done.append(4)
                else:
                    break
            
            elif chooseFun == 5:
                if (chooseFun not in done) :
                    currTime = currTime + int(a4[3]) 
                    a4[3] = str(currTime)
                    a4[5] = str(max(cpuVal))
                    dataLine = a4[0]+","+a4[1]+","+a4[2]+","+a4[3]+","+a4[4]+","+a4[5]+","+a4[6]
                    addLine(r5,dataLine)
                    weights = updateWeight(weights, 4)
                    done.append(5)
                else:
                    break
        index = index + 1

mix5W()
print('Done')
