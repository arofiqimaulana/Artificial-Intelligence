# Goals : Membuat suatu program agar bisa mengenali bentuk tangan yang membentuk gunting, batu, atau kertas
# Tahapan 
"""
1. Persiapan input data
2. Pembentukan model
3. Evaluasi Model
"""

## 1. Persiapan Input Data
"""
Tahap ini dibagi menjadi
1. Memisahkan input data menjadi folder dengan struktur
    Train----Rock
         ----Paper
         ----Scissor
    Test ----Rock
         ----Paper
         ----Scissor
2. Load data input ke Google Colab
3. Load image ke dalam bentuk grayscale
4. Mengubah ukuran dan aspek rasio gambar
"""

import pandas as pd
import numpy as np
import os
import cv2
import tensorflow as tf
import sys
import pathlib
import matplotlib.pyplot as plt
import numpy
import random

## 2. Pembentukan Model
"""
Tahap ini dibagi menjadi
1. Transfer Learning
2. 

"""
data_dir = '/content/gdrive/My Drive/DATASET/Rock-Paper-Scissors/Train'
categories = ['paper','rock','scissors']

def ReadImage(data_dir,categories,img_size):
    training_data = []
    for k in categories:
        path = os.path.join(data_dir,k)
        class_num = categories.index(k)
        for img in os.listdir(path):
            try:
                img_array = cv2.imread(os.path.join(path,img),cv2.IMREAD_GRAYSCALE)
                new_array = cv2.resize(img_array,(img_size,img_size))
                training_data.append([new_array,class_num])
            except Exception as e:
                pass

    return random.shuffle(training_data)

X = []
y = []
for features, label in training_data:
  X.append(features)
  y.append(label)

X = np.array(X).reshape(-1,img_size,img_size,1)
X = X/225
y = np.array(y) 

def generateModel():    
    model = Sequential()

    model.add(Conv2D(64,(3,3),input_shape=X.shape[1:]))
    model.add(Activation("relu"))
    model.add(MaxPool2D(pool_size=(2,2)))

    model.add(Conv2D(64,(3,3)))
    model.add(Activation("relu"))
    model.add(MaxPool2D(pool_size=(2,2)))

    model.add(Flatten())
    model.add(Dense(64))

    model.add(Dense(1))
    model.add(Activation('sigmoid'))

    model.compile(loss="binary_crossentropy",
                optimizer="adam",
                metrics=['accuracy'])
    return model

model.fit(X,y,batch_size = 32,epochs=3,validation_split = 0.1)

## Alternatif Model

def generateModel():    
    model = Sequential()

    model.add(Conv2D(16,(3,3),input_shape=X.shape[1:]))
    model.add(Activation("relu"))
    model.add(MaxPool2D(pool_size=(2,2)))

    model.add(Conv2D(32,(3,3)))
    model.add(Activation("relu"))
    model.add(MaxPool2D(pool_size=(2,2)))

    model.add(Flatten())
    model.add(Dense(512),)

    model.add(Dense(1))
    model.add(Activation('softmax'))

    model.compile(loss="categorical_crossentropy",
                optimizer="adam",
                metrics=['accuracy'])
    return model


model.fit(X,y,batch_size = 32,epochs=3,validation_split = 0.1)






densenet = DenseNet121(include_top=False, weights='imagenet', classes=3,input_shape=(300,300,3))
densenet.trainable=True

def genericModel(base):
    model = Sequential()
    model.add(base)
    model.add(MaxPool2D())
    model.add(Flatten())
    model.add(Dense(3,activation='softmax'))
    model.compile(optimizer=Adam(),loss='categorical_crossentropy',metrics=['acc'])
    return model

dnet = genericModel(densenet)

history = dnet.fit(
    x=imgData,
    y=labels,
    batch_size = 16,
    epochs=8,
    callbacks=[checkpoint,es],
    validation_split=0.2
)

## 3. Evaluasi Model


## Refference
"""
1. https://medium.com/@RaghavPrabhu/understanding-of-convolutional-neural-network-cnn-deep-learning-99760835f148
2. https://towardsdatascience.com/building-a-rock-paper-scissors-ai-using-tensorflow-and-opencv-d5fc44fc8222
"""


## ALTERNATIF
data_dir = '/content/gdrive/My Drive/DATASET/Rock-Paper-Scissors/Train'
categories = ['paper','rock','scissors']

data_train = ImageDataGenerator(
	rescale=1./225,
	rotation_range=20,
	horizontal_flip=True,
	shear_range=0.2,
	fill_mode='wrap',
	validation_split = 0.2
	)

