from functions.csvEntry import createCSV
from dataExtract import dataExtract
from dataExtract import mnmExtract
from dataExtract import anonymizedDataExtract
file1 = '/Users/shifatsarwar/Downloads/Job/graphfunction/dataList/arrayFiles/array111'
file2 = '/Users/shifatsarwar/Downloads/Job/graphfunction/dataList/arrayFiles/array222'
file3 = '/Users/shifatsarwar/Downloads/Job/graphfunction/dataList/arrayFiles/array333'
file1E = '/Users/shifatsarwar/Downloads/Job/graphfunction/dataList/encryptedFiles/array111'
file2E = '/Users/shifatsarwar/Downloads/Job/graphfunction/dataList/encryptedFiles/array222'
file3E = '/Users/shifatsarwar/Downloads/Job/graphfunction/dataList/encryptedFiles/array333'


def createGraphs(gNum, path):
    index = 1
    while index < gNum:
        if (index < 10):
            createCSV(path+'graph0'+str(index)+'.csv')
        else:
            createCSV(path+'graph'+str(index)+'.csv')
        index = index + 1

def createAnonymizedGraphs(gNum, path, level):
    index = 1
    while index < gNum:
        if (index < 10):
            createCSV(path+str(level)+'/graph0'+str(index)+'.csv')
        else:
            createCSV(path+str(level)+'/graph'+str(index)+'.csv')
        index = index + 1

def runGraphInitial(runs):
    path = '/Users/shifatsarwar/Downloads/Job/graphfunction/dataList/tests/'
    createGraphs(11, path)
    index = 0
    while index < runs:
        fileEnd = str(index)+'.csv'
        # f1 = file1+fileEnd
        # f2 = file2+fileEnd
        # f3 = file3+fileEnd
        f1E = file1E+fileEnd
        f2E = file2E+fileEnd
        f3E = file3E+fileEnd
        dataExtract.runGraph01(f1E)
        dataExtract.runGraph02(f1E, f2E)
        dataExtract.runGraph03(f1E, f2E)
        dataExtract.runGraph04(f1E, f2E, f3E)
        dataExtract.runGraph05(f1E, f2E)
        dataExtract.runGraph06(f1E, f2E)
        dataExtract.runGraph07(f1E, f2E, f3E)
        dataExtract.runGraph08(f1E)
        dataExtract.runGraph09(f1E)
        dataExtract.runGraph10(f1E, f2E, f3E)
        index = index + 1


def runGraphMnMInitial(runs):
    path = '/Users/shifatsarwar/Downloads/Job/graphfunction/dataList/tests/'
    createGraphs(11, path)
    index = 0
    while index < runs:
        fileEnd = str(index)+'.csv'
        f1 = file1+fileEnd
        f2 = file2+fileEnd
        f3 = file3+fileEnd
        f1E = file1E+fileEnd
        f2E = file2E+fileEnd
        f3E = file3E+fileEnd
        # mnmExtract.runGraph189(f1)
        # mnmExtract.runGraph2356(f1, f2, f1E, f2E)
        mnmExtract.runGraph4710(f1, f2, f3, f1E, f2E, f3E)
        index = index + 1

def runGraphAnonymizedInitial(runs, lvl):
    path = '/Users/shifatsarwar/Downloads/Job/graphfunction/dataList/tests/L'
    createAnonymizedGraphs(11, path, lvl)
    index = 0
    while index < runs:
        fileEnd = str(index)+'.csv'
        # f1 = file1+fileEnd
        # f2 = file2+fileEnd
        # f3 = file3+fileEnd
        f1E = file1E+fileEnd
        f2E = file2E+fileEnd
        f3E = file3E+fileEnd
        anonymizedDataExtract.runGraph01(f1E, lvl)
        anonymizedDataExtract.runGraph02(f1E, f2E, lvl)
        anonymizedDataExtract.runGraph03(f1E, f2E, lvl)
        anonymizedDataExtract.runGraph04(f1E, f2E, f3E, lvl)
        anonymizedDataExtract.runGraph05(f1E, f2E, lvl)
        anonymizedDataExtract.runGraph06(f1E, f2E, lvl)
        anonymizedDataExtract.runGraph07(f1E, f2E, f3E, lvl)
        anonymizedDataExtract.runGraph08(f1E, lvl)
        anonymizedDataExtract.runGraph09(f1E, lvl)
        anonymizedDataExtract.runGraph10(f1E, f2E, f3E, lvl)
        index = index + 1        