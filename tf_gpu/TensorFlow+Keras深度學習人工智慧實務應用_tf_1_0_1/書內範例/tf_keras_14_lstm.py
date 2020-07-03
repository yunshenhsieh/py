from keras.datasets import imdb
from keras.preprocessing import sequence
from keras.preprocessing.text import Tokenizer
import tf_keras_13
from keras.models import Sequential
from keras.layers.core import Dense,Dropout,Activation,Flatten
from keras.layers.embeddings import Embedding
from keras.layers.recurrent import LSTM

y_train,train_text=tf_keras_13.read_files('train')
y_test,test_text=tf_keras_13.read_files('test')

token = Tokenizer(num_words=3800)
token.fit_on_texts(train_text)

x_train_seq=token.texts_to_sequences(train_text)
x_test_seq=token.texts_to_sequences(test_text)

x_train = sequence.pad_sequences(x_train_seq,maxlen=380)
x_test = sequence.pad_sequences(x_test_seq,maxlen=380)

model = Sequential()
model.add(Embedding(output_dim=32,input_dim=3800,input_length=380))
model.add(Dropout(0.2))
model.add(LSTM(32))
model.add(Dense(units=256,activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(units=1,activation='sigmoid'))
print(model.summary())
model.compile(loss='binary_crossentropy',optimizer='adam',metrics=['accuracy'])
train_history=model.fit(x_train,y_train,batch_size=100,epochs=10,verbose=2,validation_split=0.2)
scores = model.evaluate(x_test,y_test,verbose=1)
print(scores[1])
# predict=model.predict_classes(x_test)
# # print(predict[:10])
# predict_classes=predict.reshape(-1)
# # print(predict_classes[:10])
# SentimentDict={1:'正面的',0:'負面的'}
#
# def display_test_Sentiment(i):
#     print(test_text[i])
#     print('label真實值:',SentimentDict[y_test[i]],'預測結果:',SentimentDict[predict_classes[i]])
#
# display_test_Sentiment(2)
# display_test_Sentiment(12502)
#
# input_text = '''The movie from the first scene up to the end was emotionless and spiritless. I do appreciate that they didn't want to change the story much and keep the classic version for the most. Even when the movie was slightly tweaked, it was in the wrong dull way. Some tweaks don't really make sense and don't add up.
# I don't know whom should be blamed for the 'emotion delivery failure' is it the cast or the director? Emma Watson is good actress for some certain roles, but certainly not this one. She was very stiff. We couldn't differentiate her surprise from anger or love from sadness. In many scenes Belle and the Beast were talking so fast with no emotions, soul or spirit.
# It was as if they were rehearsing on a play by reading out loud from their scripts and the director was simply not there.Cinematography had a problem too. Too many close ups. The original cartoon had some close ups too, but Do they really have to copy everything as-is? The couple dancing scene cinematography could have been better.
# I really don't advise anyone to see this movie. Disney failed this time. It happens, though!. Hopefully we'll know what really happened.'''
#
# def predict_review(input_text):
#     input_seq = token.texts_to_sequences([input_text])
#     pad_input_seq = sequence.pad_sequences(input_seq,maxlen=380)
#     predict_result=model.predict_classes(pad_input_seq)
#     print(SentimentDict[predict_result[0][0]])
#
# predict_review(input_text)