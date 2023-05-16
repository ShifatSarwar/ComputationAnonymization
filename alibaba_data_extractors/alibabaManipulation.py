import csv
import random
from random import choice
import pandas as pd
from utility import addLine
pathMain = 'dataList/graph10.csv'

result = 'dataList/trainbaba.csv'

# Get the data
def extractInfo():
    array = []
    with open(pathMain) as f:
        reader = csv.reader(f) 
        for row in reader: 
            array.append(row)

    for x in array:
        if x[3] != "timeTaken":
            
            x[3] = str(int(x[4])-int(x[3]))
            # Task 1 is 0
            # Task 3 is 1
            # Task 4 is 2
            # Task 5 is 3
            # Task 6 is 4
            # Task 8 is 5
            # Task 9 is 6
            # Task 10 is 7
            # Task 11 is 8
            # Task 12 is 9

            if(x[2] == '1'):
                x[2] = '0'
            elif(x[2] == '3'):
                x[2] = '1'
            elif(x[2] == '4'):
                x[2] = '2'
            elif(x[2] == '5'):
                x[2] = '3'
            elif(x[2] == '6'):
                x[2] = '4'
            elif(x[2] == '8'):
                x[2] = '5'
            elif(x[2] == '9'):
                x[2] = '6'
            elif(x[2] == '10'):
                x[2] = '7'
            elif(x[2] == '11'):
                x[2] = '8'
            elif(x[2] == '12'):
                x[2] = '9'
        
        dataLine = x[0]+","+x[1]+","+x[2]+","+x[3]+","+x[4]+","+x[5]+","+x[6]
        addLine(result,dataLine)

# Prepare them for training
def trainBABA():
    index = 1
    while index < 11:
        g = 'dataList/'
        if index < 10:
            g = g+'graph0'+str(index)+'.csv'
        else:
            g = g+'graph10.csv'
        array = []
        with open(g) as f:
            reader = csv.reader(f) 
            for row in reader: 
                array.append(row)
        
        i2 = 1500
        for x in array:
            if(i2 <= 0):
                break
            if x[3] != "timeTaken":
                dataLine = x[0]+","+x[1]+","+x[2]+","+x[3]+","+x[4]+","+x[5]+","+x[6]
                addLine(result,dataLine)
                i2 = i2 - 1

        index = index + 1

   

            

    