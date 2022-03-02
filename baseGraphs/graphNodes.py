from functions import graphFunctions

def graph01(output):
    # Calculate Sort 
    output = graphFunctions.decryptAES(output)
    # output = graphFunctions.getArray(output)
    output = graphFunctions.sortArray(output)
    output = graphFunctions.calculateContentsSingle(output)
    output = graphFunctions.encryptAES(output)
    return output

def graph02(output1, output2):
    # Sort Calculate Compress
    output1 = graphFunctions.decryptAES(output1)
    output2 = graphFunctions.decryptAES(output2)
    # output1 = graphFunctions.getArray(output1)
    # output2 = graphFunctions.getArray(output2)
    output = graphFunctions.fixLength(output1, output2)
    output[1] = graphFunctions.sortArray(output[1])
    output = graphFunctions.calculateContents(output[0], output[1])
    output = graphFunctions.compressGZip(output)
    output = graphFunctions.encryptAESFile(output)
    return output

def graph03(output1, output2):
    # Decrypt Calculate Encrypt
    output1 = graphFunctions.decryptAES(output1)
    output2 = graphFunctions.decryptAES(output2)
    output = graphFunctions.fixLength(output1, output2)
    output = graphFunctions.calculateContents(output[0], output[1])
    output = graphFunctions.encryptAES(output)
    return output 

def graph04(output1, output2, output3):
    # Calculate Compress
    output1 = graphFunctions.decryptAES(output1)
    output2 = graphFunctions.decryptAES(output2)
    output3 = graphFunctions.decryptAES(output3)
    output = graphFunctions.fixLengthAll(output1, output2, output3)
    # output1 = graphFunctions.getArray(output1)
    # output2 = graphFunctions.getArray(output2)
    # output3 = graphFunctions.getArray(output3)
    output[0] = graphFunctions.calculateContents(output[0], output[1])
    output = graphFunctions.calculateContents(output[0], output[2])
    output = graphFunctions.compressGZip(output)
    output = graphFunctions.encryptAESFile(output)
    return output

def graph05(output1, output2):
    # Decrypt Sort Compress Encrypt
    output1 = graphFunctions.decryptAES(output1)
    output2 = graphFunctions.decryptAES(output2)
    output1 = graphFunctions.sortArray(output1)
    output2 = graphFunctions.sortArray(output2)
    output = []
    output.append(output1)
    output.append(output2)
    output = graphFunctions.compressGZip(output)
    output = graphFunctions.encryptAESFile(output)
    return output

def graph06(output1,output2):
    # Decrypt Sort Encrypt
    output1 = graphFunctions.decryptAES(output1)
    output2 = graphFunctions.decryptAES(output2)
    output1 = graphFunctions.sortArray(output1)
    output2 = graphFunctions.sortArray(output2)
    output = []
    output.append(output1)
    output.append(output2)
    output = graphFunctions.encryptAES(output)
    return output

def graph07(output1, output2, output3):
    # Sort Compress Encrypt
    output1 = graphFunctions.decryptAES(output1)
    output2 = graphFunctions.decryptAES(output2)
    output3 = graphFunctions.decryptAES(output3)
    output = graphFunctions.fixLengthAll(output1, output2, output3)
    # output1 = graphFunctions.getArray(output1)
    # output2 = graphFunctions.getArray(output2)
    # output3 = graphFunctions.getArray(output3)
    output[0] = graphFunctions.sortArray(output[0])
    output[1] = graphFunctions.sortArray(output[1])
    output[2]= graphFunctions.sortArray(output[2])
    # output = []
    # output.append(output1)
    # output.append(output2)
    # output.append(output3)
    output = graphFunctions.compressGZip(output)
    output = graphFunctions.encryptAESFile(output)
    return output

def graph08(output):
    # Sort Encrypt
    output = graphFunctions.decryptAES(output)
    # output = graphFunctions.getArray(output)
    output = graphFunctions.sortArray2(output)
    output = graphFunctions.encryptAES(output)
    return output

def graph09(output):
    # Compress Encrypt
    output = graphFunctions.decryptAES(output)
    # output = graphFunctions.getArray(output)
    output = graphFunctions.compressGZip(output)
    output = graphFunctions.encryptAESFile(output)
    return output

def graph10(output1, output2,output3):
    # Decrypt Calculate Sort Compress
    output1 = graphFunctions.decryptAES(output1)
    output2 = graphFunctions.decryptAES(output2)
    output3 = graphFunctions.decryptAES(output3)
    output = graphFunctions.fixLengthAll(output1, output2, output3)
    output[0] = graphFunctions.sortArray(output[0])
    output[0] = graphFunctions.calculateContents(output[0], output[1])
    output = graphFunctions.calculateContents(output[0], output[2])
    output = graphFunctions.compressGZip(output)
    output = graphFunctions.encryptAESFile(output)
    return output




# def graph01(output):
#     # Calculate Sort 
#     # output = graphFunctions.decryptAES(output1)
#     output = graphFunctions.getArray(output)
#     output = graphFunctions.sortArray(output)
#     output = graphFunctions.calculateContentsSingle(output)
#     # output = graphFunctions.encryptAES(output)
#     return output

# def graph02(output1, output2):
#     # Sort Calculate Compress
#     # output1 = graphFunctions.decryptAES(output1)
#     # output2 = graphFunctions.decryptAES(output2)
#     output1 = graphFunctions.getArray(output1)
#     output2 = graphFunctions.getArray(output2)
#     output2 = graphFunctions.sortArray(output2)
#     # output = graphFunctions.fixLength(output1, output2)
#     output = graphFunctions.calculateContents(output1, output2)
#     output = graphFunctions.compressGZip(output)
#     # output = graphFunctions.encryptAESFile(output)
#     return output

# def graph03(output1, output2):
#     # Decrypt Calculate Encrypt
#     output1 = graphFunctions.decryptAES(output1)
#     output2 = graphFunctions.decryptAES(output2)
#     output = graphFunctions.fixLength(output1, output2)
#     output = graphFunctions.calculateContents(output[0], output[1])
#     output = graphFunctions.encryptAES(output)
#     return output 

# def graph04(output1, output2, output3):
#     # Calculate Compress
#     # output1 = graphFunctions.decryptAES(output1)
#     # output3 = graphFunctions.decryptAES(output3)
#     # output = graphFunctions.fixLength(output1, output3)
#     output1 = graphFunctions.getArray(output1)
#     output2 = graphFunctions.getArray(output2)
#     output3 = graphFunctions.getArray(output3)
#     output = graphFunctions.calculateContents(output1, output2)
#     # output2 = graphFunctions.decryptAES(output2)
#     # output = graphFunctions.fixLength(output, output2)
#     output = graphFunctions.calculateContents(output, output3)
#     output = graphFunctions.compressGZip(output)
#     # output = graphFunctions.encryptAESFile(output)
#     return output

# def graph05(output1, output2):
#     # Decrypt Sort Compress Encrypt
#     output1 = graphFunctions.decryptAES(output1)
#     output2 = graphFunctions.decryptAES(output2)
#     output1 = graphFunctions.sortArray(output1)
#     output2 = graphFunctions.sortArray(output2)
#     output = []
#     output.append(output1)
#     output.append(output2)
#     output = graphFunctions.compressGZip(output)
#     output = graphFunctions.encryptAESFile(output)
#     return output

# def graph06(output1,output2):
#     # Decrypt Sort Encrypt
#     output1 = graphFunctions.decryptAES(output1)
#     output2 = graphFunctions.decryptAES(output2)
#     output1 = graphFunctions.sortArray(output1)
#     output2 = graphFunctions.sortArray(output2)
#     output = []
#     output.append(output1)
#     output.append(output2)
#     output = graphFunctions.encryptAES(output)
#     return output

# def graph07(output1, output2, output3):
#     # Sort Compress Encrypt
#     # output1 = graphFunctions.decryptAES(output1)
#     # output2 = graphFunctions.decryptAES(output2)
#     # output3 = graphFunctions.decryptAES(output3)
#     output1 = graphFunctions.getArray(output1)
#     output2 = graphFunctions.getArray(output2)
#     output3 = graphFunctions.getArray(output3)
#     output1 = graphFunctions.sortArray(output1)
#     output2 = graphFunctions.sortArray(output2)
#     output3 = graphFunctions.sortArray(output3)
#     output = []
#     output.append(output1)
#     output.append(output2)
#     output.append(output3)
#     output = graphFunctions.compressGZip(output)
#     output = graphFunctions.encryptAESFile(output)
#     return output

# def graph08(output):
#     # Sort Encrypt
#     # output = graphFunctions.decryptAES(file)
#     output = graphFunctions.getArray(output)
#     output = graphFunctions.sortArray2(output)
#     output = graphFunctions.encryptAES(output)
#     return output

# def graph09(output):
#     # Compress Encrypt
#     # output = graphFunctions.decryptAES(output)
#     output = graphFunctions.getArray(output)
#     output = graphFunctions.compressGZip(output)
#     output = graphFunctions.encryptAESFile(output)
#     return output

# def graph10(output1, output2,output3):
#     # Decrypt Calculate Sort Compress
#     output1 = graphFunctions.decryptAES(output1)
#     output2 = graphFunctions.decryptAES(output2)
#     output3 = graphFunctions.decryptAES(output3)
#     output = graphFunctions.fixLengthAll(output1, output2, output3)
#     output = graphFunctions.sortArray(output1)
#     output[0] = graphFunctions.calculateContents(output[0], output[1])
#     output = graphFunctions.calculateContents(output[0], output[2])
#     output = graphFunctions.compressGZip(output)
#     output = graphFunctions.encryptAESFile(output)
#     return output



