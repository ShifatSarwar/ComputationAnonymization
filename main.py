# .real indicates using the real world graphs, they are already...
# created, connected and compiled so only anonymize works on them.
from dataExtract.real import dataExtractSimple
from dataExtract.real import dataExtractFake
# Use this for just mixing two graphs
from dataExtract.real import dataExtractMix
# Use this for Hybrid Anonymization
from dataExtract.real import dataExtractHybrid
from dataExtract.generated.graphNodes import *
import random
import scenarioRunner

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
            
# Allows the running of custom generated graph for the purpose of 
# this research. You can find the exact graphs in baseGraphs folder and
# anonymization folder.
def anonymize_custom(mode, level, runs):
    if mode == 0:
        scenarioRunner.runGraphInitial(runs)
    elif mode == 1:
        scenarioRunner.runGraphAnonymizedInitial(runs, level)
    elif mode == 2:
        scenarioRunner.runGraphMnMInitial(runs)
    else:
        scenarioRunner.runGraphHybrid(runs, level)        
  
# Allows the creation, addition and compilation of graphs
class Camouflage:

    def __init__(self):
        self.graph = []

    def CreateGraph(self):
        self.graph.append('basic_calculations')
        self.graph.append('sorting')
        self.graph.append('encryption')
        self.graph.append('decryption')
        self.graph.append('compression')

    # Function name selects the return value of the generated graph
    # after it runs through all operations.
    # Current available functions are Sorting, Encryption, Addition,
    # Multuplication, 
    def ConnectNodes(self, functionName, level):
        if level == '0':
            level = random.randint(1, 5) - 1
        else:
            level = int(level) - 1

        graph2 = []
        while level > 0:
            g = [0, 1, 2, 3, 4]
            chooseFun = random.choice(g)
            graph2.append(self.graph[chooseFun])
            level -= 1

        graph2.append(functionName)
        self.graph = graph2      

    def Compile(self):
        encrypt = False
        compress = False
        allow = True
        for x in self.graph:
            if compress:
                print('Nodes cannot be connected.')
                self.graph = []
                allow = False
                break
            if encrypt and x != 'decryption':
                print('Nodes cannot be connected.')
                self.graph = []
                allow = False
                break
            elif x == 'encryption':
                encrypt = True
            elif x == 'decryption':
                if not encrypt:
                    print('Nodes cannot be connected.')
                    self.graph = []
                    allow = False
                    break
                encrypt = False
            elif x == 'compression':
                compress = True
        if allow:
            for c in self.graph:
                print(c)
 
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
    
        return output
        
    
if __name__ == '__main__':
    # Choose mode 0 for None.
    # Choose mode 1 for Remodel.
    # Choose mode 2 for Mixing.
    # Choose mode 3 for Hybrid.
    anonymize_real_world(0, 3, 20)
    anonymize_custom(0,3,30)
    arr = [5,3,4,6,8,9]
    # Create a random graph and test if the computation can be identified without anonymization     
    G = Camouflage()
    G.CreateGraph()
    G.ConnectNodes('basic_calculations',3)
    G.Compile()
    # Calculate InputSize, OutputSize and Time for randomly generated graphs    
    G.Anonymize(0, arr, 0)
    
        
        



