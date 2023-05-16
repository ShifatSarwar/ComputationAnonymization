import time
import os
import pickle
import pandas as pd
import cv2
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
from utility import *
# from tensorflow.keras.datasets import fashion_mnist


# The flower dataset needs to be available and choose the path of your dataset
daisyLocA='extra/flower_photos_ma/daisy/'
daisyLocB='extra/flower_photos/daisy/'
roseLocA='extra/flower_photos_ma/roses/'
roseLocB='extra/flower_photos/roses/'
dandilionLocA='extra/flower_photos_ma/dandelion/'
dandilionLocB='extra/flower_photos/dandelion/'
sunflowerLocA='extra/flower_photos_ma/sunflowers/'
sunflowerLocB='extra/flower_photos/sunflower/'
tulipLocA='extra/flower_photos_ma/tulips/'
tulipLocB='extra/flower_photos/tulip/'


# Connects and Extarct data for G1
def runImageEnhancement(path, level):
    level = checkAnonymity(level, False)
    img = loadImageIE(path)
    level = checkAnonymity(level, False)
    img = inverteIE(img)
    level = checkAnonymity(level, False)
    img = dehazeIE(img)
    level = checkAnonymity(level, False)
    img = inverteIE(img)
    level = checkAnonymity(level, True)
    return img

# Connects and Extarct data for G2
def runDeepLearning(path, level): 
  level = checkAnonymity(level, False)
  fileLoc = path+'flowers/'
  classList = getClass(path+'extra/flower_photos/')
  trainSet = get_data(fileLoc+'/train', classList)
  level = checkAnonymity(level, False)

  validationSet = get_data(fileLoc+'/val', classList)
  level = checkAnonymity(level, False)
  x_train, y_train, x_val, y_val = getSplit(trainSet, validationSet)
  level = checkAnonymity(level, False)
  augmentTrain(x_train)
  level = checkAnonymity(level, False)
  model = defineNetworkA(classList)
  level = checkAnonymity(level, False)
  hist = trainModel(model, x_train, y_train, x_val, y_val)
  level = checkAnonymity(level, True)
  return hist

# Connects and Extarct data for G3
def runObjectDetection(classPath, index, level):
    level = checkAnonymity(level, False)
    x = getFramesOD(classPath, index)
    level = checkAnonymity(level, False)
    x = preProcessImageOD(x)
    level = checkAnonymity(level, False)
    c = getClassOD(classPath)
    level = checkAnonymity(level, False)
    m = getModelOD(classPath)
    level = checkAnonymity(level, False)
    imageArray = getBoundingBoxesOD(m,x,c)
    level = checkAnonymity(level, True)
    return imageArray

# Connects and Extarct data for G4
def runMultilabelAlgorithm(rawData, level):
  level = checkAnonymity(level, False)  
  arxiv_data = getData(rawData)
  level = checkAnonymity(level, False)
  arxiv_data_filtered = filter_data(arxiv_data)
  level = checkAnonymity(level, False)
  arxiv_data_filtered = create_list_string(arxiv_data_filtered)
  level = checkAnonymity(level, False)
  train_df, test_df, val_df = split_train_test(arxiv_data_filtered)
  level = checkAnonymity(level, False)
  terms, lookup, vocab, max_seqlen, batch_size, padding_token, auto = get_preprocess_data(train_df)
  level = checkAnonymity(level, False)
  train_dataset = make_dataset(train_df,  max_seqlen, batch_size, padding_token, auto, lookup, is_train=True)
  level = checkAnonymity(level, False)
  validation_dataset = make_dataset(val_df,  max_seqlen, batch_size, padding_token, auto, lookup, is_train=False)
  level = checkAnonymity(level, False)
  test_dataset = make_dataset(test_df,  max_seqlen, batch_size, padding_token, auto, lookup, is_train=False)
  level = checkAnonymity(level, False)
  train_dataset, validation_dataset, test_dataset = vectorize(train_df, train_dataset, validation_dataset, test_dataset, auto)
  level = checkAnonymity(level, False)
  shallow_mlp_model = make_model(lookup)
  level = checkAnonymity(level, False)
  history = train_model(shallow_mlp_model, train_dataset, validation_dataset)
  level = checkAnonymity(level, True)
  return history

# Connect and Extarct data for G5
def runLanguageTranslationLSTM(pairs, level):
    level = checkAnonymity(level, False) 
    english_sentences = [clean_sentence(pair[0]) for pair in pairs]
    level = checkAnonymity(level, False) 
    french_sentences = [clean_sentence(pair[1]) for pair in pairs]
    level = checkAnonymity(level, False) 
    french_text_tokenized, spa_text_tokenizer = tokenize(french_sentences)
    level = checkAnonymity(level, False) 
    eng_text_tokenized, eng_text_tokenizer = tokenize(english_sentences)
    level = checkAnonymity(level, False) 
    spanish_vocab = len(spa_text_tokenizer.word_index) + 1
    english_vocab = len(eng_text_tokenizer.word_index) + 1
    spa_pad_sentence, eng_pad_sentence, max_spanish_len, max_english_len= makeEqualLength(french_text_tokenized, eng_text_tokenized)
    level = checkAnonymity(level, False) 
    getEmbeddingLayer(spanish_vocab, max_spanish_len)
    level = checkAnonymity(level, False) 
    lstmEncoder(spanish_vocab, max_spanish_len)
    level = checkAnonymity(level, False) 
    lstmDecoder(spanish_vocab, max_spanish_len, max_english_len)
    level = checkAnonymity(level, False) 
    decoderL2(spanish_vocab, max_spanish_len, max_english_len)
    level = checkAnonymity(level, False) 
    logits, input_sequence = denseLayer(spanish_vocab, max_spanish_len, max_english_len, english_vocab)
    level = checkAnonymity(level, False) 
    enc_dec_model = getModel(logits, input_sequence)
    level = checkAnonymity(level, False) 
    model = train_model(enc_dec_model, eng_pad_sentence,spa_pad_sentence)
    level = checkAnonymity(level, True) 
    return model

# Connect and Extarct data for G6
def runSyntheticGAN(x_train, y_train, x_test, y_test, level):
   img_shape = (28,28,1)
   z_dim = 100
   level = checkAnonymity(level, False) 
   discrimination = discriminatorSG(img_shape)
   level = checkAnonymity(level, False) 
   discrimination = compile_discriminatorSG(discrimination)
   level = checkAnonymity(level, False) 
   generation = generatorSG(z_dim)
   level = checkAnonymity(level, False) 
   cgano = cganSG(generation, discrimination)
   level = checkAnonymity(level, False) 
   cgano = compile_cganSG(cgano)
   level = checkAnonymity(level, False) 
   trainSG(generation, discrimination, cgano, x_train, y_train, x_test, y_test)
   level = checkAnonymity(level, True) 

# Connect and Extarct data for G7
# To run needs descriptions.txt dataset for image captions
def runImageCaptioning(train, level):
    level = checkAnonymity(level, False) 
    # descriptions use your own location
    train_descriptions = load_clean_descriptionsICT('extra/descriptions.txt', train)
    level = checkAnonymity(level, False) 
    # photo features
    train_features = load_photo_featuresICT('extra/features.pkl', train)
    level = checkAnonymity(level, False) 
    # prepare tokenizer
    tokenizer = create_tokenizerICT(train_descriptions)
    level = checkAnonymity(level, False) 
    # save the tokenizer save in your created folder
    dump(tokenizer, open('extra/tokenizer.pkl', 'wb'))
    vocab_size = len(tokenizer.word_index) + 1
    level = checkAnonymity(level, False) 
    # determine the maximum sequence length
    max_length = get_max_lengthICT(train_descriptions)
    level = checkAnonymity(level, False) 
    # define the model
    model = define_modelICT(vocab_size, max_length)
    level = checkAnonymity(level, False) 
    # train the model, run epochs manually and save after each epoch
    epochs = 15
    steps = len(train_descriptions)
    for i in range(epochs):
        # create the data generator
        generator = data_generatorICT(train_descriptions, train_features, tokenizer, max_length, vocab_size)
        # fit for one epoch
        model.fit_generator(generator, epochs=1, steps_per_epoch=steps, verbose=1)
        # save model
        model.save('extra/model_last.h5')
    level = checkAnonymity(level, True) 

# Connect and Extarct data for G8
def runImageCaptionGenerator(photoLoc , level):
    level = checkAnonymity(level, False) 
    model = loadModelIC()
    # load the tokenizer
    tokenizer = loadTokenizerIC()
    level = checkAnonymity(level, False) 
    # load and prepare the photograph
    photo = extract_featuresIC(photoLoc)
    level = checkAnonymity(level, False) 
    description = generate_descIC(model, tokenizer, photo)
    level = checkAnonymity(level, False) 
    writeToFileIC(description)
    level = checkAnonymity(level, True) 

# Connect and Extarct data for G9
def runNeuralNetwork(rawData, level):
    level = checkAnonymity(level, False) 
    X,y = preProcessNN(rawData)
    level = checkAnonymity(level, False) 
    X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2, random_state=3, stratify=y)
    level = checkAnonymity(level, False) 
    dummy_y, dummy_v = transformDataNN(y_train, y_test)
    level = checkAnonymity(level, False) 
    model = getModelNN(X_train, dummy_y)
    level = checkAnonymity(level, True) 
    return model

# Connect and Extarct data for G10
def getClusterAnalysis(rawData, level):
    level = checkAnonymity(level, False) 
    X,y = preProcessCN(rawData)
    level = checkAnonymity(level, False) 
    X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2, random_state=3, stratify=y)
    level = checkAnonymity(level, False) 
    model = trainCN(X_train, y_train)
    level = checkAnonymity(level, True) 
    return model

# The next part contains get methods that prepares the inputs and
# allows for monitoring the graph executions

# Prepares the data before passing to G10 to collect results from it
# Needs data from the Flicker8k Dataset
# Or any other image set
def getDataImageEnhance(loop, level):
    index = 0
    # Use your own file location
    path = 'extra/Flicker8k_Dataset'
    for filename in os.listdir(path):
        l = level
        index += 1
        f = os.path.join(path, filename)
        # checking if it is a file
        if os.path.isfile(f):
            inputSize = os.path.getsize(f)
        start_time = time.time()
        output = runImageEnhancement(f, level)
        timeTaken = time.time()-start_time
        outputSize = sys.getsizeof(output)
        while(l != 0):
            if(l == 1):
                outputSize = outputSize+random.randint(10000,100000)
            elif(l == 2):
                outputSize = outputSize+random.randint(1000,10000)
            elif(l == 3):
                outputSize = outputSize+random.randint(100,1000)
            elif(l == 4):
                outputSize = outputSize+random.randint(10,100)
            else:
                outputSize = outputSize+random.randint(1,10)
            l = l -1
        if(timeTaken > 10):
            if(timeTaken < 100):
                timeTaken = timeTaken + random.randint(10,30)
            elif(timeTaken < 300):
                timeTaken = timeTaken + random.randint(10,50)
            elif(timeTaken < 600):
                timeTaken = timeTaken + random.randint(10,100)
            else:
                timeTaken = timeTaken + random.randint(10,200)

        # Assign location for data generation and fix the lower parts for all graphs
        dataLine = 'graph01,'+str(inputSize)+','+str(outputSize)+','+str(timeTaken)+',0'
        addLine('dataList/remodel/ml1.csv', dataLine)
        #   addLine('dataList/remodel/level'+str(level)+'/ml1.csv',dataLine)
        if index == loop:
            break

# Prepares the data before passing to G2 to collect results from it
def getDataDeepLearning(loop, level):
    index = 1
    while(index <= loop):
        l = level
        path = ''
        # Calculates size of all Inputs
        sizeA = getInputData(daisyLocA,daisyLocB, 10*index)
        sizeB = getInputData(roseLocA,roseLocB, 10*index)
        sizeC = getInputData(dandilionLocA,dandilionLocB, 14*index)
        sizeD = getInputData(sunflowerLocA,sunflowerLocB, 10*index)
        sizeE = getInputData(tulipLocA,tulipLocB, 12*index)
        inputSize = sizeA+sizeB+sizeC+sizeD+sizeE
        dataLoc = 'extra/flower_photos/'
        fileLoc = 'flowers/'
        start_time = time.time()
        split(dataLoc,fileLoc)
        # Sends data to run graph
        output = runDeepLearning(path, level)
        # Saves Time
        timeTaken = time.time()-start_time
        # Saves Output
        filename = 'models/finalized_model.sav'
        pickle.dump(output, open(filename, 'wb'))
        # Calculates Output Size
        outputSize = os.path.getsize(filename)
        # Adjusts output size based on levels
        while(l != 0):
            if(l == 1):
                outputSize = outputSize+random.randint(10000000,100000000)
            elif(l == 2):
                outputSize = outputSize+random.randint(1000000,10000000)
            elif(l == 3):
                outputSize = outputSize+random.randint(100000,1000000)
            elif(l == 4):
                outputSize = outputSize+random.randint(10000,100000)
            else:
                outputSize = outputSize+random.randint(1000,10000)
            l = l -1
        # Adjusts time wait based on graph time
        if(timeTaken > 10):
            if(timeTaken < 100):
                timeTaken = timeTaken + random.randint(10,30)
            elif(timeTaken < 300):
                timeTaken = timeTaken + random.randint(10,50)
            elif(timeTaken < 600):
                timeTaken = timeTaken + random.randint(10,100)
            else:
                timeTaken = timeTaken + random.randint(10,200)

        dataLine = 'graph02,'+str(inputSize)+','+str(outputSize)+','+str(timeTaken)+',1'
        addLine('dataList/remodel/level'+str(level)+'/ml2.csv',dataLine)
        index += 1

# Prepares the data before passing to G3 to collect results from it
def getDataObjectDetection(loop, level):
    index = 5
    while(index < loop):
        l = level
        classPath = 'extra/'
        inputSize = os.path.getsize(classPath+'classes.txt')
        start_time = time.time()
        output = runObjectDetection(classPath, index, level)
        timeTaken = time.time()-start_time
        outputSize = sys.getsizeof(output)
        inputSize = inputSize + outputSize
        while(l != 0):
            if(l == 1):
                outputSize = outputSize+random.randint(1000,10000)
            elif(l == 2):
                outputSize = outputSize+random.randint(1000,10000)
            elif(l == 3):
                outputSize = outputSize+random.randint(100,1000)
            elif(l == 4):
                outputSize = outputSize+random.randint(10,100)
            else:
                outputSize = outputSize+random.randint(1,10)
            l = l -1
        if(timeTaken > 10):
            if(timeTaken < 100):
                timeTaken = timeTaken + random.randint(10,30)
            elif(timeTaken < 300):
                timeTaken = timeTaken + random.randint(10,50)
            elif(timeTaken < 600):
                timeTaken = timeTaken + random.randint(10,100)
            else:
                timeTaken = timeTaken + random.randint(10,200) 
        dataLine = 'graph03,'+str(inputSize)+','+str(outputSize)+','+str(timeTaken)+',2'
        addLine('dataList/remodel/ml3.csv', dataLine)
        # addLine('dataList/remodel/level'+str(level)+'/ml3.csv',dataLine)
        index += 1


# Prepares the data before passing to G4 to collect results from it
def getDataMultilabelText(i, loop, level):
    index = i
    while(index <= loop):
        l = level
        fileLoc = 'dataList/remodel/trainset'+str(index)+'.csv'
        inputSize = os.path.getsize(fileLoc)
        start_time = time.time()
        output = runMultilabelAlgorithm(fileLoc, level)
        timeTaken = time.time()-start_time
        filename = 'models/finalized_model.sav'
        pickle.dump(output, open(filename, 'wb'))
        outputSize = os.path.getsize(filename)
        while(l != 0):
            if(l == 1):
                outputSize = outputSize+random.randint(10000000,100000000)
            elif(l == 2):
                outputSize = outputSize+random.randint(1000000,10000000)
            elif(l == 3):
                outputSize = outputSize+random.randint(100000,1000000)
            elif(l == 4):
                outputSize = outputSize+random.randint(10000,100000)
            else:
                outputSize = outputSize+random.randint(1000,10000)
            l = l -1
        if(timeTaken > 10):
            if(timeTaken < 100):
                timeTaken = timeTaken + random.randint(10,30)
            elif(timeTaken < 300):
                timeTaken = timeTaken + random.randint(10,50)
            elif(timeTaken < 600):
                timeTaken = timeTaken + random.randint(10,100)
            else:
                timeTaken = timeTaken + random.randint(10,200)
        dataLine = 'graph04,'+str(inputSize)+','+str(outputSize)+','+str(timeTaken)+',3'
        addLine('dataList/remodel/level'+str(level)+'/ml4.csv',dataLine)
        index += 1

# Prepares the data before passing to G5 to collect results from it
def getDataLanguageLSTM(loop, level):
    index = 1 
    while(index <= loop):
        l = level
        fileLoc = 'extra/eng-fra.txt'
        pairs = getPairedData(fileLoc, index)
        inputSize = sys.getsizeof(pairs)
        start_time = time.time()
        output = runLanguageTranslationLSTM(pairs, level)
        timeTaken = time.time()-start_time
        filename = 'models/finalized_model.sav'
        pickle.dump(output, open(filename, 'wb'))
        outputSize = os.path.getsize(filename)
        while(l != 0):
            if(l == 1):
                outputSize = outputSize+(random.randint(1000000,10000000))
            elif(l == 2):
                outputSize = outputSize+random.randint(100000,1000000)
            elif(l == 3):
                outputSize = outputSize+random.randint(10000,100000)
            elif(l == 4):
                outputSize = outputSize+random.randint(1000,10000)
            else:
                outputSize = outputSize+random.randint(100,1000)
            l = l -1
        if(timeTaken > 10):
            if(timeTaken < 100):
                timeTaken = timeTaken + random.randint(10,30)
            elif(timeTaken < 300):
                timeTaken = timeTaken + random.randint(10,50)
            elif(timeTaken < 600):
                timeTaken = timeTaken + random.randint(10,100)
            else:
                timeTaken = timeTaken + random.randint(10,200)

        dataLine = 'graph05,'+str(inputSize)+','+str(outputSize)+','+str(timeTaken)+',4'
        addLine('dataList/remodel/level'+str(level)+'/ml5.csv',dataLine)
        index += 1

# Prepares the data before passing to G6 to collect results from it
def getDataSyntheticGAN(loop, level):
    index = 1
    while(index <= loop):
        l = level
        (x_train, y_train), (x_test, y_test)  = fashion_mnist.load_data()
        tSize = index*1200
        vSize = index*200
        xT = chunks(x_train, tSize)
        yT = chunks(y_train, tSize)
        xV = chunks(x_test, vSize)
        yV = chunks(y_test, vSize)
        x_train = xT[0]
        y_train = yT[0]
        x_test = xV[0]
        y_test = yV[0]
        arr_reshaped1 = x_train.reshape(x_train.shape[0], -1)
        arr_reshaped2 = y_train.reshape(y_train.shape[0], -1)
        arr_reshaped3 = x_test.reshape(x_test.shape[0], -1)
        arr_reshaped4 = y_test.reshape(y_test.shape[0], -1)
        pd.DataFrame(arr_reshaped1).to_csv("dataList/remodel/file1.csv")
        pd.DataFrame(arr_reshaped2).to_csv("dataList/remodel/file2.csv")
        pd.DataFrame(arr_reshaped3).to_csv("dataList/remodel/file3.csv")
        pd.DataFrame(arr_reshaped4).to_csv("dataList/remodel/file4.csv")
        p = 'dataList/remodel/file'
        inputSize = os.path.getsize(p+'1.csv')+os.path.getsize(p+'2.csv')+os.path.getsize(p+'3.csv')+os.path.getsize(p+'4.csv')
        start_time = time.time()
        runSyntheticGAN(x_train, y_train, x_test, y_test, level)
        timeTaken = time.time()-start_time
        outputSize = os.path.getsize('extra/samples/image.jpg')
        while(l != 0):
            if(l == 1):
                outputSize = outputSize+random.randint(10000,100000)
            elif(l == 2):
                outputSize = outputSize+random.randint(1000,10000)
            elif(l == 3):
                outputSize = outputSize+random.randint(100,1000)
            elif(l == 4):
                outputSize = outputSize+random.randint(10,100)
            else:
                outputSize = outputSize+random.randint(1,10)
            l = l -1
        if(timeTaken > 10):
            if(timeTaken < 100):
                timeTaken = timeTaken + random.randint(10,30)
            elif(timeTaken < 300):
                timeTaken = timeTaken + random.randint(10,50)
            elif(timeTaken < 600):
                timeTaken = timeTaken + random.randint(10,100)
            else:
                timeTaken = timeTaken + random.randint(10,200)
        
        dataLine = 'graph06,'+str(inputSize)+','+str(outputSize)+','+str(timeTaken)+',5'
        addLine('dataList/remodel/level'+str(level)+'/ml6.csv',dataLine)
        index += 1

# Prepares the data before passing to G7 to collect results from it
def getDataImageCaptioning(loop,level):
    index = 1
    while(index <= loop):
        l = level
        # extract features from all images
        directory = 'Flicker8k_Dataset'
        features = extract_features(directory, index*10)
        # save to file output 1
        dump(features, open('extra/features.pkl', 'wb'))
        filename = 'Flickr8k_text/Flickr8k.token.txt'
        createToken(index*10)
        filename = 'extra/token.txt'
        # load descriptions
        doc = load_docICT(filename)
        # parse descriptions
        descriptions = load_descriptionsICT(doc)
        # clean descriptions
        clean_descriptionsICT(descriptions)
        # summarize vocabulary
        vocabulary = to_vocabularyICT(descriptions)
        save_descriptionsICT(descriptions, 'extra/descriptions.txt')
        filename = 'extra/Flickr8k_text/Flickr_8k.trainImages.txt'
        createTrain(index*10-(0.2*index*10))
        filename = 'extra/trainset.txt'
        train = load_setICT(filename)
        inputSize = os.path.getsize('extra/features.pkl')
        inputSize = inputSize + os.path.getsize('extra/descriptions.txt')
        inputSize = inputSize + os.path.getsize('extra/Flickr8k_text/Flickr_8k.trainImages.txt')
        start_time = time.time()
        runImageCaptioning(train, level)
        timeTaken = time.time()-start_time
        outputSize = os.path.getsize('models/model_last.h5')
        while(l != 0):
            if(l == 1):
                outputSize = outputSize+random.randint(1000000,10000000)
            elif(l == 2):
                outputSize = outputSize+random.randint(100000,1000000)
            elif(l == 3):
                outputSize = outputSize+random.randint(10000,100000)
            elif(l == 4):
                outputSize = outputSize+random.randint(1000,10000)
            else:
                outputSize = outputSize+random.randint(100,1000)
            l = l -1
        if(timeTaken > 10):
            if(timeTaken < 100):
                timeTaken = timeTaken + random.randint(10,30)
            elif(timeTaken < 300):
                timeTaken = timeTaken + random.randint(10,50)
            elif(timeTaken < 600):
                timeTaken = timeTaken + random.randint(10,100)
            else:
                timeTaken = timeTaken + random.randint(10,200)
        dataLine = 'graph07,'+str(inputSize)+','+str(outputSize)+','+str(timeTaken)+',6'
        addLine('dataList/remodel/level'+str(level)+'/ml7.csv',dataLine)
        index += 1

# Prepares the data before passing to G8 to collect results from it
def getDataImageCaption(loop,level):
    index = 0
    while(index < loop):
        l = level
        # extract features from all images
        directory = 'extra/Flicker8k_Dataset/pic'+str(index)+'.jpg'
        inputSize = os.path.getsize(directory)
        start_time = time.time()
        runImageCaptionGenerator(directory, level)
        timeTaken = time.time()-start_time
        outputSize = os.path.getsize('extra/output.txt')
        while(l != 0):
            if(l == 1):
                outputSize = outputSize+random.randint(1000,10000)
            elif(l == 2):
                outputSize = outputSize+random.randint(1000,10000)
            elif(l == 3):
                outputSize = outputSize+random.randint(100,1000)
            elif(l == 4):
                outputSize = outputSize+random.randint(10,100)
            else:
                outputSize = outputSize+random.randint(1,10)
            l = l -1
        if(timeTaken > 10):
            if(timeTaken < 100):
                timeTaken = timeTaken + random.randint(10,30)
            elif(timeTaken < 300):
                timeTaken = timeTaken + random.randint(10,50)
            elif(timeTaken < 600):
                timeTaken = timeTaken + random.randint(10,100)
            else:
                timeTaken = timeTaken + random.randint(10,200)
        dataLine = 'graph08,'+str(inputSize)+','+str(outputSize)+','+str(timeTaken)+',7'
        addLine('dataList/remodel/ml8.csv', dataLine)
        # addLine('dataList/remodel/level'+str(level)+'/ml8.csv',dataLine)
        index += 1

# Prepares the data before passing to G9 to collect results from it
def getDataNeuralNetwork(loop, level):
    index = 0
    while(index < loop):
        l = level
        fileLoc = 'extra/samples/csvs/trainset'+str(index)+'.csv'
        inputSize = os.path.getsize(fileLoc)
        start_time = time.time()
        output = runNeuralNetwork(fileLoc, level)
        timeTaken = time.time()-start_time
        filename = 'models/finalized_model.sav'
        pickle.dump(output, open(filename, 'wb'))
        outputSize = os.path.getsize(filename)
        while(l != 0):
            if(l == 1):
                outputSize = outputSize+random.randint(1000000,10000000)
            elif(l == 2):
                outputSize = outputSize+random.randint(100000,1000000)
            elif(l == 3):
                outputSize = outputSize+random.randint(10000,100000)
            elif(l == 4):
                outputSize = outputSize+random.randint(1000,10000)
            else:
                outputSize = outputSize+random.randint(100,1000)
            l = l -1
        if(timeTaken > 10):
            if(timeTaken < 100):
                timeTaken = timeTaken + random.randint(10,30)
            elif(timeTaken < 300):
                timeTaken = timeTaken + random.randint(10,50)
            elif(timeTaken < 600):
                timeTaken = timeTaken + random.randint(10,100)
            else:
                timeTaken = timeTaken + random.randint(10,200)
        dataLine = 'graph09,'+str(inputSize)+','+str(outputSize)+','+str(timeTaken)+',8'
        addLine('dataList/remodel/ml9.csv', dataLine)
        # addLine('dataList/remodel/level'+str(level)+'/ml9.csv',dataLine)
        index += 1

# Prepares the data before passing to G10 to collect results from it
def getDataSimpleCluster(loop, level):
    index = 0
    while(index < loop):
        l = level
        fileLoc = 'extra/samples/csvs/trainset'+str(index)+'.csv'
        inputSize = os.path.getsize(fileLoc)
        start_time = time.time()
        output = getClusterAnalysis(fileLoc, level)
        timeTaken = time.time()-start_time
        filename = 'models/finalized_model.sav'
        pickle.dump(output, open(filename, 'wb'))
        outputSize = os.path.getsize(filename)
        while(l != 0):
            if(l == 1):
                outputSize = outputSize+random.randint(10000,100000)
            elif(l == 2):
                outputSize = outputSize+random.randint(1000,10000)
            elif(l == 3):
                outputSize = outputSize+random.randint(100,1000)
            elif(l == 4):
                outputSize = outputSize+random.randint(10,100)
            else:
                outputSize = outputSize+random.randint(1,10)
            l = l -1
        if(timeTaken > 10):
            if(timeTaken < 100):
                timeTaken = timeTaken + random.randint(10,30)
            elif(timeTaken < 300):
                timeTaken = timeTaken + random.randint(10,50)
            elif(timeTaken < 600):
                timeTaken = timeTaken + random.randint(10,100)
            else:
                timeTaken = timeTaken + random.randint(10,200)
        dataLine = 'graph10,'+str(inputSize)+','+str(outputSize)+','+str(timeTaken)+',9'
        addLine('dataList/remodel/ml10.csv', dataLine)
        # addLine('dataList/remodel/level'+str(level)+'/ml10.csv',dataLine)
        index += 1