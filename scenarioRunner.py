from functions.csvEntry import createCSV
from dataExtract import dataExtract
from dataExtract import mnmExtract
from dataExtract import anonymizedDataExtract
file1 = 'dataList/arrayFiles/array111'
file2 = 'dataList/arrayFiles/array222'
file3 = 'dataList/arrayFiles/array333'
file1E = 'dataList/encryptedFiles/array111'
file2E = 'dataList/encryptedFiles/array222'
file3E = 'dataList/encryptedFiles/array333'


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

# Runs the experiment to fetch data of normal graphs
def runGraphInitial(runs):
    path = 'dataList/tests/'
    createGraphs(11, path)
    index = 0
    while index < runs:
        
        fileEnd = str(index)+'.csv'

        # The files with capital 'E' are encrypted files. If you want 
        # to run the graphs on encrypted files uncoment the later graph call
        # and comment the normal graph
        # You can also try a combination of encrypted and normal files if required.

        f1 = file1+fileEnd
        f2 = file2+fileEnd
        f3 = file3+fileEnd
        dataExtract.runGraph01(f1)
        dataExtract.runGraph02(f1, f2)
        dataExtract.runGraph03(f1, f2)
        dataExtract.runGraph04(f1, f2, f3)
        dataExtract.runGraph05(f1, f2)
        dataExtract.runGraph06(f1, f2)
        dataExtract.runGraph07(f1, f2, f3)
        dataExtract.runGraph08(f1)
        dataExtract.runGraph09(f1)
        dataExtract.runGraph10(f1, f2, f3)
        '''
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
        '''
        index = index + 1

# Runs the mixing and matching algorithm combining multiple graphs
def runGraphMnMInitial(runs):
    path = 'dataList/tests/'
    createGraphs(11, path)
    index = 0
    while index < runs:
        fileEnd = str(index)+'.csv'
        # Similar to above 'E' uses encrypted files as inputs
        f1 = file1+fileEnd
        f2 = file2+fileEnd
        f3 = file3+fileEnd
        f1E = file1E+fileEnd
        f2E = file2E+fileEnd
        f3E = file3E+fileEnd

        # The current selection of hard coded mixes. They can be made to mix 
        # automatically if required. 

        # mnmExtract.runGraph189(f1)
        # mnmExtract.runGraph2356(f1, f2, f1E, f2E)
        mnmExtract.runGraph4710(f1, f2, f3, f1E, f2E, f3E)
        index = index + 1

# Runs anonymization algorithm with levels of anonymization (1-5)
def runGraphAnonymizedInitial(runs, lvl):
    path = 'dataList/tests/L'
    createAnonymizedGraphs(11, path, lvl)
    index = 0
    while index < runs:
        # The files with capital 'E' are encrypted files. If you want 
        # to run the graphs on encrypted files uncoment the later graph call
        # and comment the normal graph
        # You can also try a combination of encrypted and normal files if required.

        fileEnd = str(index)+'.csv'
        f1 = file1+fileEnd
        f2 = file2+fileEnd
        f3 = file3+fileEnd
        anonymizedDataExtract.runGraph01(f1, lvl)
        anonymizedDataExtract.runGraph02(f1, f2, lvl)
        anonymizedDataExtract.runGraph03(f1, f2, lvl)
        anonymizedDataExtract.runGraph04(f1, f2, f3, lvl)
        anonymizedDataExtract.runGraph05(f1, f2, lvl)
        anonymizedDataExtract.runGraph06(f1, f2, lvl)
        anonymizedDataExtract.runGraph07(f1, f2, f3, lvl)
        anonymizedDataExtract.runGraph08(f1, lvl)
        anonymizedDataExtract.runGraph09(f1, lvl)
        anonymizedDataExtract.runGraph10(f1, f2, f3, lvl)
        '''
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
        '''
        index = index + 1        