from functions import graphFunctions

# Sort & Calculate
def graph01(output):
    output = graphFunctions.getArray(output)
    output = graphFunctions.sortArray(output)
    output = graphFunctions.calculateContentsSingle(output)
    return output

# Compress & Encrypt
def graph02(output):
    output = graphFunctions.getArray(output)
    output = graphFunctions.compressGZip(output)
    output = graphFunctions.encryptAESFile(output)
    return output

# Sort & Encrypt
def graph03(output):
    output = graphFunctions.getArray(output)
    output = graphFunctions.sortArray(output)
    output = graphFunctions.encryptAES(output)
    return output

# Calculate & Encrypt
def graph04(output):
    output = graphFunctions.getArray(output)
    output = graphFunctions.calculateContentsSingle(output)
    output = graphFunctions.encryptAES(output)
    return output

# Sort Calculate Compress
def graph05(output1, output2):
    output1 = graphFunctions.getArray(output1)
    output2 = graphFunctions.getArray(output2)
    output1 = graphFunctions.sortArray(output1)
    output2 = graphFunctions.sortArray(output2)
    output = graphFunctions.calculateContents(output1, output2)
    output = graphFunctions.compressGZip(output)
    return output

# Decrypt Calculate Encrypt
def graph06(output1, output2):
    output1 = graphFunctions.decryptAES(output1)
    output2 = graphFunctions.decryptAES(output2)
    output = graphFunctions.fixLength(output1, output2)
    output = graphFunctions.calculateContents(output[0], output[1])
    output = graphFunctions.encryptAES(output)
    return output

# Calculate Compress
def graph07(output1, output2):
    output1 = graphFunctions.getArray(output1)
    output2 = graphFunctions.getArray(output2)
    output1 = graphFunctions.calculateContentsSingle(output1)
    output2 = graphFunctions.calculateContentsSingle(output2)
    output = graphFunctions.calculateContents(output1, output2)
    output = graphFunctions.compressGZip(output)
    return output

# Sort Decrypt Compress Calculate Encrypt
def graph08(output1, output2):
    output1 = graphFunctions.decryptAES(output1)
    output2 = graphFunctions.decryptAES(output2)
    output = graphFunctions.fixLength(output1, output2)
    output1 = graphFunctions.sortArray(output[0])
    output2 = graphFunctions.sortArray(output[1])
    output = graphFunctions.calculateContents(output1, output2)
    output = graphFunctions.compressGZip(output)
    output = graphFunctions.encryptAESFile(output)
    return output

# Sort Calculate
def graph09(output1, output2, output3):
    output1 = graphFunctions.getArray(output1)
    output2 = graphFunctions.getArray(output2)
    output3 = graphFunctions.getArray(output3)
    output1 = graphFunctions.sortArray(output1)
    output2 = graphFunctions.sortArray(output2)
    output3 = graphFunctions.sortArray(output3)
    output = graphFunctions.calculateContents(output1, output2)
    output = graphFunctions.calculateContents(output, output3)
    return output

# Calculate Compress Encrypt
def graph10(output1, output2, output3):
    output1 = graphFunctions.getArray(output1)
    output2 = graphFunctions.getArray(output2)
    output3 = graphFunctions.getArray(output3)
    output = graphFunctions.calculateContents(output1, output2)
    output = graphFunctions.calculateContents(output, output3)
    output = graphFunctions.compressGZip(output)
    output = graphFunctions.encryptAESFile(output)
    return output

# Sort Decrypt Compress Calculate Encrypt
def graph11(output1, output2, output3):
    output1 = graphFunctions.decryptAES(output1)
    output2 = graphFunctions.decryptAES(output2)
    output3 = graphFunctions.decryptAES(output3)
    output = graphFunctions.fixLengthAll(output1, output2, output3)
    output1 = graphFunctions.sortArray(output[0])
    output2 = graphFunctions.sortArray(output[1])
    output3 = graphFunctions.sortArray(output[2])
    output = graphFunctions.calculateContents(output1, output2)
    output = graphFunctions.calculateContents(output, output3)
    output = graphFunctions.compressGZip(output)
    output = graphFunctions.encryptAESFile(output)
    return output

# Decrypt Calculate Encrypt
def graph12(output1, output2, output3):
    output1 = graphFunctions.decryptAES(output1)
    output2 = graphFunctions.decryptAES(output2)
    output3 = graphFunctions.decryptAES(output3)
    output = graphFunctions.fixLengthAll(output1, output2, output3)
    output1 = graphFunctions.calculateContentsSingle(output[0])
    output2 = graphFunctions.calculateContentsSingle(output[1])
    output3 = graphFunctions.calculateContentsSingle(output[2])
    output = graphFunctions.calculateContents(output1, output2)
    output = graphFunctions.calculateContents(output, output3)
    output = graphFunctions.encryptAES(output)
    return output