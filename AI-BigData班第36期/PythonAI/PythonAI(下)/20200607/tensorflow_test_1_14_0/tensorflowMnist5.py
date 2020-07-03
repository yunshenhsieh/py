import matplotlib.pyplot as plt
from tensorflow.examples.tutorials.mnist import input_data
import tensorflow as tf
import numpy as np

#載入mnist資料
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)

# 檢視結構
print('訓練資料集的圖像的結構{}'.format( mnist.train.images.shape))
print('訓練資料集的圖像標註的結構{}'.format( mnist.train.labels.shape))
print('訓練資料集的圖像的總數={}'.format( len( mnist.train.images)))
print('訓練資料集的第一個圖像(張量)= ={}'.format( mnist.train.images[1]))
print('訓練資料集的第一個圖像標註的張量顯示={}'.format( mnist.train.labels[1]))

#定義一個函數,將圖像資料轉換成28x28矩陣
def data_to_matrix(data):
    return np.reshape(data, (28, 28))

#轉換 訓練資料集的第一個圖像數組 為矩陣
matrix = data_to_matrix(mnist.train.images[1])

plt.figure()

#畫出矩陣
plt.imshow(matrix)
plt.title('the first image and label is {}'.format( np.argmax(mnist.train.labels[1])))
plt.matshow(matrix, cmap=plt.get_cmap('gray'))
plt.title("the first image and label is {}".format(np.argmax(mnist.train.labels[1])))
plt.show()

x = tf.placeholder(tf.float32, shape=[None, 784])
Y = tf.placeholder(tf.float32, shape=[None, 10])

W = tf.Variable(tf.zeros([784,10]))
b = tf.Variable(tf.zeros([10]))

#模型公式
y_ = tf.matmul(x, W) + b

lr = 0.5
batch_size = 1000
epochs = 1000
epoch_list=[]
accuracy_list=[]
loss_list=[]

#設定成本函數
loss = tf.reduce_mean( tf.nn.softmax_cross_entropy_with_logits(labels=Y, logits=y_))
train = tf.train.GradientDescentOptimizer(lr).minimize(loss)

#計算正確率
correct_prediction = tf.equal(tf.argmax(y_,1), tf.argmax(Y,1))
cp = tf.cast(correct_prediction, tf.float32)
accuracy = tf.reduce_mean(cp)
