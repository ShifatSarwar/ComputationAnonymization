import csv
import random
from random import choice
from utility import addLine
from numpy import timedelta64 

array = []   
array2 = [] 
g1 = 'dataList/mixing/g1.csv'
g2 = 'dataList/mixing/g2.csv'
g3 = 'dataList/mixing/g3.csv'
g4 = 'dataList/mixing/g4.csv'
g5 = 'dataList/mixing/g5.csv'
g6 = 'dataList/mixing/g6.csv'
g7 = 'dataList/mixing/g7.csv'
g8 = 'dataList/mixing/g8.csv'
g9 = 'dataList/mixing/g9.csv'
g10 = 'dataList/mixing/g10.csv'
 
r1 = 'dataList/mixing/unweighted/mix3/g1.csv'
r2 = 'dataList/mixing/unweighted/mix3/g2.csv'
r3 = 'dataList/mixing/unweighted/mix3/g3.csv'
r4 = 'dataList/mixing/unweighted/mix4/g4.csv'
r5 = 'dataList/mixing/unweighted/mix5/g5.csv'

# Adds time and resources based on the effect of mixing
def mixAndMatchBox():
    array1 = []
    with open(g1) as f:
        reader = csv.reader(f) 
        for row in reader: 
            array1.append(row)
    array4 = []
    with open(g4) as f:
        reader = csv.reader(f) 
        for row in reader: 
            array4.append(row)
    array5 = []
    with open(g6) as f:
        reader = csv.reader(f) 
        for row in reader: 
            array5.append(row)
    array6 = []
    with open(g9) as f:
        reader = csv.reader(f) 
        for row in reader: 
            array6.append(row)
    array12 = []
    with open(g10) as f:
        reader = csv.reader(f) 
        for row in reader: 
            array12.append(row)
    time1 = array1[1][4]
    time4 = array4[1][4]
    time5 = array5[1][4]
    time6 = array6[1][4]
    time12 = array12[1][4]
    a1 = array1[1]
    a4 = array4[1]
    a5 = array5[1]
    a6 = array6[1]
    a12 = array12[1]
    index = 0
    while index < 35:
        a1[4] = time1
        a4[4] = time4
        a5[4] = time5
        a6[4] = time6
        a12[4] = time12
        done = []
        currTime = 0
        check = [1,2,3,4,5]
        while True:
            if len(done) == 5:
                break
            cpuVal = [int(float(a1[5])), int(float(a4[5])), int(float(a5[5])), int(float(a6[5])), int(float(a12[5]))]
            if len(done) == 4:
                for x in check:
                    if x not in done:
                        chooseFun = x
            else:
                chooseFun = choice([i for i in range(1,6) if i not in done])
        
            if chooseFun == 1:
                currTime = currTime + int(a1[4])
                a1[4] = str(currTime)
                a1[5] = str(max(cpuVal))
                dataLine = a1[0]+","+a1[1]+","+a1[2]+","+a1[3]+","+a1[4]+","+a1[5]+","+a1[6]
                addLine(r1,dataLine)
                done.append(1)
        
            elif chooseFun == 2:
                currTime = currTime + int(a4[4])
                a4[4] = str(currTime)
                a4[5] = str(max(cpuVal))
                dataLine = a4[0]+","+a4[1]+","+a4[2]+","+a4[3]+","+a4[4]+","+a4[5]+","+a4[6]
                addLine(r4,dataLine)
                done.append(2)
        
            elif chooseFun == 3:
                currTime = currTime + int(a5[4])
                a5[4] = str(currTime)
                a5[5] = str(max(cpuVal))
                dataLine = a5[0]+","+a5[1]+","+a5[2]+","+a5[3]+","+a5[4]+","+a5[5]+","+a5[6]
                addLine(r2,dataLine)
                done.append(3)
        
            elif chooseFun == 4:
                currTime = currTime + int(a6[4])
                a6[4] = str(currTime)
                a6[5] = str(max(cpuVal))
                dataLine = a6[0]+","+a6[1]+","+a6[2]+","+a6[3]+","+a6[4]+","+a6[5]+","+a6[6]
                addLine(r3,dataLine)
                done.append(4)

            elif chooseFun == 5:
                currTime = currTime + int(a12[4])
                a12[4] = str(currTime)
                a12[5] = str(max(cpuVal))
                dataLine = a12[0]+","+a12[1]+","+a12[2]+","+a12[3]+","+a12[4]+","+a12[5]+","+a12[6]
                addLine(r1,dataLine)
                done.append(5)

        index = index + 1

def mix2U():
    array1 = []
    with open(g2) as f:
        reader = csv.reader(f) 
        for row in reader: 
            array1.append(row)
    array2 = []
    with open(g9) as f:
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
        check = [1,2]
        a1 = array1[index]
        a2 = array2[index]
        while True:
            if len(done) == 2:
                break
            cpuVal = [int(float(a1[5])), int(float(a2[5]))]
            if len(done) == 1:
                for x in check:
                    if x not in done:
                        chooseFun = x
            else:
                chooseFun = choice([i for i in range(1,3) if i not in done])
        
            if chooseFun == 1:
                currTime = currTime + int(a1[3])
                a1[3] = str(currTime)
                a1[5] = str(max(cpuVal))
                dataLine = a1[0]+","+a1[1]+","+a1[2]+","+a1[3]+","+a1[4]+","+a1[5]+","+a1[6]
                addLine(r1,dataLine)
                done.append(1)
        
            elif chooseFun == 2:
                currTime = currTime + int(a2[3])
                a2[3] = str(currTime)
                a2[5] = str(max(cpuVal))
                dataLine = a2[0]+","+a2[1]+","+a2[2]+","+a2[3]+","+a2[4]+","+a2[5]+","+a2[6]
                addLine(r2,dataLine)
                done.append(2)
        
        index = index + 1


def mix3U():
    array1 = []
    with open(g5) as f:
        reader = csv.reader(f) 
        for row in reader: 
            array1.append(row)
    array2 = []
    with open(g6) as f:
        reader = csv.reader(f) 
        for row in reader: 
            array2.append(row)
    
    array3 = []
    with open(g7) as f:
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
        check = [1,2,3]
        a1 = array1[index]
        a2 = array2[index]
        a3 = array3[index]
        while True:
            if len(done) == 3:
                break
            cpuVal = [int(float(a1[5])), int(float(a2[5])), int(float(a3[5]))]
            if len(done) == 2:
                for x in check:
                    if x not in done:
                        chooseFun = x
            else:
                chooseFun = choice([i for i in range(1,4) if i not in done])
        
            if chooseFun == 1:
                currTime = currTime + int(a1[3])
                a1[3] = str(currTime)
                a1[5] = str(max(cpuVal))
                dataLine = a1[0]+","+a1[1]+","+a1[2]+","+a1[3]+","+a1[4]+","+a1[5]+","+a1[6]
                addLine(r1,dataLine)
                done.append(1)
        
            elif chooseFun == 2:
                currTime = currTime + int(a2[3])
                a2[3] = str(currTime)
                a2[5] = str(max(cpuVal))
                dataLine = a2[0]+","+a2[1]+","+a2[2]+","+a2[3]+","+a2[4]+","+a2[5]+","+a2[6]
                addLine(r2,dataLine)
                done.append(2)
            
            elif chooseFun == 3:
                currTime = currTime + int(a3[3])
                a3[3] = str(currTime)
                a3[5] = str(max(cpuVal))
                dataLine = a3[0]+","+a3[1]+","+a3[2]+","+a3[3]+","+a3[4]+","+a3[5]+","+a3[6]
                addLine(r3,dataLine)
                done.append(3)
        
        index = index + 1

def mix4U():
    array1 = []
    with open(g5) as f:
        reader = csv.reader(f) 
        for row in reader: 
            array1.append(row)
    array2 = []
    with open(g6) as f:
        reader = csv.reader(f) 
        for row in reader: 
            array2.append(row)
    
    array3 = []
    with open(g7) as f:
        reader = csv.reader(f) 
        for row in reader: 
            array3.append(row)

    array4 = []
    with open(g8) as f:
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
        check = [1,2,3,4]
        a1 = array1[index]
        a2 = array2[index]
        a3 = array3[index]
        a4 = array4[index]
        while True:
            if len(done) == 4:
                break
            cpuVal = [int(float(a1[5])), int(float(a2[5])), int(float(a3[5])), int(float(a4[5]))]
            if len(done) == 3:
                for x in check:
                    if x not in done:
                        chooseFun = x
            else:
                chooseFun = choice([i for i in range(1,5) if i not in done])
        
            if chooseFun == 1:
                currTime = currTime + int(a1[3])
                a1[3] = str(currTime)
                a1[5] = str(max(cpuVal))
                dataLine = a1[0]+","+a1[1]+","+a1[2]+","+a1[3]+","+a1[4]+","+a1[5]+","+a1[6]
                addLine(r1,dataLine)
                done.append(1)
        
            elif chooseFun == 2:
                currTime = currTime + int(a2[3])
                a2[3] = str(currTime)
                a2[5] = str(max(cpuVal))
                dataLine = a2[0]+","+a2[1]+","+a2[2]+","+a2[3]+","+a2[4]+","+a2[5]+","+a2[6]
                addLine(r2,dataLine)
                done.append(2)
            
            elif chooseFun == 3:
                currTime = currTime + int(a3[3])
                a3[3] = str(currTime)
                a3[5] = str(max(cpuVal))
                dataLine = a3[0]+","+a3[1]+","+a3[2]+","+a3[3]+","+a3[4]+","+a3[5]+","+a3[6]
                addLine(r3,dataLine)
                done.append(3)
            
            elif chooseFun == 4:
                currTime = currTime + int(a4[3])
                a4[3] = str(currTime)
                a4[5] = str(max(cpuVal))
                dataLine = a4[0]+","+a4[1]+","+a4[2]+","+a4[3]+","+a4[4]+","+a4[5]+","+a4[6]
                addLine(r4,dataLine)
                done.append(4)
        
        index = index + 1


def mix5U():
    array1 = []
    with open(g5) as f:
        reader = csv.reader(f) 
        for row in reader: 
            array1.append(row)
    array2 = []
    with open(g6) as f:
        reader = csv.reader(f) 
        for row in reader: 
            array2.append(row)
    
    array3 = []
    with open(g7) as f:
        reader = csv.reader(f) 
        for row in reader: 
            array3.append(row)

    array4 = []
    with open(g8) as f:
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
        check = [1,2,3,4,5]
        a1 = array1[index]
        a2 = array2[index]
        a3 = array3[index]
        a4 = array4[index]
        a5 = array5[index]
        while True:
            if len(done) == 5:
                break
            cpuVal = [int(float(a1[5])), int(float(a2[5])), int(float(a3[5])), int(float(a4[5])), int(float(a5[5]))]
            if len(done) == 4:
                for x in check:
                    if x not in done:
                        chooseFun = x
            else:
                chooseFun = choice([i for i in range(1,6) if i not in done])
        
            if chooseFun == 1:
                currTime = currTime + int(a1[3])
                a1[3] = str(currTime)
                a1[5] = str(max(cpuVal))
                dataLine = a1[0]+","+a1[1]+","+a1[2]+","+a1[3]+","+a1[4]+","+a1[5]+","+a1[6]
                addLine(r1,dataLine)
                done.append(1)
        
            elif chooseFun == 2:
                currTime = currTime + int(a2[3])
                a2[3] = str(currTime)
                a2[5] = str(max(cpuVal))
                dataLine = a2[0]+","+a2[1]+","+a2[2]+","+a2[3]+","+a2[4]+","+a2[5]+","+a2[6]
                addLine(r2,dataLine)
                done.append(2)
            
            elif chooseFun == 3:
                currTime = currTime + int(a3[3])
                a3[3] = str(currTime)
                a3[5] = str(max(cpuVal))
                dataLine = a3[0]+","+a3[1]+","+a3[2]+","+a3[3]+","+a3[4]+","+a3[5]+","+a3[6]
                addLine(r3,dataLine)
                done.append(3)
            
            elif chooseFun == 4:
                currTime = currTime + int(a4[3])
                a4[3] = str(currTime)
                a4[5] = str(max(cpuVal))
                dataLine = a4[0]+","+a4[1]+","+a4[2]+","+a4[3]+","+a4[4]+","+a4[5]+","+a4[6]
                addLine(r4,dataLine)
                done.append(4)
            
            elif chooseFun == 5:
                currTime = currTime + int(a5[3])
                a5[3] = str(currTime)
                a5[5] = str(max(cpuVal))
                dataLine = a5[0]+","+a5[1]+","+a5[2]+","+a5[3]+","+a5[4]+","+a5[5]+","+a5[6]
                addLine(r5,dataLine)
                done.append(5)
        
        index = index + 1

mix3U()
print("Done")
