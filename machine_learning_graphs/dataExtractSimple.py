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
# from tensorflow.keras.datasets import fashion_mnist
from utility import *

import time
import os
import pickle
import pandas as pd
import cv2

import sys

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
def runImageEnhancement(path):
    img = loadImageIE(path)
    img = inverteIE(img)
    img = dehazeIE(img)
    return inverteIE(img)

# Connects and Extarct data for G2
def runDeepLearning(path): 
    fileLoc = path+'extra/flowers/'
    classList = getClass(path+'extra/flower_photos/')
    trainSet = get_data(fileLoc+'/train', classList)

    validationSet = get_data(fileLoc+'/val', classList)
    x_train, y_train, x_val, y_val = getSplit(trainSet, validationSet)
    augmentTrain(x_train)
    model = defineNetworkA(classList)
    hist = trainModel(model, x_train, y_train, x_val, y_val)
    return hist

# Connects and Extarct data for G3
def runObjectDetection(classPath, index):
    x = getFramesOD(classPath, index)
    x = preProcessImageOD(x)
    c = getClassOD(classPath)
    m = getModelOD(classPath)
    return getBoundingBoxesOD(m,x,c)

# Connects and Extarct data for G4
def runMultilabelAlgorithm(rawData):
    arxiv_data = getData(rawData)
    arxiv_data_filtered = filter_data(arxiv_data)
    arxiv_data_filtered = create_list_string(arxiv_data_filtered)
    train_df, test_df, val_df = split_train_test(arxiv_data_filtered)
    terms, lookup, vocab, max_seqlen, batch_size, padding_token, auto = get_preprocess_data(train_df)
    train_dataset = make_dataset(train_df,  max_seqlen, batch_size, padding_token, auto, lookup, is_train=True)
    validation_dataset = make_dataset(val_df,  max_seqlen, batch_size, padding_token, auto, lookup, is_train=False)
    test_dataset = make_dataset(test_df,  max_seqlen, batch_size, padding_token, auto, lookup, is_train=False)
    train_dataset, validation_dataset, test_dataset = vectorize(train_df, train_dataset, validation_dataset, test_dataset, auto)
    shallow_mlp_model = make_model(lookup)
    history = train_model(shallow_mlp_model, train_dataset, validation_dataset)
    return history

# Connects and Extarct data for G5
def runLanguageTranslationLSTM(pairs):
    english_sentences = [clean_sentence(pair[0]) for pair in pairs]
    french_sentences = [clean_sentence(pair[1]) for pair in pairs]
    french_text_tokenized, spa_text_tokenizer = tokenize(french_sentences)
    eng_text_tokenized, eng_text_tokenizer = tokenize(english_sentences)
    spanish_vocab = len(spa_text_tokenizer.word_index) + 1
    english_vocab = len(eng_text_tokenizer.word_index) + 1
    spa_pad_sentence, eng_pad_sentence, max_spanish_len, max_english_len= makeEqualLength(french_text_tokenized, eng_text_tokenized)
    getEmbeddingLayer(spanish_vocab, max_spanish_len)
    lstmEncoder(spanish_vocab, max_spanish_len)
    lstmDecoder(spanish_vocab, max_spanish_len, max_english_len)
    decoderL2(spanish_vocab, max_spanish_len, max_english_len)
    logits, input_sequence = denseLayer(spanish_vocab, max_spanish_len, max_english_len, english_vocab)
    enc_dec_model = getModel(logits, input_sequence)
    return train_model(enc_dec_model, eng_pad_sentence,spa_pad_sentence)

# Connects and Extarct data for G6
def runSyntheticGAN(x_train, y_train, x_test, y_test):
    img_shape = (28,28,1)
    z_dim = 100
    discrimination = discriminatorSG(img_shape)
    discrimination = compile_discriminatorSG(discrimination)
    generation = generatorSG(z_dim)
    cgano = cganSG(generation, discrimination)
    cgano = compile_cganSG(cgano)
    trainSG(generation, discrimination, cgano, x_train, y_train, x_test, y_test)


# Connects and Extarct data for G7
def runImageCaptioning(train):
    # descriptions
    train_descriptions = load_clean_descriptionsICT('extra/descriptions.txt', train)
    # photo features
    train_features = load_photo_featuresICT('extra/features.pkl', train)
    # prepare tokenizer
    tokenizer = create_tokenizerICT(train_descriptions)
    # save the tokenizer
    dump(tokenizer, open('extra/tokenizer.pkl', 'wb'))
    vocab_size = len(tokenizer.word_index) + 1
    # determine the maximum sequence length
    max_length = get_max_lengthICT(train_descriptions)
    # define the model
    model = define_modelICT(vocab_size, max_length)
    # train the model, run epochs manually and save after each epoch
    epochs = 10
    steps = len(train_descriptions)
    for i in range(epochs):
        # create the data generator
        generator = data_generatorICT(train_descriptions, train_features, tokenizer, max_length, vocab_size)
        # fit for one epoch
        model.fit_generator(generator, epochs=1, steps_per_epoch=steps, verbose=1)
        # save model
        model.save('models/model_last.h5')

# Connects and Extarct data for G8
def runImageCaptionGenerator(photoLoc):
    model = loadModelIC()
    # load the tokenizer
    tokenizer = loadTokenizerIC()
    # load and prepare the photograph
    photo = extract_featuresIC(photoLoc)
    description = generate_descIC(model, tokenizer, photo)
    writeToFileIC(description)

# Connects and Extarct data for G9
def runNeuralNetwork(rawData):
    X,y = preProcessNN(rawData)
    X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2, random_state=3, stratify=y)
    dummy_y, dummy_v = transformDataNN(y_train, y_test)
    return getModelNN(X_train, dummy_y)

# Connects and Extarct data for G10
def getClusterAnalysis(rawData):
    X,y = preProcessCN(rawData)
    X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2, random_state=3, stratify=y)
    return trainCN(X_train, y_train)

# The next part contains get methods that prepares the inputs and
# allows for monitoring the graph executions

# Prepares the data before passing to G1 to collect results from it
def getDataImageEnhance(loop):
    index = 0
    path = 'extra/Flicker8k_Dataset'
    for filename in os.listdir(path):
        index += 1
        f = os.path.join(path, filename)
        # checking if it is a file
        if os.path.isfile(f):
            inputSize = os.path.getsize(f)
        start_time = time.time()
        output = runImageEnhancement(f)
        timeTaken = time.time()-start_time
        outputSize = sys.getsizeof(output)
        dataLine = 'graph01,'+str(inputSize)+','+str(outputSize)+','+str(timeTaken)+',0'
        addLine('dataList/simple/ml1.csv',dataLine)
        if index == loop:
           break

# Prepares the data before passing to G2 to collect results from it
def getDataDeepLearning(loop):
    index = 100
    while(index <= loop):
        path = ''
        sizeA = getInputData(daisyLocA,daisyLocB, 5*index)
        sizeB = getInputData(roseLocA,roseLocB, 5*index)
        sizeC = getInputData(dandilionLocA,dandilionLocB, 7*index)
        sizeD = getInputData(sunflowerLocA,sunflowerLocB, 5*index)
        sizeE = getInputData(tulipLocA,tulipLocB, 6*index)
        inputSize = sizeA+sizeB+sizeC+sizeD+sizeE
        dataLoc = 'extra/flower_photos/'
        fileLoc = 'extra/flowers/'
        start_time = time.time()
        split(dataLoc,fileLoc)
        output = runDeepLearning(path)
        timeTaken = time.time()-start_time
        filename = 'models/finalized_model.sav'
        pickle.dump(output, open(filename, 'wb'))
        outputSize = os.path.getsize(filename)
        dataLine = 'graph02,'+str(inputSize)+','+str(outputSize)+','+str(timeTaken)+',1'
        addLine('dataList/simple/ml2.csv',dataLine)
        index += 1

# Prepares the data before passing to G3 to collect results from it
def getDataObjectDetection(loop):
    index = 5
    while(index < loop):
        classPath = 'extra/'
        inputSize = os.path.getsize(classPath+'classes.txt')
        start_time = time.time()
        output = runObjectDetection(classPath, index)
        timeTaken = time.time()-start_time
        outputSize = sys.getsizeof(output)
        inputSize = inputSize + outputSize
        dataLine = 'graph03,'+str(inputSize)+','+str(outputSize)+','+str(timeTaken)+',2'
        addLine('dataList/simple/ml3.csv',dataLine)
        index += 1

# Prepares the data before passing to G4 to collect results from it
def getDataMultilabelText(loop):
    index = 0
    while(index < loop):
        fileLoc = 'dataList/simple/trainset'+str(index)+'.csv'
        inputSize = os.path.getsize(fileLoc)
        start_time = time.time()
        output = runMultilabelAlgorithm(fileLoc)
        timeTaken = time.time()-start_time
        filename = 'modelsfinalized_model.sav'
        pickle.dump(output, open(filename, 'wb'))
        outputSize = os.path.getsize(filename)
        dataLine = 'graph04,'+str(inputSize)+','+str(outputSize)+','+str(timeTaken)+',3'
        addLine('dataList/simple/ml4.csv',dataLine)
        index += 1

# Prepares the data before passing to G5 to collect results from it 
def getDataLanguageLSTM(loop):
    index = 1
    while(index <= loop):
        fileLoc = 'extra/eng-fra.txt'
        pairs = getPairedData(fileLoc, index)
        inputSize = sys.getsizeof(pairs)
        start_time = time.time()
        output = runLanguageTranslationLSTM(pairs)
        timeTaken = time.time()-start_time
        filename = 'models/finalized_model.sav'
        pickle.dump(output, open(filename, 'wb'))
        outputSize = os.path.getsize(filename)
        dataLine = 'graph05,'+str(inputSize)+','+str(outputSize)+','+str(timeTaken)+',4'
        addLine('dataList/simple/ml5.csv',dataLine)
        index += 1

# Prepares the data before passing to G6 to collect results from it 
def getDataSyntheticGAN(loop):
    index = 1
    while(index <= loop):
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
        pd.DataFrame(arr_reshaped1).to_csv("dataList/simple/file1.csv")
        pd.DataFrame(arr_reshaped2).to_csv("dataList/simple/file2.csv")
        pd.DataFrame(arr_reshaped3).to_csv("dataList/simple/file3.csv")
        pd.DataFrame(arr_reshaped4).to_csv("dataList/simple/file4.csv")
        p = 'dataList/simple/file'
        inputSize = os.path.getsize(p+'1.csv')+os.path.getsize(p+'2.csv')+os.path.getsize(p+'3.csv')+os.path.getsize(p+'4.csv')
        start_time = time.time()
        runSyntheticGAN(x_train, y_train, x_test, y_test)
        timeTaken = time.time()-start_time
        outputSize = os.path.getsize('extra/samples/image.jpg')
        dataLine = 'graph06,'+str(inputSize)+','+str(outputSize)+','+str(timeTaken)+',5'
        addLine('dataList/simple/ml6.csv',dataLine)
        index += 1

# Prepares the data before passing to G7 to collect results from it    
def getDataImageCaptioning(loop):
    index = 1
    while(index <= loop):
        # extract features from all images
        directory = 'extra/Flicker8k_Dataset'
        features = extract_features(directory, index*100)
        # save to file output 1
        dump(features, open('extra/features.pkl', 'wb'))
        filename = 'extra/Flickr8k_text/Flickr8k.token.txt'
        createToken(index*100)
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
        createTrain(index*100-(0.2*index*100))
        filename = 'extra/trainset.txt'
        train = load_setICT(filename)
        inputSize = os.path.getsize('extra/features.pkl')
        inputSize = inputSize + os.path.getsize('extra/descriptions.txt')
        inputSize = inputSize + os.path.getsize('extra/Flickr8k_text/Flickr_8k.trainImages.txt')
        start_time = time.time()
        runImageCaptioning(train)
        timeTaken = time.time()-start_time
        outputSize = os.path.getsize('extra/model_last.h5')
        dataLine = 'graph07,'+str(inputSize)+','+str(outputSize)+','+str(timeTaken)+',6'
        addLine('dataList/simple/ml7.csv',dataLine)
        index += 1

# Prepares the data before passing to G8 to collect results from it 
def getDataImageCaption(loop):
    index = 0
    while(index < loop):
        # extract features from all images
        directory = 'extra/Flicker8k_Dataset/pic'+str(index)+'.jpg'
        inputSize = os.path.getsize(directory)
        start_time = time.time()
        runImageCaptionGenerator(directory)
        timeTaken = time.time()-start_time
        outputSize = os.path.getsize('extra/output.txt')
        dataLine = 'graph08,'+str(inputSize)+','+str(outputSize)+','+str(timeTaken)+',7'
        addLine('dataList/simple/ml8.csv',dataLine)
        index += 1

# Prepares the data before passing to G9 to collect results from it 
def getDataNeuralNetwork(loop):
    index = 0
    while(index < loop):
        fileLoc = 'extra/samples/csvs/trainset'+str(index)+'.csv'
        inputSize = os.path.getsize(fileLoc)
        start_time = time.time()
        output = runNeuralNetwork(fileLoc)
        timeTaken = time.time()-start_time
        filename = 'models/finalized_model.sav'
        pickle.dump(output, open(filename, 'wb'))
        outputSize = os.path.getsize(filename)
        dataLine = 'graph09,'+str(inputSize)+','+str(outputSize)+','+str(timeTaken)+',8'
        addLine('dataList/simple/ml9.csv',dataLine)
        index += 1

# Prepares the data before passing to G10 to collect results from it 
def getDataSimleCluster(loop):
    index = 0
    while(index < loop):
        fileLoc = 'extra/samples/csvs/trainset'+str(index)+'.csv'
        inputSize = os.path.getsize(fileLoc)
        start_time = time.time()
        output = getClusterAnalysis(fileLoc)
        timeTaken = time.time()-start_time
        filename = 'models/finalized_model.sav'
        pickle.dump(output, open(filename, 'wb'))
        outputSize = os.path.getsize(filename)
        dataLine = 'graph10,'+str(inputSize)+','+str(outputSize)+','+str(timeTaken)+',9'
        addLine('dataList/simple/ml10.csv',dataLine)
        index += 1







