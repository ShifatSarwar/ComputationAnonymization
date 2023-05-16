import splitfolders
import keras
from keras.models import Sequential
from keras.layers import Dense, Conv2D , MaxPool2D , Flatten , Dropout 
from keras.preprocessing.image import ImageDataGenerator

from sklearn.metrics import classification_report,confusion_matrix

import tensorflow as tf
from tensorflow.keras.optimizers import Adam 

import cv2
import os
import numpy as np
import torch

import time
import os
import sys

# Nodes for Machine Learning Graph G2

# Get the Data
def split(dataLoc, fileLoc):
    splitfolders.ratio(dataLoc, fileLoc, seed=42, ratio=(0.7,0.3), group_prefix=None)
    return fileLoc

# Here we get augmented data
def get_data(data_dir, classList):
    data = [] 
    img_size = 224
    print(classList)
    for label in classList: 
        path = os.path.join(data_dir, label)
        class_num = classList.index(label)
        for img in os.listdir(path):
            try:
                img_arr = cv2.imread(os.path.join(path, img))[...,::-1]  #convert BGR to RGB format
                resized_arr = cv2.resize(img_arr, (img_size, img_size)) # Reshaping images to preferred size
                data.append([resized_arr, class_num])
            except Exception as e:
                print(e)
    return np.array(data)

# Get list of classess from folders
def getClass(fileLoc):
    classList = []
    index = 0
    for x in os.walk(fileLoc):
        curr = str(x[0])
        if index > 0:
            classList.append(curr.split('/')[6])
        index+=1
    return classList

# Data Train Test Split
def getSplit(train, val):
    img_size = 224
    x_train = []
    y_train = []
    x_val = []
    y_val = []

    for feature, label in train:
        x_train.append(feature)
        y_train.append(label)

    for feature, label in val:
        x_val.append(feature)
        y_val.append(label)

    # Normalize the data
    x_train = np.array(x_train) / 255
    x_val = np.array(x_val) / 255

    x_train.reshape(-1, img_size, img_size, 1)
    y_train = np.array(y_train)

    x_val.reshape(-1, img_size, img_size, 1)
    y_val = np.array(y_val)

    return x_train, y_train, x_val, y_val

# Data Augmentation on Train Set
def augmentTrain(x_train):
  
    datagen = ImageDataGenerator(
            featurewise_center=False,  # set input mean to 0 over the dataset
            samplewise_center=False,  # set each sample mean to 0
            featurewise_std_normalization=False,  # divide inputs by std of the dataset
            samplewise_std_normalization=False,  # divide each input by its std
            zca_whitening=False,  # apply ZCA whitening
            rotation_range = 30,  # randomly rotate images in the range (degrees, 0 to 180)
            zoom_range = 0.2, # Randomly zoom image 
            width_shift_range=0.1,  # randomly shift images horizontally (fraction of total width)
            height_shift_range=0.1,  # randomly shift images vertically (fraction of total height)
            horizontal_flip = True,  # randomly flip images
            vertical_flip=False)  # randomly flip images
    datagen.fit(x_train)

# Simple Deep Neural Network
def defineNetworkA(classList):
    model = Sequential()
    model.add(Conv2D(32,3,padding="same", activation="relu", input_shape=(224,224,3)))
    model.add(MaxPool2D())

    model.add(Conv2D(32, 3, padding="same", activation="relu"))
    model.add(MaxPool2D())

    model.add(Conv2D(64, 3, padding="same", activation="relu"))
    model.add(MaxPool2D())
    model.add(Dropout(0.4))

    model.add(Flatten())
    model.add(Dense(128,activation="relu"))
    model.add(Dense(len(classList), activation="softmax"))

    return model

def trainModel(model, x_train, y_train, x_val, y_val):
    model.compile(loss = 'sparse_categorical_crossentropy', 
        optimizer = "adam",               
                metrics = ['accuracy'])
    ep = 200
    model.fit(x_train,y_train,epochs = ep , validation_data = (x_val, y_val))
    return model

# Deep Neural Network with Group Normalization
def defineNetwork3():
    num_groups = 2
    # MNIST Classifier
    net = torch.nn.Sequential(
        torch.nn.Conv2d(224,7, kernel_size=2, stride=2, padding="same"),
        # GroupNorm takes number of groups to divide the
        # channels in and the number of channels to expect
        # in the input
        torch.nn.GroupNorm(num_groups, 7),
        torch.nn.ReLU(),
        torch.nn.MaxPool2d(kernel_size=3, stride=2),

        torch.nn.Conv2d(32, 64, kernel_size=5, stride=1, padding=2),
        torch.nn.GroupNorm(num_groups, 64),
        torch.nn.ReLU(),
        torch.nn.MaxPool2d(kernel_size=2, stride=2),
        torch.nn.Flatten(),
        torch.nn.Linear(7 * 7 * 64, 10),
        )
