
import time
import os
import pickle
import random
import sys
# Simple Image Enhancement Graph - G1
from functions.imageEnhancement import *
# Machine Learning Graph - G2
from functions.deepLearning import *
# Uses Trained Model to Detect Object - G3
from functions.objectDetection import *
# Machine Learning Graph 2 - G4
from functions.multilabelText import *
# Machine Learning Graph 3 - G5
from functions.languageTranslationLSTM import *
# Machine Learning Graph 4 - G6
from functions.syntheticGAN import *
# Machine Learning Graph 5 - G7
from functions.imageCaptionTraining import *
from functions.featureExtract import *
# Uses Trained Model for Image Captioning - G8
from functions.imageCaption import *
# Machine Learning Graph 6 - G9
from functions.neuralNetwork import *
# Machine Learning Graph 7 - G10
from functions.simpleClustering import *
from functions.hybrid import *
from utility import *
# from tensorflow.keras.datasets import fashion_mnist

path = 'dataList/mix/' 
nextP = 'dataList/mix/two_mix/'
nextP2 = 'dataList/mix/three_mix/'
nextP3 = 'dataList/mix/four_mix/'
nextP4 = 'dataList/mix/five_mix/'

# Fix the inputs for the three graphs.
# Collect the Input and Output Sizes along with time.
# Looks similar to normal mixing but uses remodeling
# as another mixed graph.
# Runs and Collects Data from the mix of Graph 1,8,10
def runGraph1810(idx, level):
    path1 = 'extra/Flicker8k_Dataset/pic'+str(idx)+'.jpg'
    inputSize1 = os.path.getsize(path1)
    inputSize1 = getUpdatedSizeInput(inputSize1, 1)
    fileLoc10 = 'extra/samples/csvs/trainset'+str(idx)+'.csv'
    inputSize10 = os.path.getsize(fileLoc10)
    inputSize10 = getUpdatedSizeInput(inputSize10, 10)
    path08 = 'extra/Flicker8k_Dataset/pic'+str(idx)+'.jpg'
    inputSize08 = os.path.getsize(path08)
    inputSize08 = getUpdatedSizeInput(inputSize08, 8)
    iSize = [inputSize1, inputSize08, inputSize10]
    a1 = [path1, 0, 0, 0]
    a2 = [fileLoc10,0, 0, 0]
    a3 = [fileLoc10, 0, 0, 0]

    graphNum = [1,9,10]
    updateValues=[a1, a2, a3]
    output = process3W(updateValues, level)
    outputValues = output[0]
    timeValues = output[1]
    
    index=0

    for x in outputValues:
        if index != 2:
            name = 'graph0'+str(graphNum[index])
        else: 
            name = 'graph'+str(graphNum[index])

        if(type(x)==str):
            outputSize = os.path.getsize(x)
        
        # The dump and get outputSize for 9 and 10 
        elif(index == 2):
            filename = 'models/finalized_model2.sav'
            pickle.dump(x, open(filename, 'wb'))
            outputSize = os.path.getsize(filename)
        else:
            outputSize = sys.getsizeof(x)
    
        outputSize = getUpdatedSize(outputSize, graphNum[index])
        dataLine = name+','+str(iSize[index])+','+str(outputSize)+','+str(timeValues[index])+','+str(graphNum[index]-1)
        addLine(path+name+'.csv',dataLine)
        index=index+1

# Runs and Collects Data from the mix of Graph 3,9,10
def runGraph3910(idx, level):
    classPath = 'extra/'
    inputSize3 = os.path.getsize(classPath+'classes.txt')
    # inputSize3 = getUpdatedSizeInput(inputSize3, 3)
    fileLoc10 = 'extra/samples/csvs/trainset'+str(idx)+'.csv'
    inputSize10 = os.path.getsize(fileLoc10)
    # inputSize10 = getUpdatedSizeInput(inputSize10, 10)
    # inputSize9 = getUpdatedSizeInput(inputSize10, 9)
    iSize = [inputSize3, inputSize10, inputSize10]
    a1 = [classPath, 5, 0, 0]
    a2 = [fileLoc10,0, 0, 0]
    a3 = [fileLoc10, 0, 0, 0]

    graphNum = [3,9,10]
    updateValues=[a1, a2, a3]
    output = process3W(updateValues, level)
    outputValues = output[0]
    timeValues = output[1]
    
    index=0

    for x in outputValues:
        if index != 2:
            name = 'graph0'+str(graphNum[index])
        else: 
            name = 'graph'+str(graphNum[index])

        if(index==0):
            outputSize = sys.getsizeof(x)
        # The dump and get outputSize for 9 and 10 
        elif(index == 1):
            filename = 'models/finalized_model1.sav'
            pickle.dump(x, open(filename, 'wb'))
            outputSize = os.path.getsize(filename)
        elif(index == 2):
            filename = 'models/finalized_model2.sav'
            pickle.dump(x, open(filename, 'wb'))
            outputSize = os.path.getsize(filename)


        outputSize = getUpdatedSize(outputSize, graphNum[index])
        dataLine = name+','+str(iSize[index])+','+str(outputSize)+','+str(timeValues[index])+','+str(graphNum[index]-1)
        addLine(path+name+'.csv',dataLine)
        index=index+1

# Runs and Collects Data from the mix of Graph 1,3,8
def runGraph138(idx, level):
    path1 = 'extra/Flicker8k_Dataset/pic'+str(idx)+'.jpg'
    inputSize1 = os.path.getsize(path1)
    # inputSize1 = getUpdatedSizeInput(inputSize1, 1)
    classPath = 'extra/'
    inputSize3 = os.path.getsize(classPath+'classes.txt')
    # inputSize3 = getUpdatedSizeInput(inputSize3, 3)
    path08 = 'extra/Flicker8k_Dataset/pic'+str(idx)+'.jpg'
    inputSize08 = os.path.getsize(path08)
    # inputSize08 = getUpdatedSizeInput(inputSize08, 8)
    iSize = [inputSize1, inputSize3, inputSize08]
    a1 = [path1, 0, 0, 0]
    a2 = [classPath,5, 0, 0]
    a3 = [path08, 0, 0, 0]

    graphNum = [1,3,8]
    updateValues=[a1, a2, a3]
    output = process3W(updateValues, level)
    outputValues = output[0]
    timeValues = output[1]
    
    index=0

    for x in outputValues:
        name = 'graph0'+str(graphNum[index])
        
        if(type(x)==str):
            outputSize = os.path.getsize(x)
        else:
            outputSize = sys.getsizeof(x)
        
        outputSize = getUpdatedSize(outputSize, graphNum[index])
        dataLine = name+','+str(iSize[index])+','+str(outputSize)+','+str(timeValues[index])+','+str(graphNum[index]-1)
        addLine(path+name+'.csv',dataLine)
        index=index+1

# Runs and Collects Data from the mix of Graph 1,9,10
def runGraph1910(idx, level):
    path1 = 'extra/Flicker8k_Dataset/pic'+str(idx)+'.jpg'
    inputSize1 = os.path.getsize(path1)
    # inputSize1 = getUpdatedSizeInput(inputSize1, 1)
    fileLoc10 = 'extra/samples/csvs/trainset'+str(idx)+'.csv'
    inputSize10 = os.path.getsize(fileLoc10)
    # inputSize10 = getUpdatedSizeInput(inputSize10, 10)
    # inputSize9 = getUpdatedSizeInput(inputSize10, 9)
    iSize = [inputSize1, inputSize10, inputSize10]
    a1 = [path1, 0, 0, 0]
    a2 = [fileLoc10,0, 0, 0]
    a3 = [fileLoc10, 0, 0, 0]

    graphNum = [1,9,10]
    updateValues=[a1, a2, a3]
    output = process3W(updateValues, level)
    outputValues = output[0]
    timeValues = output[1]
    
    index=0

    for x in outputValues:
        if index != 2:
            name = 'graph0'+str(graphNum[index])
        else: 
            name = 'graph'+str(graphNum[index])

        if(index==0):
            outputSize = sys.getsizeof(x)
                # The dump and get outputSize for 9 and 10 
        elif(index == 1):
            filename = 'models/finalized_model1.sav'
            pickle.dump(x, open(filename, 'wb'))
            outputSize = os.path.getsize(filename)
        elif(index == 2):
            filename = 'models/finalized_model2.sav'
            pickle.dump(x, open(filename, 'wb'))
            outputSize = os.path.getsize(filename)

        outputSize = getUpdatedSize(outputSize, graphNum[index])
        dataLine = name+','+str(iSize[index])+','+str(outputSize)+','+str(timeValues[index])+','+str(graphNum[index]-1)
        addLine(path+name+'.csv',dataLine)
        index=index+1


# Runs and Collects Data from the mix of Graph 1,8, 9, 10
def runGraph1839(idx, level):
    path1 = 'extra/Flicker8k_Dataset/pic'+str(idx)+'.jpg'
    inputSize1 = os.path.getsize(path1)
    # inputSize1 = getUpdatedSizeInput(inputSize1, 1)
    classPath = 'extra/'
    inputSize3 = os.path.getsize(classPath+'classes.txt')
    # inputSize3 = getUpdatedSizeInput(inputSize3, 3)
    fileLoc10 = 'extra/samples/csvs/trainset'+str(idx)+'.csv'
    inputSize10 = os.path.getsize(fileLoc10)
    # inputSize9 = getUpdatedSizeInput(inputSize10, 9)
    path08 = 'extra/Flicker8k_Dataset/pic'+str(idx)+'.jpg'
    inputSize08 = os.path.getsize(path08)
    # inputSize08 = getUpdatedSizeInput(inputSize08, 8)
    iSize = [inputSize1, inputSize3, inputSize08, inputSize10]
    a1 = [path1, 0, 0, 0]
    a2 = [classPath,5, 0, 0]
    a3 = [path08, 0, 0, 0]
    a4 = [fileLoc10, 0, 0, 0]

    graphNum = [1,3,8,9]
    updateValues=[a1, a2, a3, a4]
    output = process4W(updateValues, level)
    outputValues = output[0]
    timeValues = output[1]
    
    index=0

    for x in outputValues:
        name = 'graph0'+str(graphNum[index])

        if(type(x)==str):
            outputSize = os.path.getsize(x)
        
        # The dump and get outputSize for 9 and 10 
        elif(index == 3):
            filename = 'models/finalized_model1.sav'
            pickle.dump(x, open(filename, 'wb'))
            outputSize = os.path.getsize(filename)
        else:
            outputSize = sys.getsizeof(x)
    
        outputSize = getUpdatedSize(outputSize, graphNum[index])
        dataLine = name+','+str(iSize[index])+','+str(outputSize)+','+str(timeValues[index])+','+str(graphNum[index]-1)
        addLine(nextP2+name+'.csv',dataLine)
        index=index+1

# Runs and Collects Data from the mix of Graph 1,10,3 and 9
def runGraph13910(idx, level):
    path1 = 'extra/Flicker8k_Dataset/pic'+str(idx)+'.jpg'
    inputSize1 = os.path.getsize(path1)
    inputSize1 = getUpdatedSizeInput(inputSize1, 1)
    classPath = 'extra/'
    inputSize3 = os.path.getsize(classPath+'classes.txt')
    inputSize3 = getUpdatedSizeInput(inputSize3, 3)
    fileLoc10 = 'extra/samples/csvs/trainset'+str(idx)+'.csv'
    inputSize10 = os.path.getsize(fileLoc10)
    inputSize10 = getUpdatedSizeInput(inputSize10, 10)
    inputSize9 = getUpdatedSizeInput(inputSize10, 9)
    iSize = [inputSize1, inputSize3, inputSize9, inputSize10]
    a1 = [path1, 0, 0, 0]
    a2 = [classPath,idx, 0, 0]
    a3 = [fileLoc10, 0, 0, 0]
    a4 = [fileLoc10, 0, 0, 0]

    graphNum = [1,3,9,10]
    updateValues=[a1, a2, a3, a4]
    output = process4W(updateValues, level)
    outputValues = output[0]
    timeValues = output[1]
    
    index=0

    for x in outputValues:
        if index != 3:
            name = 'graph0'+str(graphNum[index])
        else: 
            name = 'graph'+str(graphNum[index])

        if(type(x)==str):
            outputSize = os.path.getsize(x)
        
        # The dump and get outputSize for 9 and 10 
        elif(index == 2):
            filename = 'fmodels/inalized_model1.sav'
            pickle.dump(x, open(filename, 'wb'))
            outputSize = os.path.getsize(filename)
        elif(index == 3):
            filename = 'models/finalized_model2.sav'
            pickle.dump(x, open(filename, 'wb'))
            outputSize = os.path.getsize(filename)
        else:
            outputSize = sys.getsizeof(x)
    
        outputSize = getUpdatedSize(outputSize, graphNum[index])
        dataLine = name+','+str(iSize[index])+','+str(outputSize)+','+str(timeValues[index])+','+str(graphNum[index]-1)
        addLine(nextP2+name+'.csv',dataLine)
        index=index+1

# Runs and Collects Data from the mix of Graph 1,3,8 and 10
def runGraph13810(idx, level):
    path1 = 'extra/Flicker8k_Dataset/pic'+str(idx)+'.jpg'
    inputSize1 = os.path.getsize(path1)
    # inputSize1 = getUpdatedSizeInput(inputSize1, 1)
    classPath = 'extra/'
    inputSize3 = os.path.getsize(classPath+'classes.txt')
    # inputSize3 = getUpdatedSizeInput(inputSize3, 3)
    fileLoc10 = 'extra/samples/csvs/trainset'+str(idx)+'.csv'
    inputSize10 = os.path.getsize(fileLoc10)
    # inputSize10 = getUpdatedSizeInput(inputSize10, 10)
    path08 = 'extra/Flicker8k_Dataset/pic'+str(idx)+'.jpg'
    inputSize08 = os.path.getsize(path08)
    # inputSize08 = getUpdatedSizeInput(inputSize08, 8)
    iSize = [inputSize1, inputSize3, inputSize08, inputSize10]
    a1 = [path1, 0, 0, 0]
    a2 = [classPath,5, 0, 0]
    a3 = [path08, 0, 0, 0]
    a4 = [fileLoc10, 0, 0, 0]

    graphNum = [1,3,8,10]
    updateValues=[a1, a2, a3, a4]
    output = process4W(updateValues, level)
    outputValues = output[0]
    timeValues = output[1]
    
    index=0

    for x in outputValues:
        if index != 3:
            name = 'graph0'+str(graphNum[index])
        else: 
            name = 'graph'+str(graphNum[index])


        if(type(x)==str):
            outputSize = os.path.getsize(x)
        
        # The dump and get outputSize for 9 and 10 
        elif(index == 3):
            filename = 'models/finalized_model2.sav'
            pickle.dump(x, open(filename, 'wb'))
            outputSize = os.path.getsize(filename)
        else:
            outputSize = sys.getsizeof(x)
    
        outputSize = getUpdatedSize(outputSize, graphNum[index])
        dataLine = name+','+str(iSize[index])+','+str(outputSize)+','+str(timeValues[index])+','+str(graphNum[index]-1)
        addLine(nextP2+name+'.csv',dataLine)
        index=index+1


# Runs and Collects Data from the mix of Graph 1,8,9 and 10
def runGraph18910(idx, level):
    path1 = 'extra/Flicker8k_Dataset/pic'+str(idx)+'.jpg'
    inputSize1 = os.path.getsize(path1)
    inputSize1 = getUpdatedSizeInput(inputSize1, 1)
    fileLoc10 = 'extra/samples/csvs/trainset'+str(idx)+'.csv'
    inputSize10 = os.path.getsize(fileLoc10)
    inputSize10 = getUpdatedSizeInput(inputSize10, 10)
    inputSize9 = getUpdatedSizeInput(inputSize10, 9)
    path08 = 'extra/Flicker8k_Dataset/pic'+str(idx)+'.jpg'
    inputSize08 = os.path.getsize(path08)
    inputSize08 = getUpdatedSizeInput(inputSize08, 8)
    iSize = [inputSize1, inputSize08, inputSize9, inputSize10]
    a1 = [path1, 0, 0, 0]
    a2 = [path08,0, 0, 0]
    a3 = [fileLoc10, 0, 0, 0]
    a4 = [fileLoc10, 0, 0, 0]

    graphNum = [1,8,9,10]
    updateValues=[a1, a2, a3, a4]
    output = process4W(updateValues, level)
    outputValues = output[0]
    timeValues = output[1]
    
    index=0

    for x in outputValues:
        if index != 3:
            name = 'graph0'+str(graphNum[index])
        else: 
            name = 'graph'+str(graphNum[index])

        if(type(x)==str):
            outputSize = os.path.getsize(x)
        
        # The dump and get outputSize for 9 and 10 
        elif(index == 2):
            filename = 'models/finalized_model1.sav'
            pickle.dump(x, open(filename, 'wb'))
            outputSize = os.path.getsize(filename)
        elif(index == 3):
            filename = 'models/finalized_model2.sav'
            pickle.dump(x, open(filename, 'wb'))
            outputSize = os.path.getsize(filename)
        else:
            outputSize = sys.getsizeof(x)
    
        outputSize = getUpdatedSize(outputSize, graphNum[index])
        dataLine = name+','+str(iSize[index])+','+str(outputSize)+','+str(timeValues[index])+','+str(graphNum[index]-1)
        addLine(nextP2+name+'.csv',dataLine)
        index=index+1

# Runs and Collects Data from the mix of Graph 1 and 10
# All Input Size Results are wrong.
def runGraph110(idx, level):
    path1 = 'extra/Flicker8k_Dataset/pic'+str(idx)+'.jpg'
    inputSize1 = os.path.getsize(path1)
    inputSize1 = getUpdatedSizeInput(inputSize1, 1)
    fileLoc10 = 'extra/samples/csvs/trainset'+str(idx)+'.csv'
    inputSize10 = os.path.getsize(fileLoc10)
    inputSize10 = getUpdatedSizeInput(inputSize10, 10)
    iSize = [inputSize1, inputSize10]
    a1 = [path1, 0, 0, 0]
    a2 = [fileLoc10, 0, 0, 0]
    graphNum = [1,10]
    updateValues=[a1, a2]
    output = process2W(updateValues, level)
    outputValues = output[0]
    timeValues = output[1]
    
    index=0

    for x in outputValues:
        if index != 1:
            name = 'graph0'+str(graphNum[index])
        else: 
            name = 'graph'+str(graphNum[index])

        if(index == 0):
            outputSize = sys.getsizeof(x)
        # The dump and get outputSize for 9 and 10 
        elif(index == 1):
            filename = 'models/finalized_model4.sav'
            pickle.dump(x, open(filename, 'wb'))
            outputSize = os.path.getsize(filename)
        
        outputSize = getUpdatedSize(outputSize, graphNum[index])
        dataLine = name+','+str(iSize[index])+','+str(outputSize)+','+str(timeValues[index])+','+str(graphNum[index]-1)
        addLine(nextP+name+'.csv',dataLine)
        index=index+1

# Runs and Collects Data from the mix of Graph 3 and 9
def runGraph39(idx, level):
    classPath = 'extra/'
    inputSize3 = os.path.getsize(classPath+'classes.txt')
    # inputSize3 = getUpdatedSizeInput(inputSize3, 3)
    fileLoc10 = 'extra/samples/csvs/trainset'+str(idx)+'.csv'
    inputSize10 = os.path.getsize(fileLoc10)
    # inputSize9 = getUpdatedSizeInput(inputSize10, 9)
    iSize = [inputSize3, inputSize10]
    a1 = [classPath, 5, 0, 0]
    a2 = [fileLoc10, 0, 0, 0]
    graphNum = [3,9]
    updateValues=[a1, a2]
    output = process2W(updateValues, level)
    outputValues = output[0]
    timeValues = output[1]
    
    index=0

    for x in outputValues:
        name = 'graph0'+str(graphNum[index])
        
        if(index==0):
            outputSize = sys.getsizeof(x)
        # The dump and get outputSize for 9 and 10 
        elif(index == 1):
            filename = 'models/finalized_model3.sav'
            pickle.dump(x, open(filename, 'wb'))
            outputSize = os.path.getsize(filename)
        
        outputSize = getUpdatedSize(outputSize, graphNum[index])
        dataLine = name+','+str(iSize[index])+','+str(outputSize)+','+str(timeValues[index])+','+str(graphNum[index]-1)
        addLine(nextP+name+'.csv',dataLine)
        index=index+1

# Runs and Collects Data from the mix of Graph 8 and 9
def runGraph89(idx, level):
    path08 = 'extra/Flicker8k_Dataset/pic'+str(idx)+'.jpg'
    inputSize08 = os.path.getsize(path08)
    # inputSize3 = getUpdatedSizeInput(inputSize3, 3)
    fileLoc10 = 'extra/samples/csvs/trainset'+str(idx)+'.csv'
    inputSize10 = os.path.getsize(fileLoc10)
    # inputSize9 = getUpdatedSizeInput(inputSize10, 9)
    iSize = [inputSize08, inputSize10]
    a1 = [path08, 0, 0, 0]
    a2 = [fileLoc10, 0, 0, 0]
    graphNum = [8,9]
    updateValues=[a1, a2]
    output = process2W(updateValues, level)
    outputValues = output[0]
    timeValues = output[1]
    
    index=0

    for x in outputValues:
        name = 'graph0'+str(graphNum[index])
        
        if(index==0):
            outputSize = sys.getsizeof(x)
        # The dump and get outputSize for 9 and 10 
        elif(index == 1):
            filename = 'models/finalized_model3.sav'
            pickle.dump(x, open(filename, 'wb'))
            outputSize = os.path.getsize(filename)
        
        outputSize = getUpdatedSize(outputSize, graphNum[index])
        dataLine = name+','+str(iSize[index])+','+str(outputSize)+','+str(timeValues[index])+','+str(graphNum[index]-1)
        addLine(nextP+name+'.csv',dataLine)
        index=index+1

# Runs and Collects Data from the mix of Graph 1 and 8
def runGraph18(idx, level):
    path1 = 'extra/Flicker8k_Dataset/pic'+str(idx)+'.jpg'
    inputSize1 = os.path.getsize(path1)
    # inputSize1 = getUpdatedSizeInput(inputSize1, 1)
    path08 = 'extra/Flicker8k_Dataset/pic'+str(idx)+'.jpg'
    inputSize08 = os.path.getsize(path08)
    # inputSize08 = getUpdatedSizeInput(inputSize08, 8)
    iSize = [inputSize1, inputSize08]
    a1 = [path1, 0, 0, 0]
    a2 = [path08, 0, 0, 0]
    graphNum = [1,8]
    updateValues=[a1, a2]
    output = process2W(updateValues, level)
    outputValues = output[0]
    timeValues = output[1]
    
    index=0

    for x in outputValues:
        name = 'graph0'+str(graphNum[index])
        
        if(type(x)==str):
            outputSize = os.path.getsize(x)
        else:
            outputSize = sys.getsizeof(x)
        
        outputSize = getUpdatedSize(outputSize, graphNum[index])
        dataLine = name+','+str(iSize[index])+','+str(outputSize)+','+str(timeValues[index])+','+str(graphNum[index]-1)
        addLine(nextP+name+'.csv',dataLine)
        index=index+1

# Runs and Collects Data from the mix of Graph 8 and 10
def runGraph810(idx, level):
    fileLoc10 = 'extra/samples/csvs/trainset'+str(idx)+'.csv'
    inputSize10 = os.path.getsize(fileLoc10)
    # inputSize10 = getUpdatedSizeInput(inputSize10, 10)
    path08 = 'extra/Flicker8k_Dataset/pic'+str(idx)+'.jpg'
    inputSize08 = os.path.getsize(path08)
    # inputSize08 = getUpdatedSizeInput(inputSize08, 8)
    iSize = [inputSize08, inputSize10]
    a1 = [path08, 0, 0, 0]
    a2 = [fileLoc10, 0, 0, 0]
    graphNum = [8,10]
    updateValues=[a1, a2]
    output = process2W(updateValues, level)
    outputValues = output[0]
    timeValues = output[1]
    
    index=0

    for x in outputValues:
        if index != 1:
            name = 'graph0'+str(graphNum[index])
        else: 
            name = 'graph'+str(graphNum[index])

        if(type(x)==str):
            outputSize = os.path.getsize(x)
        # The dump and get outputSize for 9 and 10 
        elif(index == 1):
            filename = 'models/finalized_model4.sav'
            pickle.dump(x, open(filename, 'wb'))
            outputSize = os.path.getsize(filename)

        outputSize = getUpdatedSize(outputSize, graphNum[index])
        dataLine = name+','+str(iSize[index])+','+str(outputSize)+','+str(timeValues[index])+','+str(graphNum[index]-1)
        addLine(nextP+name+'.csv',dataLine)
        index=index+1


