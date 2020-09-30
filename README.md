# EngineersDegreeThesis
Automated MachineLearning program that performs an image classification between the user requested classes

For the correct functioning of this project there is an order of execution of the different files, before starting the execution
make sure you are inside the cloned folder.

  1. First you should execute ```python3 CargaFlickr.py``` which will help you download the required datasets for the classification.
  2. After that you should use the ```python3 DataA.py``` file which will perform Data Augmentation techniques over the datasets, as a result we will obtain bigger datasets which will help to make our model perform better.
  3. Lastly you can execute ```python3 Conv2D.py``` which will create a Bidimension Convolutional Neural Network model to start classifying the images.

You should execute all files in the same folder in order to obtain the correct performance.
