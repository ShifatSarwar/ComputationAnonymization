from functions import graphFunctions

def graph01(output, level):
    # Calculate Sort 
    level = graphFunctions.checkAnonymity(level, False)
    output = graphFunctions.decryptAES(output)
    level = graphFunctions.checkAnonymity(level, False)
    # output = graphFunctions.getArray(output)
    output = graphFunctions.sortArray(output)
    level = graphFunctions.checkAnonymity(level, False)
    output = graphFunctions.calculateContentsSingle(output)
    level = graphFunctions.checkAnonymity(level, True)
    output = graphFunctions.encryptAES(output)
    level = graphFunctions.checkAnonymity(level, True)
    return output

def graph02(output1, output2, level):
    # Sort Calculate Compress
    level = graphFunctions.checkAnonymity(level, False)
    output1 = graphFunctions.decryptAES(output1)
    level = graphFunctions.checkAnonymity(level, False)
    output2 = graphFunctions.decryptAES(output2)
    level = graphFunctions.checkAnonymity(level, False)
    # output1 = graphFunctions.getArray(output1)
    # output2 = graphFunctions.getArray(output2)
    output = graphFunctions.fixLength(output1, output2)
    output[1] = graphFunctions.sortArray(output[1])
    level = graphFunctions.checkAnonymity(level, False)
    output = graphFunctions.calculateContents(output[0], output[1])
    level = graphFunctions.checkAnonymity(level, False)
    output = graphFunctions.compressGZip(output)
    level = graphFunctions.checkAnonymity(level, True)
    output = graphFunctions.encryptAESFile(output)
    level = graphFunctions.checkAnonymity(level, True)
    return output

def graph03(output1, output2, level):
    # Decrypt Calculate Encrypt
    level = graphFunctions.checkAnonymity(level, False)
    output1 = graphFunctions.decryptAES(output1)
    level = graphFunctions.checkAnonymity(level, False)
    output2 = graphFunctions.decryptAES(output2)
    level = graphFunctions.checkAnonymity(level, False)
    output = graphFunctions.fixLength(output1, output2)
    output = graphFunctions.calculateContents(output[0], output[1])
    level = graphFunctions.checkAnonymity(level, False)
    output = graphFunctions.encryptAES(output)
    level = graphFunctions.checkAnonymity(level, True)
    return output 

def graph04(output1, output2, output3, level):
    # Calculate Compress
    level = graphFunctions.checkAnonymity(level, False)
    output1 = graphFunctions.decryptAES(output1)
    level = graphFunctions.checkAnonymity(level, False)
    output2 = graphFunctions.decryptAES(output2)
    level = graphFunctions.checkAnonymity(level, False)
    output3 = graphFunctions.decryptAES(output3)
    level = graphFunctions.checkAnonymity(level, False)
    # output1 = graphFunctions.getArray(output1)
    # output2 = graphFunctions.getArray(output2)
    # output3 = graphFunctions.getArray(output3)
    output = graphFunctions.fixLengthAll(output1, output2, output3)
    output[0] = graphFunctions.calculateContents(output[0], output[1])
    level = graphFunctions.checkAnonymity(level, False)
    output = graphFunctions.calculateContents(output[0], output[2])
    level = graphFunctions.checkAnonymity(level, False)
    output = graphFunctions.compressGZip(output)
    level = graphFunctions.checkAnonymity(level, True)
    output = graphFunctions.encryptAESFile(output)
    level = graphFunctions.checkAnonymity(level, True)
    return output

def graph05(output1, output2, level):
    # Decrypt Sort Compress Encrypt
    level = graphFunctions.checkAnonymity(level, False)
    output1 = graphFunctions.decryptAES(output1)
    level = graphFunctions.checkAnonymity(level, False)
    output2 = graphFunctions.decryptAES(output2)
    level = graphFunctions.checkAnonymity(level, False)
    output1 = graphFunctions.sortArray(output1)
    level = graphFunctions.checkAnonymity(level, False)
    output2 = graphFunctions.sortArray(output2)
    level = graphFunctions.checkAnonymity(level, False)
    output = []
    output.append(output1)
    output.append(output2)
    output = graphFunctions.compressGZip(output)
    level = graphFunctions.checkAnonymity(level, False)
    output = graphFunctions.encryptAESFile(output)
    level = graphFunctions.checkAnonymity(level, True)
    return output

def graph06(output1,output2, level):
    # Decrypt Sort Encrypt
    level = graphFunctions.checkAnonymity(level, False)
    output1 = graphFunctions.decryptAES(output1)
    level = graphFunctions.checkAnonymity(level, False)
    output2 = graphFunctions.decryptAES(output2)
    level = graphFunctions.checkAnonymity(level, False)
    output1 = graphFunctions.sortArray(output1)
    level = graphFunctions.checkAnonymity(level, False)
    output2 = graphFunctions.sortArray(output2)
    output = []
    output.append(output1)
    output.append(output2)
    level = graphFunctions.checkAnonymity(level, False)
    output = graphFunctions.encryptAES(output)
    level = graphFunctions.checkAnonymity(level, True)
    return output

def graph07(output1, output2, output3, level):
    # Sort Compress Encrypt
    level = graphFunctions.checkAnonymity(level, False)
    output1 = graphFunctions.decryptAES(output1)
    level = graphFunctions.checkAnonymity(level, False)
    output2 = graphFunctions.decryptAES(output2)
    level = graphFunctions.checkAnonymity(level, False)
    output3 = graphFunctions.decryptAES(output3)
    level = graphFunctions.checkAnonymity(level, False)
    output = graphFunctions.fixLengthAll(output1, output2, output3)
    # output1 = graphFunctions.getArray(output1)
    output[0] = graphFunctions.sortArray(output[0])
    level = graphFunctions.checkAnonymity(level, False)
    # output2 = graphFunctions.getArray(output2)
    output[1] = graphFunctions.sortArray(output[1])
    level = graphFunctions.checkAnonymity(level, False)
    # output3 = graphFunctions.getArray(output3)
    output[2] = graphFunctions.sortArray(output[2])
    level = graphFunctions.checkAnonymity(level, False)
    output = graphFunctions.compressGZip(output)
    level = graphFunctions.checkAnonymity(level, False)
    output = graphFunctions.encryptAESFile(output)
    level = graphFunctions.checkAnonymity(level, True)
    return output

def graph08(output, level):
    # Sort Encrypt
    level = graphFunctions.checkAnonymity(level, False)
    output = graphFunctions.decryptAES(output)
    level = graphFunctions.checkAnonymity(level, False)
    # output = graphFunctions.getArray(output)
    output = graphFunctions.sortArray2(output)
    level = graphFunctions.checkAnonymity(level, False)
    output = graphFunctions.encryptAES(output)
    level = graphFunctions.checkAnonymity(level, True)
    return output

def graph09(output, level):
    # Compress Encrypt
    level = graphFunctions.checkAnonymity(level, False)
    output = graphFunctions.decryptAES(output)
    level = graphFunctions.checkAnonymity(level, False)
    # output = graphFunctions.getArray(output)
    output = graphFunctions.compressGZip(output)
    level = graphFunctions.checkAnonymity(level, False)
    output = graphFunctions.encryptAESFile(output)
    level = graphFunctions.checkAnonymity(level, True)
    return output

def graph10(output1, output2,output3, level):
    # Decrypt Calculate Sort Compress
    level = graphFunctions.checkAnonymity(level, False)
    output1 = graphFunctions.decryptAES(output1)
    level = graphFunctions.checkAnonymity(level, False)
    output2 = graphFunctions.decryptAES(output2)
    level = graphFunctions.checkAnonymity(level, False)
    output3 = graphFunctions.decryptAES(output3)
    level = graphFunctions.checkAnonymity(level, False)
    output = graphFunctions.fixLengthAll(output1, output2, output3)
    output[0] = graphFunctions.sortArray(output1)    
    level = graphFunctions.checkAnonymity(level, False)
    output[0] = graphFunctions.calculateContents(output[0], output[1])
    output = graphFunctions.calculateContents(output[0], output[2])
    level = graphFunctions.checkAnonymity(level, False)
    output = graphFunctions.compressGZip(output)
    level = graphFunctions.checkAnonymity(level, False)
    output = graphFunctions.encryptAESFile(output)
    level = graphFunctions.checkAnonymity(level, True)
    return output