from os import listdir
from keras.applications.vgg16 import VGG16
from tensorflow.keras.utils import load_img
from tensorflow.keras.utils import img_to_array
from keras.applications.vgg16 import preprocess_input
from keras.models import Model
import string
import os
from keras.models import Model

# Nodes for Machine Learning Graph G5

# extract features from each photo in the directory
def extract_features(directory, index):
  # load the model
  model = VGG16()
  # re-structure the model
  model = Model(inputs=model.inputs, outputs=model.layers[-2].output)
  # extract features from each photo
  features = dict()
  count = 0
  while (count < index):
    for name in listdir(directory):
      # load an image from file
      if (name == "pic"+str(count)+".jpg"):
        filename = directory + '/' + name
        image = load_img(filename, target_size=(224, 224))
        # convert the image pixels to a numpy array
        image = img_to_array(image)
        # reshape data for the model
        image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))
        # prepare the image for the VGG model
        image = preprocess_input(image)
        # get features
        feature = model.predict(image, verbose=0)
        # get image id
        image_id = name.split('.')[0]
        # store feature
        features[image_id] = feature
        break
    count+=1
  
  

  return features