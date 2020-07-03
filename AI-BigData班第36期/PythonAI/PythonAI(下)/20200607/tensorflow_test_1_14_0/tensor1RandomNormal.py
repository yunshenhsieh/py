import tensorflow as tf
import matplotlib.pyplot as plt

random_normal = tf.random_normal( [100] , 0 , 1)

with tf.Session() as sess:
  print( random_normal.eval() )
  plt.hist( random_normal.eval() )
  plt.show()
