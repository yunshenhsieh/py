import tensorflow as tf

fill = tf.fill([1,3],5)

with tf.Session() as sess:
    print(sess.run(fill))
