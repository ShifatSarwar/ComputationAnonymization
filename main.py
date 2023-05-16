# .real indicates using the real world graphs, they are already...
# created, connected and compiled so only anonymize works on them.
from dataExtract.real import dataExtractSimple
from dataExtract.real import dataExtractFake
# Use this for just mixing two graphs
from dataExtract.real import dataExtractMix
# Use this for Hybrid Anonymization
from dataExtract.real import dataExtractHybrid

# .generated indicates using the generated graphs. 
from dataExtract.generated import dataExtractSimple
from dataExtract.generated import dataExtractFake
# Use this for just mixing two graphs
from dataExtract.generated import dataExtractMix
# Use this for Hybrid Anonymization
from dataExtract.generated import dataExtractHybrid
from dataExtract.generated.graphNodes import *
import random

# Choose number of loops to collect graph data
# For real world graph choose the name of graph 
# after the getData from the list below:
# 1) ImageEnhance    2) DeepLearning 3) ObjectDetection
# 4) MultilabelText  5) LanguageLSTM 6) SyntheticGAN
# 7) ImageCaptioning 8) ImageCaption 9) NeuralNetwork
# 10) SimpleCluster Example: getDataDeepLearning.
def anonymize_real_world(mode, level, runs):
    if mode == 0:
        dataExtractSimple.getDataDeepLearning(runs)
    elif mode == 1:
        dataExtractFake.getDataDeepLearning(runs, level)
    # For Hybrid and Mix choose numbers of graph in the manner below:
    # Like runGraph13810, runs a mixture of graph 1, 3, 8 and 10 from
    # above list. Check if combination is available in dataExtractMix
    # file as all combinations are not possible. For hybrid only 2 to 
    # 4 graphs can be combined for regular mixing 5 graph combination
    # option is available. Use lower runs here to collect results by 
    # changing epoch and other parameters from the 
    # dataExtract.real.functions folder.
    elif mode == 2:
        idx = 0
        while idx < runs:
            dataExtractMix.runGraph13810(idx)
            idx+=1
    else:
        idx = 0
        while idx < runs:
            dataExtractHybrid.runGraph13810(idx, level)
            idx+=1

# Allows the creation, addition and compilation of graphs
class Camouflage:

    def __init__(self):
        self.graph1 = []
        self.graph2 = []
        self.graph3 = []

    # Creates random graph instances
    def CreateGraph(self):
        self.graph1.append('basic_calculations')      
        self.graph1.append('sorting')
        self.graph1.append('encryption')
        self.graph1.append('decryption')
        self.graph1.append('compression')

    # Function name selects the return value of the generated graph
    # after it runs through all operations.
    # Current available functions are Sorting, Encryption, Addition,
    # Multuplication, 
    def ConnectNodes(self, functionName,level):
        if level == '0':
            level = random.randint(1,5) - 1
        else:
            level = level -1 
        graph2 = []
        while level > 0:
            g = [0,1,2,3,4]
            chooseFun = random.choices(g)
            graph2 = self.append(chooseFun)
            random_val -= 1
        graph2.append(functionName)
        self.graph1 = graph2
        

    def Compile(self):
        encrypt = False
        compress = False
        for x in self.graph:
            if compress:
                print('Nodes cannot be connected.')
                self.graph = []
                break
            if encrypt and x != 'decryption':
                print('Nodes cannot be connected.')
                self.graph = []
                break
            elif x == 'encryption':
                encrypt = True
            elif x == 'decryption':
                if not encrypt:
                    print('Nodes cannot be connected.')
                    self.graph = []
                    break
                encrypt = False
            elif x == 'compression':
                compress = True
 
    def Anonymize(self, mode, data, level):
        output = data
        if mode == 0:
            for x in self.graph:
                if x == 'basic_calculations':
                    output = calculateContentsSingle(output)
                elif x == 'sorting':
                    output = sortArray(output)
                elif x == 'encryption':
                    output = encryptAES(output)
                elif x =='decryption':
                    output = decryptAES(output)
                elif x =='compression':
                    output = compressGZip(output)

        elif mode == 1:
            for x in self.graph:
                level = checkAnonymity(level, False)
                if x == 'basic_calculations':
                    output = calculateContentsSingle(output)
                elif x == 'sorting':
                    output = sortArray(output)
                elif x == 'encryption':
                    output = encryptAES(output)
                elif x =='decryption':
                    output = decryptAES(output)
                elif x =='compression':
                    output = compressGZip(output)         
            level = checkAnonymity(level, True)
        
        elif mode == 2:
            pass
        return output
    
    


if __name__ == '__main__':
    # Choose mode 0 for None.
    # Choose mode 1 for Remodel.
    # Choose mode 2 for Mixing.
    # Choose mode 3 for Hybrid.
    anonymize_real_world(0, 3, 20)
    
        
        



