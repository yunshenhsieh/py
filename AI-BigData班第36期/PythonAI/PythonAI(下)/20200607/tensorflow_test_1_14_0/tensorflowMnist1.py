import matplotlib.pyplot as plt
from tensorflow.examples.tutorials.mnist import input_data
import tensorflow as tf
import numpy as np

#載入mnist資料
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)
