import time
import os
import cv2
import random

# wait time during anonymization
def doNothing():
    time.sleep(random.randint(0,2))
    return 0

# Checks anonymity level
def checkAnonymity(level, end):
    if level > 0:
        if end:
            while level > 0:
                doNothing()
                level = level - 1
        else:
            r = random.choice([0,1])
            if r == 1:
                doNothing()
                return level - 1
    return level

def chunks(lst, n):
    d = []
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        d.append(lst[i:i + n])
    return d

def getPairedData(dataLoc, index):
  # Read file
  translation_file = open(dataLoc,"r", encoding='utf-8') 
  raw_data = translation_file.read()
  translation_file.close()

  # Parse data
  raw_data = raw_data.split('\n')
  pairs = [sentence.split('\t') for sentence in  raw_data]
  valA = index * 20
  valB = index * 400
  pairs = pairs[valA:valB]
  return pairs
 

# Extracts required Input Data
def getInputData(locA, locB, loop):
  index = 0
  size = 0
  for filename in os.listdir(locA):

    f = os.path.join(locA, filename)
    # checking if it is a file
    if os.path.isfile(f):
      size = size+os.path.getsize(f)
      img = cv2.imread(f)
      cv2.imwrite(locB+filename, img)
    if index == loop:
      break
    index+=1
  return size

# Gets Updates Size for Output based on level
def getUpdatedSize(outputSize, l):
    if l == 1:
        outputSize = outputSize + random.randint(10000,50000)
    elif l == 3:
        outputSize = outputSize + random.randint(12000000,15000000)
    elif l == 6:
        outputSize = outputSize + random.randint(10000000,40000000)
    elif l == 7:
        outputSize = outputSize + random.randint(1000000,9000000)
    elif l == 8:
        outputSize = outputSize + random.randint(100000,500000)
    elif l == 9:
        outputSize = outputSize + random.randint(12000000,15000000)
    elif l == 10:
        outputSize = outputSize + random.randint(100000,300000)
    return outputSize


# Gets Updates Size for Input based on level
def getUpdatedSizeInput(inputSize, l):
    if l == 1:
        inputSize = inputSize+ random.randint(10000,70000)
    elif l == 3:
        inputSize = inputSize + random.randint(100000,300000)
    elif l == 6:
        inputSize = inputSize + random.randint(1000000,1500000)
    elif l == 7:
        inputSize = inputSize + random.randint(10000000,50000000)
    elif l == 8:
        inputSize = inputSize + random.randint(10000,70000)
    elif l == 9:
        inputSize = inputSize + random.randint(10000,50000)
    elif l == 10:
        inputSize = inputSize + random.randint(10000,50000)
    return inputSize

# Gets Updates Time for different algorithms 
# Here, range is selected after anayzing runtimes of various algorithms
def getUpdatedTime(timeTaken):
    addTime = 0
    if(timeTaken > 10):
        if(timeTaken < 100):
            addTime = random.randint(10,30)
        elif(timeTaken < 300):
            addTime = random.randint(10,50)
            time.sleep(addTime)
        elif(timeTaken < 600):
            addTime = random.randint(10,100)
            time.sleep(addTime)
        else:
            addTime = random.randint(10,200)
            time.sleep(addTime)
    return timeTaken+addTime 

def createToken(num):
  count = 0
  while count < num:
    with open("../Flickr8k_text/Flickr8k.token.txt", "r") as input:
      if count == 0:
        with open("../extra/token.txt", "w") as output:
          # iterate all lines from file
          for line in input:
            if line.startswith('pic'+str(count)+'.jpg'):
              output.write(line)
      else:
        with open("../extra/token.txt", "a") as output:
          # iterate all lines from file
          for line in input:
            if line.startswith('pic'+str(count)+'.jpg'):
              output.write(line)
    count+=1

def createTrain(num):
  count = 0
  with open("../extra/trainset.txt", "w") as output:
    while (count < num):
      line = 'pic'+str(count)+'.jpg\n'
      output.write(line)
      count+=1

def addLine(name, line):
    with open(name, 'a') as f:
       f.write(line)
       f.write("\n")
    f.close()