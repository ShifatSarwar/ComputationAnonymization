import cv2

import time
import csv
import sys
import os

# Nodes for Object Detection Graph G3

def getFramesOD(filePath, index):
    filePath = filePath+"omunoodles.mov"
    vidcap = cv2.VideoCapture(filePath)
    success,image = vidcap.read()
    count = 0
    imageArray = []
    while success:
        imageArray.append(image)
        # cv2.imwrite("frame%d.jpg" % count, image) # save frame as JPEG file      
        success,image = vidcap.read()
        count += 1
        if(count == index*10):
            break
    vidcap.release()
    return imageArray

def preProcessImageOD(imageArray):
    count = 0
    scale_percent = 60 
    for x in imageArray:
        width = int(x.shape[1] * scale_percent / 100)
        height = int(x.shape[0] * scale_percent / 100)
        dim = (width, height)
        resize = cv2.resize(x, dim, interpolation = cv2.INTER_AREA)
        x = resize
        # cv2.imwrite("frame%d.jpg" % count, resize)
        count += 1
    return imageArray

def getClassOD(classPath):
    classPath = classPath+"classes.txt"
    class_name = []
    with open(classPath, 'r') as f:
        class_name = [cname.strip() for cname in f.readlines()]
    return class_name

def getModelOD(classPath):
    weights = classPath+'yolov4-tiny.weights'
    cfg = classPath+'yolov4-tiny.cfg'
    net = cv2.dnn.readNet(weights, cfg)
    # net.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
    # net.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA_FP16)
    model = cv2.dnn_DetectionModel(net)
    model.setInputParams(size=(416,416), scale=1/255, swapRB=True)
    return model

def getBoundingBoxesOD(model, imageArray, class_name):
    Conf_threshold = 0.4
    NMS_threshold = 0.4
    COLORS=[(0,255,0),(0,0,255),(255,0,0),(255,255,0),(255,0,255),(0,255,255)]
    starting_time = time.time()
    count = 0
    for x in imageArray:
        classes, scores, boxes = model.detect(x, Conf_threshold, NMS_threshold)
        for (classid, score, box) in zip(classes, scores, boxes):
            color = COLORS[int(classid) % len(COLORS)]
            label = "%s : %f" % (class_name[classid], score)
            cv2.rectangle(x, box, color, 1)
            cv2.putText(x, label, (box[0], box[1]-10),
                   cv2.FONT_HERSHEY_COMPLEX, 0.3, color, 1)
        endingTime = time.time() - starting_time
        fps = count/endingTime
        # print(fps)
        cv2.putText(x, f'FPS: {fps}', (20, 50),
               cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 255, 0), 2)
        # cv2.imshow('frame', x)
        # cv2.imwrite("frame%d.jpg" % count, x)
        key = cv2.waitKey(1)
        if key == ord('q'):
            break
        count += 1
    cv2.destroyAllWindows()
    return imageArray
