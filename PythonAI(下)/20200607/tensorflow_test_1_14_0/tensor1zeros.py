import tensorflow as tf

zeros = tf.zeros([1,3])

with tf.Session() as sess:
    print(sess.run(zeros))
