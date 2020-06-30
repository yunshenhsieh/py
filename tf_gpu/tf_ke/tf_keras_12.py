import numpy
import pandas as pd
from sklearn import preprocessing
import tf_keras_11
from keras.models import Sequential
from keras.layers import Dense,Dropout
import tf_keras_07

numpy.random.seed(10)
all_df = pd.read_excel("C:\\Users\\Big data\\Desktop\\data\\titanic3.xls")
cols=['survived','name','pclass','sex','age','sibsp','parch','fare','embarked']
all_df=all_df[cols]
msk = numpy.random.rand(len(all_df)) < 0.8
train_df = all_df[msk]
test_df = all_df[~msk]
train_Features,train_Label = tf_keras_11.PreprocessData(train_df)
test_Features,test_Label = tf_keras_11.PreprocessData(test_df)

model = Sequential()
model.add(Dense(units=40,input_dim=9,kernel_initializer='uniform',activation='relu'))
model.add(Dense(units=30,kernel_initializer='uniform',activation='relu'))
model.add(Dense(units=1,kernel_initializer='uniform',activation='sigmoid'))

model.compile(loss='binary_crossentropy',optimizer='adam',metrics=['accuracy'])
train_history = model.fit(x=train_Features,y=train_Label,validation_split=0.1,epochs=30,batch_size=30,verbose=2)

tf_keras_07.show_train_history(train_history,'accuracy','val_accuracy')
tf_keras_07.show_train_history(train_history,'loss','val_loss')

scores = model.evaluate(x=test_Features,y=test_Label)
print(scores[1])

Jack = pd.Series([0,'Jack',3,'male',23,1,0,5.0000,'S'])
Rose = pd.Series([1,'Rose',1,'female',20,1,0,100.0000,'S'])
JR_df=pd.DataFrame([list(Jack),list(Rose)],columns=['survived','name','pclass','sex','age','sibsp','parch','fare','embarked'])
all_df=pd.concat([all_df,JR_df])

all_Features,Label = tf_keras_11.PreprocessData(all_df)
all_probability = model.predict(all_Features)
pd=all_df
pd.insert(len(all_df.columns),'probability',all_probability)
print(pd[-2:])
print(pd[(pd['survived']==0) & (pd['probability'] > 0.9)])
print(pd[:5])