import random
import os
import time
import sys
import cv2
import image_dehazer

# Nodes for Graph G1

def loadImageIE(imgLoc):
  return cv2.imread(imgLoc)

def inverteIE(imagem):
  return (255-imagem)

def dehazeIE(img):
  return image_dehazer.remove_haze(img)

