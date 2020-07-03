from keras.datasets import mnist
from keras.utils import np_utils
from keras.models import Sequential
from keras.layers import Dense,Dropout,Flatten,Conv2D,MaxPooling2D
import pandas as pd
import numpy as np
import tf_keras_07,tf_keras_06
np.random.seed(10)
(x_Train,y_Train),(x_Test,y_Test)=mnist.load_data()
x_Train4D=x_Train.reshape(x_Train.shape[0],28,28,1).astype('float32')
x_Test4D=x_Test.reshape(x_Test.shape[0],28,28,1).astype('float32')
x_Train4D_normalize = x_Train4D/255
x_Test4D_normalize = x_Test4D/255
y_TrainOneHot = np_utils.to_categorical(y_Train)
y_TestOneHot = np_utils.to_categorical(y_Test)
model = Sequential()
model.add(Conv2D(filters=16,kernel_size=(5,5),padding='same',input_shape=(28,28,1),activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Conv2D(filters=36,kernel_size=(5,5),padding='same',activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dropout(0.25))
model.add(Flatten())
model.add(Dense(128,activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(10,activation='softmax'))

model.compile(loss='categorical_crossentropy',optimizer='adam',metrics=['accuracy'])
train_history=model.fit(x=x_Train4D_normalize,y=y_TrainOneHot,validation_split=0.2,epochs=10,batch_size=300,verbose=2)

tf_keras_07.show_train_history(train_history,'accuracy','val_accuracy')
tf_keras_07.show_train_history(train_history,'loss','val_loss')
scores = model.evaluate(x_Test4D_normalize,y_TestOneHot)
print(scores[1])

prediction=model.predict_classes(x_Test4D_normalize)
print(prediction[:10])
tf_keras_06.plot_images_labels_prediction(x_Test,y_Test,prediction,idx=0)

print(pd.crosstab(y_Test,prediction,rownames=['label'],colnames=['predict']))
