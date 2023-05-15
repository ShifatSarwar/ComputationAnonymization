import csv
pathMain = '../dataList/arrayFiles/'
path = '../dataList/arrayFiles/'

# Creates 100s of random values array from three csv files with lots of random values.
def createFiles():
    arrayOfarray = []
    arrayOfarray2 = []
    arrayOfarray3 = []
    with open(pathMain+"array_file111.csv") as f:
        reader = csv.reader(f) 
        for row in reader: 
            arrayOfarray.append(row)
    
    with open(pathMain+"array_file222.csv") as f:
        reader = csv.reader(f) 
        for row in reader: 
            arrayOfarray2.append(row)

    with open(pathMain+"array_file333.csv") as f:
        reader = csv.reader(f) 
        for row in reader: 
            arrayOfarray3.append(row)

    index = 0
    while index < 100:
        line = arrayOfarray[index]
        line2 = arrayOfarray2[index]
        line3 = arrayOfarray3[index]
        array1 = []
        array2 = []
        array3 = []
        for l in line:
            array1.append(int(l))
        
        for l in line2:
            array2.append(int(l))

        for l in line3:
            array3.append(int(l))

        array1 = str(array1)
        array2 = str(array2)
        array3 = str(array3)
        array1Loc = path+'array111'+str(index)+'.csv'
        array2Loc = path+'array222'+str(index)+'.csv'
        array3Loc = path+'array333'+str(index)+'.csv'
        with open(array1Loc, 'w') as f:
            f.write(array1)
            f.write("\n")
        f.close()

        with open(array2Loc, 'w') as f:
            f.write(array2)
            f.write("\n")
        f.close()

        with open(array3Loc, 'w') as f:
            f.write(array3)
            f.write("\n")
        f.close()

        index = index + 1
    print('Done')

createFiles()