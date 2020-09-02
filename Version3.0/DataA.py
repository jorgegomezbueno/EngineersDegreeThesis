import os
import numpy as np
from tensorflow import keras
from keras_preprocessing.image import ImageDataGenerator
from PIL import Image



entries= os.listdir("./")
directorios=[]

for entry in entries:
    if ".py" not in entry:
        directorios.append(entry)

datagen= ImageDataGenerator(rotation_range=10,width_shift_range=0.1,height_shift_range=0.1,shear_range=0.15,zoom_range=0.1,channel_shift_range=10,horizontal_flip=True)

    
for directorio in directorios:
    imagenes=os.listdir("./"+directorio)
    images=[]
    for imagen in imagenes:
        image_path="./"+directorio+"/"+imagen
        images.append(np.asarray(Image.open(image_path)))
        

    images=np.array(images).reshape((np.array(images).shape[0], 50,50, 1))
    datagen.fit(images)
    for x,val in zip(datagen.flow(images,save_to_dir=directorio,save_prefix='aug',save_format='jpeg'),range(300)):
        pass