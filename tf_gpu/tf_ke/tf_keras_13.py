import urllib.request
import os
import tarfile
from keras.preprocessing import sequence
from keras.preprocessing.text import Tokenizer
import re

url="http://ai.stanford.edu/~amaas/data/sentiment/aclImdb_v1.tar.gz"
filepath = "C:\\Users\\Big data\\Desktop\\data\\aclImdb_v1.tar.gz"
if not os.path.isfile(filepath):
    result = urllib.request.urlretrieve(url,filepath)
    print('downloaded :',result)
if not os.path.exists("C:\\Users\\Big data\\Desktop\\data\\aclImdb"):
    tfile=tarfile.open("C:\\Users\\Big data\\Desktop\\data\\aclImdb_v1.tar.gz",'r:gz')
    result=tfile.extractall("C:\\Users\\Big data\\Desktop\\data\\")

def rm_tags(text):
    re_tag = re.compile(r'<[^>]+>')
    return re_tag.sub('',text)

def read_files(filetype):
    path = "C:\\Users\\Big data\\Desktop\\data\\aclImdb\\"
    file_list=[]

    positive_path = path + filetype +"\\pos\\"
    for f in os.listdir(positive_path):
        file_list+=[positive_path + f]
    negative_path = path + filetype +"\\neg\\"
    for f in os.listdir(negative_path):
        file_list+=[negative_path + f]
    print('read',filetype,'files : ',len(file_list))
    all_labels = ([1] * 12500 + [0] * 12500)
    all_texts = []
    for fi in file_list:
        with open(fi,encoding='utf-8') as file_input:
            all_texts += [rm_tags(" ".join(file_input.readlines()))]
    return all_labels,all_texts

y_train,train_text=read_files('train')
y_test,test_text=read_files('test')

token = Tokenizer(num_words=2000)
token.fit_on_texts(train_text)

x_train_seq = token.texts_to_sequences(train_text)
x_test_seq = token.texts_to_sequences(test_text)

x_train = sequence.pad_sequences(x_train_seq,maxlen=100)
x_test = sequence.pad_sequences(x_test_seq,maxlen=100)
