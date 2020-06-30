import tensorflow as tf
import matplotlib.pyplot as plt

n = 5000000
A = tf.truncated_normal([n,])
B = tf.random_normal([n,])
with tf.Session() as sess:
    a, b = sess.run([A, B])
    plt.hist(b, 100, (-5, 5));
    plt.show()
    plt.hist(a, 100, (-5, 5));
    plt.show()
