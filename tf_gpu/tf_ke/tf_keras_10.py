from keras.datasets import cifar10
import numpy as np
from keras.utils import np_utils
from keras.models import Sequential
from keras.layers import Dense,Dropout,Activation,Flatten,Conv2D,MaxPooling2D,ZeroPadding2D
from tf_ke import tf_keras_07,tf_keras_09
import matplotlib.pyplot as plt
import pandas as pd

np.random.seed(10)
(x_img_train,y_label_train),(x_img_test,y_label_test)=cifar10.load_data()
x_img_train_normalize = x_img_train.astype('float32')/255.0
x_img_test_normalize = x_img_test.astype('float32')/255.0
y_label_train_OneHot = np_utils.to_categorical(y_label_train)
y_label_test_OneHot = np_utils.to_categorical(y_label_test)
label_dict={0:"airplane",1:"automobile",2:"bird",3:"cat",4:"deer",5:"dog",6:"frog",7:"horse",8:"ship",9:'truck'}

model = Sequential()
model.add(Conv2D(filters=32,kernel_size=(3,3),input_shape=(32,32,3),activation='relu',padding='same'))
model.add(Dropout(rate=0.3))
model.add(Conv2D(filters=32,kernel_size=(3,3),activation='relu',padding='same'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Conv2D(filters=64,kernel_size=(3,3),activation='relu',padding='same'))
model.add(Dropout(0.3))
model.add(Conv2D(filters=64,kernel_size=(3,3),activation='relu',padding='same'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Conv2D(filters=128,kernel_size=(3,3),activation='relu',padding='same'))
model.add(Dropout(0.3))
model.add(Conv2D(filters=128,kernel_size=(3,3),activation='relu',padding='same'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Flatten())
model.add(Dropout(0.3))
model.add(Dense(2500,activation='relu'))
model.add(Dropout(0.3))
model.add(Dense(1500,activation='relu'))
model.add(Dropout(0.3))
model.add(Dense(10,activation='softmax'))

model.compile(loss='categorical_crossentropy',optimizer='adam',metrics=['accuracy'])
train_history=model.fit(x_img_train_normalize,y_label_train_OneHot,validation_split=0.2,epochs=10,batch_size=300,verbose=1)

tf_keras_07.show_train_history(train_history,'acc','val_acc')
tf_keras_07.show_train_history(train_history,'loss','val_loss')

scores = model.evaluate(x_img_test_normalize,y_label_test_OneHot,verbose=0)
print(scores[1])

prediction = model.predict_classes(x_img_test_normalize)
print(prediction[:10])
tf_keras_09.plot_images_labels_prediction(x_img_test,y_label_test,prediction,0,10)
Predicted_Probability =model.predict(x_img_test_normalize)

def show_Predicted_Probability(y,prediction,x_img,Predicted_Probability,i):
    print('label:',label_dict[y[i][0]],'predict:',label_dict[prediction[i]])
    plt.figure(figsize=(2,2))
    plt.imshow(np.reshape(x_img_test[i],(32,32,3)))
    plt.show()
    for j in range(10):
        print(label_dict[j]+' Probability:%1.9f' % (Predicted_Probability[i][j]))
# show_Predicted_Probability(y_label_test,prediction,x_img_test,Predicted_Probability,0)
# show_Predicted_Probability(y_label_test,prediction,x_img_test,Predicted_Probability,3)

print(pd.crosstab(y_label_test.reshape(-1),prediction,rownames=['label'],colnames=['predict']))