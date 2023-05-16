import numpy as np
import pandas as pd
import time
import os
import sys
from sklearn import svm
from sklearn import preprocessing
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

# Nodes for Machine Learning Graph G10
def preProcessCN(rawData):
  df = pd.read_csv(rawData)
  X=df.drop(columns=['taskType'])
  y=df.taskType
  return X,y

def trainCN(X, y):
  knn = KNeighborsClassifier(n_neighbors=12)
  knn.fit(X,y)
  return knn

def score(X, y, knn):
  return knn.score(X,y)