import tensorflow as tf

ones = tf.ones([1,3])

with tf.Session() as sess:
    print(sess.run(ones))
