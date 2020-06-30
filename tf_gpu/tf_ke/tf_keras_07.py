from keras.utils import np_utils
import numpy as np
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
import matplotlib.pyplot as plt
from tf_ke import tf_keras_06
import pandas as pd

np.random.seed(10)
(x_train_image,y_train_label),(x_test_image,y_test_label)=mnist.load_data()
x_Train= x_train_image.reshape(60000,784).astype('float32')
x_Test = x_test_image.reshape(10000,784).astype('float32')
x_Train_normalize =x_Train/255
x_Test_normalize =x_Test/255
y_TrainOneHot=np_utils.to_categorical(y_train_label)
y_TestOneHot=np_utils.to_categorical(y_test_label)

model = Sequential()
# model.add(Dense(units=256,input_dim=784,kernel_initializer='normal',activation='relu'))
# model.add(Dense(units=10,kernel_initializer='normal',activation='softmax'))
model.add(Dense(units=1000,input_dim=784,kernel_initializer='normal',activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(units=1000,kernel_initializer='normal',activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(units=10,kernel_initializer='normal',activation='softmax'))
print(model.summary())

model.compile(loss='categorical_crossentropy',optimizer='adam',metrics=['accuracy'])
train_history = model.fit(x=x_Train_normalize,y=y_TrainOneHot,validation_split=0.2,epochs=10,batch_size=200,verbose=2)

def show_train_history(train_history,train,validation):
    plt.plot(train_history.history[train])
    plt.plot(train_history.history[validation])
    plt.title('Train History')
    plt.ylabel(train)
    plt.xlabel('Epoch')
    plt.legend(['train','validation'],loc='upper left')
    plt.show()
show_train_history(train_history,'acc','val_acc')
scores = model.evaluate(x_Test_normalize,y_TestOneHot)
print()
print('accuracy=',scores[1])

prediction = model.predict_classes(x_Test)

# print(pd.crosstab(y_test_label,prediction,rownames=['label'],colnames=['predict']))
df = pd.DataFrame({'label':y_test_label,'predict':prediction})
# print(df[:2])
# print(df[(df.label==5)&(df.predict==3)])
# tf_keras_06.plot_images_labels_prediction(x_test_image,y_test_label,prediction,idx=2526,num=1)