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
