import csv
import random
from csvEntry import addLine

array = []   
array2 = [] 
pathMain = '../dataList/tests/graph05.csv'
result = '../dataList/tests/results.csv'

with open(pathMain) as f:
    reader = csv.reader(f) 
    for row in reader: 
        array.append(row)

# with open(pathMain2) as f:
#     reader = csv.reader(f) 
#     for row in reader: 
#         array2.append(row)

index = 0
for x in array:
    if index > 0 :
        # y = array2[index]
        size = int(x[3])
        sizeO = size/100 * random.randint(10,70)
        sizeI = size/100 * random.randint(10,70)
        x[3] = str(int(int(x[3])+sizeI))
        # x[4] = str(int(int(x[4])+sizeO))
        # x[1] = str(random.randint(3,5))
        # x[5]=y[5]
        # x[0]=y[0]
    dataLine = x[0]+","+x[1]+","+x[2]+","+x[3]+","+x[4]+","+x[5]+","+x[6]
    addLine(result,dataLine)
    index = index + 1