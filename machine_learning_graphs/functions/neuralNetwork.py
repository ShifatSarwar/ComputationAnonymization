from keras.models import Sequential
from keras.layers import Dense
from keras.utils import np_utils
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import pandas as pd

# Nodes for Machine Learning Graph G9

def preProcessNN(rawData):
  df = pd.read_csv(rawData)
  X=df.drop(columns=['taskType'])
  y=df.taskType
  return X,y


def transformDataNN(y_train, y_test):
  encoder = LabelEncoder()
  encoder.fit(y_train)
  encoded_Y = encoder.transform(y_train)
  dummy_y = np_utils.to_categorical(encoded_Y)
  encoder.fit(y_test)
  encode_V = encoder.transform(y_test)
  dummy_v = np_utils.to_categorical(encode_V)
  return dummy_y,dummy_v

def getModelNN(X_train, dummy_y):
  model = Sequential()
  model.add(Dense(1000, input_dim=5, activation='relu'))
  model.add(Dense(1000, activation='relu'))
  model.add(Dense(12, activation='softmax'))
  model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
  model.fit(X_train, dummy_y, epochs=100, batch_size=64)
  return model

def getScore(X_test, dummy_v,model):
  result = model.evaluate(X_test, dummy_v, batch_size=64)
  return result