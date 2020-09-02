import os
import numpy as np
from tensorflow import keras
import matplotlib.pyplot as plt
from PIL import Image
from PIL import ImageFile
from sklearn.metrics import confusion_matrix
import time

start_time=time.time()

entries= os.listdir("./")
directorios=[]
valor=3000
index=-1

train_images=[]
train_labels=[]
test_images=[]
test_labels=[]

for entry in entries:
    if ".py" not in entry:
        directorios.append(entry)

for directorio in directorios:
    index=index+1
    print("El label " + str(index) + " corresponde a la query "+ directorio)
    imagenes=os.listdir("./"+directorio)
    valor=len(imagenes)
    K=0
    for imagen in imagenes:
        if(K==valor):
            break
        image=Image.open("./"+directorio+"/"+imagen)
        if(K<(valor*0.75)-1):
            train_images.append(np.asarray(image))
            train_labels.append(index)
        else:
            test_images.append(np.asarray(image))
            test_labels.append(index)
        K=K+1


train_images = np.array(train_images).reshape((np.array(train_images).shape[0], 50,50, 1))
test_images = np.array(test_images).reshape((np.array(test_images).shape[0], 50, 50, 1))
train_images=np.array(train_images,dtype='float32')
test_images=np.array(test_images,dtype='float32')
train_images=(train_images.astype(np.float32)-127.5)/127.5
test_images=(test_images.astype(np.float32)-127.5)/127.5
input_shape=train_images[0].shape
Model=keras.Sequential([
     keras.layers.Conv2D(filters=32,kernel_size=(3,3),activation='relu',input_shape=input_shape),
     keras.layers.MaxPooling2D(pool_size=(2,2)),
     keras.layers.Conv2D(filters=32,kernel_size=(3,3),activation='relu'),
     keras.layers.MaxPooling2D(pool_size=(2,2)),
     keras.layers.Conv2D(filters=32,kernel_size=(3,3),activation='relu'),
     keras.layers.MaxPooling2D(pool_size=(2,2)),

     keras.layers.Flatten(),
     keras.layers.Dense(256,activation='relu'),
     keras.layers.Dense(len(directorios),activation='softmax')               
])
Model.summary()

Model.compile(loss='sparse_categorical_crossentropy',optimizer='adam',metrics=['accuracy'])
Model.fit(x=train_images,y=train_labels,epochs=15)
Model.evaluate(test_images,test_labels)

predictions= Model.predict_classes(test_images,batch_size=32,verbose=0)

print(confusion_matrix(predictions,test_labels))

print("--- %s seconds ---" % (time.time()-start_time))
